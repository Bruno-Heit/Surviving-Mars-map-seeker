from PySide6.QtWidgets import (QTableWidget, QHeaderView, QWidget, QGraphicsEffect, 
                               QGraphicsDropShadowEffect)
from PySide6.QtGui import (QColor, QBrush, QPalette, QPixmap)

import pandas



def setTableWidthPolitics(tableWidget:QTableWidget) -> None:
    '''Recibe un 'QTableWidget' y especifica las políticas de ancho de las columnas. 
    \nRetorna None.'''
    header:QHeaderView = tableWidget.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeToContents)
    header.setSectionResizeMode(3, QHeaderView.Stretch)
    header.setMinimumSectionSize(130)
    return None


def addGlowToBorder(widget:QWidget) -> None:
    '''Recibe un widget cualquiera y le aplica un borde estilo neon azul. 
    \nRetorna None.'''
    effect:QGraphicsEffect = QGraphicsDropShadowEffect(widget)
    effect.setOffset(0, 0)
    effect.setBlurRadius(5)
    effect.setColor(113238254) # rgba(113, 238, 254, 1) - electric blue
    widget.setGraphicsEffect(effect)

    return None


