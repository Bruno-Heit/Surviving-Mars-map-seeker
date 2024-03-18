from PySide6.QtWidgets import (QTableWidget, QHeaderView)
import pandas
from time import perf_counter


def setTableWidthPolitics(tableWidget:QTableWidget) -> None:
    '''Recibe un 'QTableWidget' y especifica las políticas de ancho de las columnas. 
    \nRetorna None.'''
    header:QHeaderView = tableWidget.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeToContents)
    header.setSectionResizeMode(3, QHeaderView.Stretch)
    header.setMinimumSectionSize(130)
    return None


