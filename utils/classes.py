from ui.mainwindow import Ui_MainWindow
from PySide6.QtWidgets import (QMainWindow)
from PySide6.QtGui import (QIcon)
from PySide6.QtCore import (QPropertyAnimation, QEasingCurve, QSize)
from utils.functionutils import (setTableWidthPolitics, searchTextToRegex)
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lw_breakthroughs.hide()

        # TODO: corregir, lw_breakthroughs muestra los items en columnas una al lado de la otra

        # coloco los íconos en cada widget
        icon:QIcon = QIcon()
        icon.addFile("icons/icons8-menu-24.png")
        self.ui.btn_sidebar_toggle.setIcon(icon)

        # declaro el dataframe (se inicializa en 'self.handleFillTableWidget')
        self.dataframe:pd.DataFrame

        # determina las políticas del ancho de las columnas de la tabla
        setTableWidthPolitics(self.ui.tw_mapdata)

        # señales
        self.ui.btn_sidebar_toggle.clicked.connect(self.toggleSidebar)
        self.ui.le_searchbar.returnPressed.connect(lambda: self.handleFillTableWidget(self.ui.le_searchbar.text()) )
        self.ui.lw_breakthroughs.itemPressed.connect(lambda item: self.handleFillTableWidget(item.text()) )


    
    def toggleSidebar(self) -> None:
        '''Abre/cierra la sidebar. 
        \nRetorna None.'''
        start_val:int
        end_val:int
        show_list:int
        anim:QPropertyAnimation

        # TODO: corregir, cuando pongo items en la lista no se puede cerrar el sidebar.

        start_val = self.ui.sidebar.width()
        end_val = 250 if start_val < 250 else 40
        show_list = 1 if end_val == 250 else 0

        # funciones de animación
        anim = QPropertyAnimation(self.ui.sidebar, b"maximumWidth", self.ui.body)
        anim.setDuration(190)
        anim.setStartValue(start_val)
        anim.setEndValue(end_val)
        anim.setEasingCurve(QEasingCurve.Type.InOutCubic)
        anim.start()

        # muestra/esconde la lista de breakthroughs
        self.ui.lw_breakthroughs.show() if show_list else self.ui.lw_breakthroughs.hide()
        self.ui.lw_breakthroughs.setEnabled(False if self.ui.lw_breakthroughs.isHidden() else True)
        return None



    def handleFillTableWidget(self, search_text:str) -> None:
        '''Maneja funciones para leer el archivo ".csv", filtrar por términos y llenar la tabla "tw_mapdata".
        \nRetorna None.'''
        
        if search_text.strip(): # si el texto no está vacío...
            # convierte el texto a una regex
            print(search_text)
            search_text = searchTextToRegex(search_text)
            print(search_text)

            # lee el archivo y filtra los registros
            self.dataframe = pd.read_csv("MapData_Breakthroughs.csv")

            # TODO: filtrar usando map en el dataframe las Series que tengan los términos de search_text
            # self.dataframe.map(self.dataframe.)
            
            # llena la tabla

        return None