from ui.mainwindow import Ui_MainWindow
from PySide6.QtWidgets import (QMainWindow)
from PySide6.QtCore import (QPropertyAnimation, QEasingCurve)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # señales
        self.ui.btn_sidebar_toggle.clicked.connect(self.toggleSidebar)

    
    def toggleSidebar(self) -> None:
        '''Abre/cierra la sidebar. Retorna None.'''
        start_val:int
        end_val:int
        show_list:int
        anim:QPropertyAnimation

        start_val = self.ui.sidebar.width()
        end_val = 188 if start_val < 188 else 40
        show_list = 1 if end_val == 188 else 0
        anim = QPropertyAnimation(self.ui.sidebar, b"maximumWidth", self.ui.body)
        anim.setDuration(190)
        anim.setStartValue(start_val)
        anim.setEndValue(end_val)
        anim.setEasingCurve(QEasingCurve.Type.InOutCubic)
        anim.start()

        self.ui.lw_breakthroughs.show() if show_list else self.ui.lw_breakthroughs.hide()
        return None