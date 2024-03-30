# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_coordinatesdatawidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_CoordinatesDataWidget(object):
    def setupUi(self, CoordinatesDataWidget):
        if not CoordinatesDataWidget.objectName():
            CoordinatesDataWidget.setObjectName(u"CoordinatesDataWidget")
        CoordinatesDataWidget.resize(468, 80)
        CoordinatesDataWidget.setMaximumSize(QSize(16777215, 80))
        CoordinatesDataWidget.setWindowTitle(u"")
        CoordinatesDataWidget.setStyleSheet(u"#label_coords,\n"
"#label_topography,\n"
"#label_altitude {\n"
"	color: #F5E002;\n"
"}\n"
"\n"
"\n"
"#label_coords {\n"
"	font-size: 21px;\n"
"}\n"
"\n"
"\n"
"#label_topography,\n"
"#label_altitude {\n"
"	font-size: 19px;\n"
"	letter-spacing: 0px;\n"
"}")
        self.gridLayout = QGridLayout(CoordinatesDataWidget)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.label_coords = QLabel(CoordinatesDataWidget)
        self.label_coords.setObjectName(u"label_coords")
        self.label_coords.setMaximumSize(QSize(16777215, 25))
#if QT_CONFIG(tooltip)
        self.label_coords.setToolTip(u"<html><head/><body><p><span style=\" font-size:14pt;\">La coordenada del mapa teniendo en cuenta latitud(N/S) y longitud(W/E).</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.label_coords.setTextFormat(Qt.PlainText)
        self.label_coords.setWordWrap(True)
        self.label_coords.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.label_coords, 0, 0, 1, 1)

        self.label_altitude = QLabel(CoordinatesDataWidget)
        self.label_altitude.setObjectName(u"label_altitude")
        self.label_altitude.setMaximumSize(QSize(16777215, 25))
#if QT_CONFIG(tooltip)
        self.label_altitude.setToolTip(u"<html><head/><body><p><span style=\" font-size:14pt;\">La altitud del mapa.</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.label_altitude.setText(u"")
        self.label_altitude.setTextFormat(Qt.PlainText)
        self.label_altitude.setScaledContents(False)
        self.label_altitude.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_altitude.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.label_altitude, 0, 1, 1, 1)

        self.label_topography = QLabel(CoordinatesDataWidget)
        self.label_topography.setObjectName(u"label_topography")
        self.label_topography.setMaximumSize(QSize(16777215, 50))
#if QT_CONFIG(tooltip)
        self.label_topography.setToolTip(u"<html><head/><body><p><span style=\" font-size:14pt;\">La topograf\u00eda del mapa.</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.label_topography.setTextFormat(Qt.PlainText)
        self.label_topography.setAlignment(Qt.AlignCenter)
        self.label_topography.setWordWrap(True)
        self.label_topography.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.label_topography, 1, 0, 1, 2)


        self.retranslateUi(CoordinatesDataWidget)

        QMetaObject.connectSlotsByName(CoordinatesDataWidget)
    # setupUi

    def retranslateUi(self, CoordinatesDataWidget):
        self.label_coords.setText("")
        self.label_topography.setText("")
        pass
    # retranslateUi

