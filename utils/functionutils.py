from PySide6.QtWidgets import (QTableWidget, QHeaderView, QWidget, QGraphicsEffect, 
                               QGraphicsDropShadowEffect, QProgressBar)
from PySide6.QtCore import (QSize, QPropertyAnimation, QEasingCurve, QObject)
from PySide6.QtGui import (QPixmap, QPaintEvent)

from resources import (rc_images)


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
    effect.setBlurRadius(7)
    effect.setColor(113238254) # rgb(113, 238, 254) - electric blue
    widget.setGraphicsEffect(effect)

    return None

