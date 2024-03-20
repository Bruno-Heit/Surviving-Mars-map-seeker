from ui.mainwindow import Ui_MainWindow
from ui.coordinatesdatawidget import Ui_CoordinatesDataWidget
from ui.resourcesdatawidget import Ui_ResourcesDataWidget

import os

from PySide6.QtWidgets import (QMainWindow, QWidget)
from PySide6.QtGui import (QIcon, QPixmap)
from PySide6.QtCore import (QPropertyAnimation, QEasingCurve, QSize, QThread, QObject, Signal, Slot)

from utils.functionutils import *

import pandas


class MainWindow(QMainWindow):
    begin_filtering:Signal = Signal(pandas.DataFrame, str)
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lw_breakthroughs.hide()

        # coloca el ícono en btn_sidebar_toggle
        icon:QIcon = QIcon()
        icon.addFile("icons/menu.svg", QSize(24, 24))
        self.ui.btn_sidebar_toggle.setIcon(icon)

        # añado efecto box-shadow fluorescente a los widgets
        addGlowToBorder(self.ui.btn_sidebar_toggle)
        addGlowToBorder(self.ui.le_searchbar)
        addGlowToBorder(self.ui.btn_show_more)

        # dataframe con innovaciones
        self.dataframe:pandas.DataFrame = pandas.read_csv("MapData_Breakthroughs.csv")
        # lista de términos de búsqueda
        self.search_terms:str = None
        # lista de índices coincidentes
        self.filtered_indexes:list = []

        # determina las políticas del ancho de las columnas de la tabla
        setTableWidthPolitics(self.ui.tw_mapdata)

        # Thread y worker para QThread
        self.filter_worker = FilterMapsWorker()
        self.thread = QThread()

        self.filter_worker.moveToThread(self.thread)

        # señales
        self.ui.btn_sidebar_toggle.clicked.connect(self.toggleSidebar)
        self.ui.le_searchbar.returnPressed.connect(lambda: self.handleFillTableWidget(self.ui.le_searchbar.text()) )
        self.ui.lw_breakthroughs.itemPressed.connect(lambda item: self.handleFillTableWidget(item.text(), True) )
        self.ui.btn_show_more.clicked.connect(self.showMoreMaps)


        # señal de filter_worker
        self.filter_worker.progress.connect(lambda index: self.filtered_indexes.append(index))
        self.filter_worker.completed.connect(lambda: self.showMapsInTable(self.filtered_indexes))
        self.begin_filtering.connect(self.filter_worker.filterMapsByTerms)

        # inicio el thread (sino no funciona)
        self.thread.start()


    def toggleSidebar(self) -> None:
        '''Abre/cierra la sidebar.
        \nRetorna None.'''
        start_val:int
        end_val:int
        show_list:int
        anim:QPropertyAnimation
        icon:QIcon

        start_val = self.ui.sidebar.width()
        end_val = 250 if start_val < 250 else 40
        show_list = 1 if end_val == 250 else 0

        # funciones de animación
        anim = QPropertyAnimation(self.ui.sidebar, b"minimumWidth", self.ui.body)
        anim.setDuration(150)
        anim.setStartValue(start_val)
        anim.setEndValue(end_val)
        anim.setEasingCurve(QEasingCurve.Type.InOutCubic)
        anim.start()

        # muestra/esconde la lista de breakthroughs
        self.ui.lw_breakthroughs.show() if show_list else self.ui.lw_breakthroughs.hide()
        self.ui.lw_breakthroughs.setEnabled(False if self.ui.lw_breakthroughs.isHidden() else True)

        return None


    def handleFillTableWidget(self, search_text:str, list_selected:bool=False) -> None:
        '''Maneja funciones para leer el archivo ".csv", filtrar por términos y llenar la tabla "tw_mapdata".
        \nSi 'list_selected' es True es porque se selecciona una innovación desde 'lw_breakthroughs', si False \
        se seleccionó desde 'le_searchbar'.
        \nRetorna None.'''
        if search_text.strip(): # si el texto no está vacío...
            if not list_selected: # si no se selecciona desde lw_breakthroughs...
                # convierte el texto a palabras clave
                search_text = search_text.split()

            self.begin_filtering.emit(self.dataframe, search_text)

        return None


    def showMapsInTable(self, filtered_indexes:tuple | None) -> None:
        '''Recibe una tupla con los índices que coincidieron con los criterios de búsqueda.
        \nDetermina la cantidad de filas de la tabla, crea los widgets necesarios para cada columna y asigna los \
        datos.
        \nRetorna None.'''
        filtered_df:pandas.DataFrame
        coords_data_widget:CoordinatesDataWidget # widget que muestra las coordenadas y topografía del mapa

        # convierte la lista de índices en tupla para que sea más rápida
        self.filtered_indexes = tuple(self.filtered_indexes)

        # crea un dataframe nuevo con los mapas filtrados
        filtered_df = self.dataframe.loc[filtered_indexes]

        # especifica la cantidad de filas inicial de la tabla (muestra 25)
        self.ui.tw_mapdata.setRowCount(25 if filtered_df.shape[0] >= 25 else filtered_df.shape[0])

        # TODO: crear los widgets necesarios para cada columna acá
        for row in range(self.ui.tw_mapdata.rowCount()):
            # columna 0: coordenadas/topografía
            coords_data_widget = CoordinatesDataWidget(coords=self.dataframe.at[self.filtered_indexes[row], "Coordenadas"],
                                                       topography=self.dataframe.at[self.filtered_indexes[row], "Topografía"])
            self.ui.tw_mapdata.setCellWidget(row, 0, coords_data_widget)
            # columna 1: recursos
            resources_data_widget = ResourcesDataWidget(metals_level=self.dataframe.at[self.filtered_indexes[row], "Metales"],
                                                        rare_metals_level=self.dataframe.at[self.filtered_indexes[row], "Metales raros"],
                                                        concrete_level=self.dataframe.at[self.filtered_indexes[row], "Concreto"],
                                                        water_level=self.dataframe.at[self.filtered_indexes[row], "Agua"])
            self.ui.tw_mapdata.setCellWidget(row, 1, resources_data_widget)
            self.ui.tw_mapdata.setColumnWidth(1, 184)

            # columna 2: dificultad

            # columna 3: innovaciones

        self.ui.tw_mapdata.resizeRowsToContents()
        return None


    def showMoreMaps(self) -> None:
        '''Añade otros 25 mapas a la tabla 'tw_mapdata'.
        \nPara hacerlo, toma el índice del último mapa mostrado en la tabla y busca en el archivo ".csv"\
        los 25 siguientes índices coincidentes guardados en 'self.filtered_indexes'.
        \nRetorna None.'''
        # TODO: tomar el índice del último mapa coincidente, pero para eso primero tengo que crear 
        # todo: los widgets.
        pass




