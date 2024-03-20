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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_CoordinatesDataWidget(object):
    def setupUi(self, CoordinatesDataWidget):
        if not CoordinatesDataWidget.objectName():
            CoordinatesDataWidget.setObjectName(u"CoordinatesDataWidget")
        CoordinatesDataWidget.resize(468, 80)
        CoordinatesDataWidget.setMaximumSize(QSize(16777215, 80))
        CoordinatesDataWidget.setWindowTitle(u"")
        CoordinatesDataWidget.setStyleSheet(u"#label_coords {\n"
"	font-size: 21px;\n"
"}\n"
"\n"
"\n"
"#label_topography {\n"
"	font-size: 19px;\n"
"	letter-spacing: 0px;\n"
"}")
        self.verticalLayout = QVBoxLayout(CoordinatesDataWidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.label_coords = QLabel(CoordinatesDataWidget)
        self.label_coords.setObjectName(u"label_coords")
        self.label_coords.setMaximumSize(QSize(16777215, 25))
        self.label_coords.setTextFormat(Qt.PlainText)
        self.label_coords.setWordWrap(True)
        self.label_coords.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.label_coords)

        self.label_topography = QLabel(CoordinatesDataWidget)
        self.label_topography.setObjectName(u"label_topography")
        self.label_topography.setMaximumSize(QSize(16777215, 50))
        self.label_topography.setTextFormat(Qt.PlainText)
        self.label_topography.setAlignment(Qt.AlignCenter)
        self.label_topography.setWordWrap(True)
        self.label_topography.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.label_topography)


        self.retranslateUi(CoordinatesDataWidget)

        QMetaObject.connectSlotsByName(CoordinatesDataWidget)
    # setupUi

    def retranslateUi(self, CoordinatesDataWidget):
        self.label_coords.setText("")
        self.label_topography.setText("")
        pass
    # retranslateUi

