import sys
from PySide6.QtWidgets import QApplication
import pandas as pd
from pandas import DataFrame
from utils.classes import MainWindow



# MAIN ========================================================================================================================
def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())
        


if __name__ == '__main__':
    main()