from ui.mainwindow import Ui_MainWindow
from PySide6.QtWidgets import (QMainWindow, QListWidgetItem, QListView)
from PySide6.QtGui import (QIcon, QFont)
from PySide6.QtCore import (QPropertyAnimation, QEasingCurve, QSize, QThread)
from utils.functionutils import *
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lw_breakthroughs.hide()

        # coloco los íconos en cada widget
        icon:QIcon = QIcon()
        icon.addFile("icons/icons8-menu-24.png")
        self.ui.btn_sidebar_toggle.setIcon(icon)

        # dataframe con innovaciones
        self.dataframe:pd.DataFrame = pd.read_csv("MapData_Breakthroughs.csv")

        # determina las políticas del ancho de las columnas de la tabla
        setTableWidthPolitics(self.ui.tw_mapdata)

        # señales
        self.ui.btn_sidebar_toggle.clicked.connect(self.toggleSidebar)
        self.ui.le_searchbar.returnPressed.connect(lambda: self.handleFillTableWidget(self.ui.le_searchbar.text()) )
        self.ui.lw_breakthroughs.itemPressed.connect(lambda item: self.handleFillTableWidget(item.text(), True) )


    
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
        filtered_res:pd.DataFrame | None
        
        if search_text.strip(): # si el texto no está vacío...
            if not list_selected: # si no se selecciona desde lw_breakthroughs...
                # convierte el texto a palabras clave
                search_text = search_text.split()

            # filtra los registros
            filtered_res = filterMaps(self.dataframe, search_text)

            # define la cantidad de filas de la tabla
            if filtered_res:
                self.ui.tw_mapdata.setRowCount(filtered_res.shape[0])

                # por cada columna crea los widgets correspondientes
            
        return None




class 