class FilterMapsWorker(QObject):
    '''Clase que maneja la función y las señales que sirven para filtrar mapas en un thread/hilo aparte usando un worker.'''
    # si se encontraron resultados envía un dataframe filtrado, sino envía None
    progress:Signal = Signal(object)
    completed:Signal = Signal(None)
    
    @Slot(pandas.DataFrame, str)
    def filterMapsByTerms(self, df:pandas.DataFrame, search_terms:str) -> None:
        # el for recorre todas las filas, iterrows() devuelve el índice y la Serie...
        for row_idx, serie in df.loc[:1000, "Coordenadas":"Innovación 12"].iterrows():

            # en cada Serie verifica que TODAS los 'search_terms' estén en las columnas (no importa en cuáles, pero entre todas)...
            if all(word.lower() in ' '.join(map(str, serie)).lower() for word in search_terms):
                # si están todas las palabras, emite el índice de la Serie
                self.progress.emit(row_idx)

                # TODO: permitir al usuario buscar por columnas específicas: ej.: agua=4; concreto=2; etc.

        self.completed.emit()
        return None





class CoordinatesDataWidget(QWidget):
    '''Clase simple que muestra las coordenadas del mapa y la topografía.'''
    def __init__(self, coords:str, topography:str):
        super(CoordinatesDataWidget, self).__init__()
        self.coord_ui = Ui_CoordinatesDataWidget()
        self.coord_ui.setupUi(self)

        self.coord_ui.label_coords.setText(coords)
        self.coord_ui.label_topography.setText(topography)





class ResourcesDataWidget(QWidget):
    '''Clase simple que muestra los 4 recursos disponibles en el mapa al comienzo.'''
    def __init__(self, metals_level:int, rare_metals_level:int, concrete_level:int, water_level:int):
        super(ResourcesDataWidget, self).__init__()
        self.resrc_ui = Ui_ResourcesDataWidget()
        self.resrc_ui.setupUi(self)

        # TODO: cambiar qss de mainwindow usando paleta de azules igual que la gui del juego.

        # coloca los íconos de cada recurso
        metals_icon = QPixmap("icons/metals.ico")
        self.resrc_ui.label_metals_icon.setPixmap(metals_icon)
        rare_metals_icon = QPixmap("icons/rare_metals.ico")
        self.resrc_ui.label_rare_metals_icon.setPixmap(rare_metals_icon)
        concrete_icon = QPixmap("icons/concrete.ico")
        self.resrc_ui.label_concrete_icon.setPixmap(concrete_icon)
        water_icon = QPixmap("icons/water.ico")
        self.resrc_ui.label_water_icon.setPixmap(water_icon)

        # coloca los valores de los recursos del mapa en los labels
        self.resrc_ui.label_metals_level.setText(f"{metals_level}")
        self.resrc_ui.label_rare_metals_level.setText(f"{rare_metals_level}")
        self.resrc_ui.label_concrete_level.setText(f"{concrete_level}")
        self.resrc_ui.label_water_level.setText(f"{water_level}")
