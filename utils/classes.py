from ui.mainwindow import Ui_MainWindow
from ui.coordinatesdatawidget import Ui_CoordinatesDataWidget
from ui.resourcesdatawidget import Ui_ResourcesDataWidget

from resources import (rc_icons, rc_images)

from PySide6.QtWidgets import (QMainWindow, QWidget)
from PySide6.QtGui import (QIcon, QPaintEvent, QPixmap)
from PySide6.QtCore import (QPropertyAnimation, QEasingCurve, QSize, QThread, QObject, Signal, Slot, QEvent, Qt)

from utils.functionutils import *

import pandas
from re import (findall, IGNORECASE)



class MainWindow(QMainWindow):
    begin_filtering:Signal = Signal(pandas.DataFrame, object)
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lw_breakthroughs.hide()
        self.ui.pb_searchingdata.hide()

        # coloca el ícono en btn_sidebar_toggle
        icon:QIcon = QIcon()
        icon.addFile(":/icons/menu.svg", QSize(24, 24))
        self.ui.btn_sidebar_toggle.setIcon(icon)

        # añado efecto box-shadow fluorescente a los widgets
        addGlowToBorder(self.ui.btn_sidebar_toggle)
        addGlowToBorder(self.ui.le_searchbar)
        addGlowToBorder(self.ui.btn_show_more)
        addGlowToBorder(self.ui.pb_searchingdata)

        # dataframe con innovaciones
        pandas_usecols:list[str] = [
            "Coordenadas","Topografía","Dificultad_del_desafío","Altitud","Temperatura","Metales","Metales_raros",
            "Concreto","Agua","Remolinos_de_polvo","Tormentas_de_arena","Meteoros","Olas_de_frío","Innovación_1",
            "Innovación_2","Innovación_3","Innovación_4","Innovación_5","Innovación_6","Innovación_7","Innovación_8",
            "Innovación_9","Innovación_10","Innovación_11","Innovación_12"
            ]
        pandas_dtype:dict[str:str] = {
            "Coordenadas":"string",
            "Topografía":"string",
            "Dificultad_del_desafío":"uint16",
            "Altitud":"int16",
            "Temperatura":"int16",
            "Metales":"uint8",
            "Metales_raros":"uint8",
            "Concreto":"uint8",
            "Agua":"uint8",
            "Remolinos_de_polvo":"uint8",
            "Tormentas_de_arena":"uint8",
            "Meteoros":"uint8",
            "Olas_de_frío":"uint8",
            "Innovación_1":"string",
            "Innovación_2":"string",
            "Innovación_3":"string",
            "Innovación_4":"string",
            "Innovación_5":"string",
            "Innovación_6":"string",
            "Innovación_7":"string",
            "Innovación_8":"string",
            "Innovación_9":"string",
            "Innovación_10":"string",
            "Innovación_11":"string",
            "Innovación_12":"string"
        }
        self.dataframe:pandas.DataFrame = pandas.read_csv("MapData_Breakthroughs.csv", header=0, usecols=pandas_usecols, dtype=pandas_dtype)
        
        # lista de términos de búsqueda
        self.search_terms:str = None
        # lista de índices coincidentes
        self.filtered_indexes:list = []

        # determina las políticas del ancho de las columnas de la tabla
        setTableWidthPolitics(self.ui.tw_mapdata)

        # Thread y worker para QThread
        self.filter_worker = FilterMapsWorker()
        self.filter_thread = QThread()

        self.filter_worker.moveToThread(self.filter_thread)

        # ############ señales ############################################################
        self.ui.btn_sidebar_toggle.clicked.connect(self.toggleSidebar)
        self.ui.le_searchbar.returnPressed.connect(lambda: self.handleFillTableWidget(self.ui.le_searchbar.text()) )
        self.ui.lw_breakthroughs.itemPressed.connect(lambda item: self.handleFillTableWidget(item.text(), True) )
        self.ui.btn_show_more.clicked.connect(self.showMoreMaps)

        # señal de filter_worker
        self.filter_worker.progress.connect(lambda index: self.filteringProgressMade(index))
        self.filter_worker.completed.connect(lambda: self.filteringMapsFinished(self.filtered_indexes))
        self.begin_filtering.connect(self.filter_worker.filterMapsByTerms)

        # inicio el thread (sino no funciona)
        self.filter_thread.start()


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
        search_terms:list[str]
        columns_list:pandas.Index[str]
        pattern:str
        re_res:list

        if search_text.strip() != "": # si el texto no está vacío...
            if not list_selected: # si no se selecciona desde lw_breakthroughs...
                # convierte el texto a palabras clave
                search_terms = search_text.split(",")

                search_terms = [term.strip() for term in search_terms]
            
            # TODO: verificar si se está buscando en alguna columna específica, y crear un pandas.df.query()

            self.begin_filtering.emit(self.dataframe, search_terms)

        return None


    def filteringProgressMade(self, index:int) -> None:
        '''Si se logra algún progreso mientras se filtran los criterios de búsqueda, se recibe el índice del \
        mapa encontrado y se lo guarda en la lista 'self.filtered_indexes', pero si el largo de la lista llega \
        a 25 se reinicia la lista.
        \nAdemás anima los cambios entre 'chunks' de la barra de progreso 'pb_searchingdata'.
        \nRetorna None.'''
        self.filtered_indexes.append(index) if len(self.filtered_indexes) <= 25 else self.filtered_indexes.clear()

        # si pb_searchingdata está escondido es porque recién comienza a buscar FilterMapsWorker
        if self.ui.pb_searchingdata.isHidden():
            self.ui.pb_searchingdata.show()
            self.ui.pb_searchingdata.setEnabled(True)
            self.ui.pb_searchingdata.reset()

        self.ui.pb_searchingdata.setValue(len(self.filtered_indexes))
        return None


    def filteringMapsFinished(self, filtered_indexes:tuple | None) -> None:
        '''Una vez que se terminan de filtrar los criterios de búsqueda, recibe una tupla con los índices que \
        coincidieron.
        \nDetermina la cantidad de filas de la tabla, crea los widgets necesarios para cada columna y asigna los \
        datos. Adicionalmente esconde la barra de progreso 'pb_searchingdata'.
        \nRetorna None.'''
        filtered_df:pandas.DataFrame
        coords_data_widget:CoordinatesDataWidget # widget que muestra las coordenadas y topografía del mapa

        # reinicia el value de pb_searchingdata y lo esconde
        self.ui.pb_searchingdata.reset()
        self.ui.pb_searchingdata.hide()

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
                                                        rare_metals_level=self.dataframe.at[self.filtered_indexes[row], "Metales_raros"],
                                                        concrete_level=self.dataframe.at[self.filtered_indexes[row], "Concreto"],
                                                        water_level=self.dataframe.at[self.filtered_indexes[row], "Agua"])
            self.ui.tw_mapdata.setCellWidget(row, 1, resources_data_widget)
            self.ui.tw_mapdata.setColumnWidth(1, 184)

            # columna 2: dificultad

            # columna 3: innovaciones
        
        # vuelve a convertirla a lista
        self.filtered_indexes = list(self.filtered_indexes)

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
    '''Clase que maneja la función y las señales que sirven para filtrar mapas en un thread/hilo aparte usando un worker. 
    Filtra de a 25 mapas.'''
    # si se encontraron resultados envía un dataframe filtrado, sino envía None
    progress:Signal = Signal(object)
    completed:Signal = Signal(None)
    
    @Slot(pandas.DataFrame)
    def filterMapsByTerms(self, df:pandas.DataFrame, search_terms:list[str]) -> None:
        print(search_terms)

        cont:int = 0 # cuenta los mapas coincidentes, cuando llega a 25 sale del bucle
        
        # el for recorre todas las filas, iterrows() devuelve el índice y la Serie...
        for row_idx, serie in df.loc[0:, "Coordenadas":"Innovación_12"].iterrows():

            # en cada Serie verifica que TODAS los 'search_terms' estén en las columnas (no importa en cuáles, pero entre todas)...
            if all(word.lower() in ' '.join(map(str, serie)).lower() for word in search_terms) and cont < 25:

                # si están todas las palabras, emite el índice de la Serie
                self.progress.emit(row_idx)
                cont += 1

            elif cont == 25:
                break

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

        # coloca los íconos de cada recurso
        metals_icon = QPixmap(":/icons/metals.ico")
        self.resrc_ui.label_metals_icon.setPixmap(metals_icon)
        rare_metals_icon = QPixmap(":/icons/rare_metals.ico")
        self.resrc_ui.label_rare_metals_icon.setPixmap(rare_metals_icon)
        concrete_icon = QPixmap(":/icons/concrete.ico")
        self.resrc_ui.label_concrete_icon.setPixmap(concrete_icon)
        water_icon = QPixmap(":/icons/water.ico")
        self.resrc_ui.label_water_icon.setPixmap(water_icon)

        # coloca los valores de los recursos del mapa en los labels
        self.resrc_ui.label_metals_level.setText(f"{metals_level}")
        self.resrc_ui.label_rare_metals_level.setText(f"{rare_metals_level}")
        self.resrc_ui.label_concrete_level.setText(f"{concrete_level}")
        self.resrc_ui.label_water_level.setText(f"{water_level}")
