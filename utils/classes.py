from ui.mainwindow import Ui_MainWindow
from PySide6.QtWidgets import (QMainWindow, QListWidgetItem, QListView)
from PySide6.QtGui import (QIcon, QFont)
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

        # coloco los íconos en cada widget
        icon:QIcon = QIcon()
        icon.addFile("icons/icons8-menu-24-dark.png")
        self.ui.btn_sidebar_toggle.setIcon(icon)

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

        # TODO: crear señal para el botón brn_show_more

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

            print("handleFillTableWidget")
            self.begin_filtering.emit(self.dataframe, search_text)

        return None


    def showMapsInTable(self, filtered_indexes:tuple | None) -> None:
        '''Recibe una tupla con los índices que coincidieron con los criterios de búsqueda.
        \nDetermina la cantidad de filas de la tabla, crea los widgets necesarios para cada columna y asigna los \
        datos.
        \nRetorna None.'''
        filtered_df:pandas.DataFrame

        # convierte la lista de índices en tupla para que sea más rápida
        self.filtered_indexes = tuple(self.filtered_indexes)

        # crea un dataframe nuevo con los mapas filtrados
        filtered_df = self.dataframe.loc[filtered_indexes]

        # especifica la cantidad de filas inicial de la tabla
        self.ui.tw_mapdata.setRowCount(100 if filtered_df.shape[0] >= 100 else filtered_df.shape[0])

        return None






class FilterMapsWorker(QObject):
    # si se encontraron resultados envía un dataframe filtrado, sino envía None
    progress:Signal = Signal(object)
    completed:Signal = Signal(None)
    
    @Slot(pandas.DataFrame, str)
    def filterMapsByTerms(self, df:pandas.DataFrame, search_terms:str) -> None:
        # el for recorre todas las filas, iterrows() devuelve el índice y la Serie...
        for row_idx, serie in df.loc[:5000, "Coordenadas":"Innovación 12"].iterrows():

            # en cada Serie verifica que TODAS los 'search_terms' estén en las columnas (no importa en cuáles, pero entre todas)...
            if all(word.lower() in ' '.join(map(str, serie)).lower() for word in search_terms):
                # si están todas las palabras, emite el índice de la Serie
                self.progress.emit(row_idx)

                # TODO: permitir al usuario buscar por columnas específicas: ej.: agua=4; concreto=2; etc.

        self.completed.emit()
        return None