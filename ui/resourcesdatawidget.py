# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_resourcesdatawidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_ResourcesDataWidget(object):
    def setupUi(self, ResourcesDataWidget):
        if not ResourcesDataWidget.objectName():
            ResourcesDataWidget.setObjectName(u"ResourcesDataWidget")
        ResourcesDataWidget.resize(460, 80)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ResourcesDataWidget.sizePolicy().hasHeightForWidth())
        ResourcesDataWidget.setSizePolicy(sizePolicy)
        ResourcesDataWidget.setMinimumSize(QSize(184, 40))
        ResourcesDataWidget.setMaximumSize(QSize(16777215, 80))
        ResourcesDataWidget.setWindowTitle(u"")
#if QT_CONFIG(tooltip)
        ResourcesDataWidget.setToolTip(u"<html><head/><body><p><span style=\" font-size:12pt;\">Niveles de recursos que hay inicialmente en el mapa.</span></p><p><span style=\" font-size:12pt;\">Los niveles var\u00edan entre 1 y 4, siendo 1 escasez de un recurso y 4 su abundancia.</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        ResourcesDataWidget.setStyleSheet(u"#label_metals_level,\n"
"#label_rare_metals_level,\n"
"#label_concrete_level {\n"
"	margin-right: 5px;\n"
"}\n"
"\n"
"#label_metals_level,\n"
"#label_rare_metals_level,\n"
"#label_concrete_level,\n"
"#label_water_level {\n"
"	color: #F5E002;\n"
"}")
        self.horizontalLayout = QHBoxLayout(ResourcesDataWidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.label_metals_icon = QLabel(ResourcesDataWidget)
        self.label_metals_icon.setObjectName(u"label_metals_icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_metals_icon.sizePolicy().hasHeightForWidth())
        self.label_metals_icon.setSizePolicy(sizePolicy1)
        self.label_metals_icon.setMinimumSize(QSize(40, 40))
#if QT_CONFIG(tooltip)
        self.label_metals_icon.setToolTip(u"<html><head/><body><p><span style=\" font-size:12pt;\">Metales comunes disponibles inicialmente en el mapa</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.label_metals_icon.setText(u"")
        self.label_metals_icon.setTextFormat(Qt.PlainText)
        self.label_metals_icon.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.label_metals_icon)

        self.label_metals_level = QLabel(ResourcesDataWidget)
        self.label_metals_level.setObjectName(u"label_metals_level")
#if QT_CONFIG(tooltip)
        self.label_metals_level.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_metals_level.setText(u"")
        self.label_metals_level.setTextFormat(Qt.PlainText)
        self.label_metals_level.setWordWrap(False)
        self.label_metals_level.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.label_metals_level)

        self.label_rare_metals_icon = QLabel(ResourcesDataWidget)
        self.label_rare_metals_icon.setObjectName(u"label_rare_metals_icon")
        sizePolicy1.setHeightForWidth(self.label_rare_metals_icon.sizePolicy().hasHeightForWidth())
        self.label_rare_metals_icon.setSizePolicy(sizePolicy1)
        self.label_rare_metals_icon.setMinimumSize(QSize(40, 40))
#if QT_CONFIG(tooltip)
        self.label_rare_metals_icon.setToolTip(u"<html><head/><body><p><span style=\" font-size:12pt;\">Metales raros disponibles inicialmente en el mapa</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.label_rare_metals_icon.setText(u"")
        self.label_rare_metals_icon.setTextFormat(Qt.PlainText)
        self.label_rare_metals_icon.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.label_rare_metals_icon)

        self.label_rare_metals_level = QLabel(ResourcesDataWidget)
        self.label_rare_metals_level.setObjectName(u"label_rare_metals_level")
#if QT_CONFIG(tooltip)
        self.label_rare_metals_level.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_rare_metals_level.setText(u"")
        self.label_rare_metals_level.setTextFormat(Qt.PlainText)
        self.label_rare_metals_level.setWordWrap(False)
        self.label_rare_metals_level.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.label_rare_metals_level)

        self.label_concrete_icon = QLabel(ResourcesDataWidget)
        self.label_concrete_icon.setObjectName(u"label_concrete_icon")
        sizePolicy1.setHeightForWidth(self.label_concrete_icon.sizePolicy().hasHeightForWidth())
        self.label_concrete_icon.setSizePolicy(sizePolicy1)
        self.label_concrete_icon.setMinimumSize(QSize(40, 40))
#if QT_CONFIG(tooltip)
        self.label_concrete_icon.setToolTip(u"<html><head/><body><p><span style=\" font-size:12pt;\">Concreto disponible inicialmente en el mapa</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.label_concrete_icon.setText(u"")
        self.label_concrete_icon.setTextFormat(Qt.PlainText)
        self.label_concrete_icon.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.label_concrete_icon)

        self.label_concrete_level = QLabel(ResourcesDataWidget)
        self.label_concrete_level.setObjectName(u"label_concrete_level")
#if QT_CONFIG(tooltip)
        self.label_concrete_level.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_concrete_level.setText(u"")
        self.label_concrete_level.setTextFormat(Qt.PlainText)
        self.label_concrete_level.setWordWrap(False)
        self.label_concrete_level.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.label_concrete_level)

        self.label_water_icon = QLabel(ResourcesDataWidget)
        self.label_water_icon.setObjectName(u"label_water_icon")
        sizePolicy1.setHeightForWidth(self.label_water_icon.sizePolicy().hasHeightForWidth())
        self.label_water_icon.setSizePolicy(sizePolicy1)
        self.label_water_icon.setMinimumSize(QSize(40, 40))
#if QT_CONFIG(tooltip)
        self.label_water_icon.setToolTip(u"<html><head/><body><p><span style=\" font-size:12pt;\">Agua disponible inicialmente en el mapa</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.label_water_icon.setText(u"")
        self.label_water_icon.setTextFormat(Qt.PlainText)
        self.label_water_icon.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.label_water_icon)

        self.label_water_level = QLabel(ResourcesDataWidget)
        self.label_water_level.setObjectName(u"label_water_level")
#if QT_CONFIG(tooltip)
        self.label_water_level.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_water_level.setText(u"")
        self.label_water_level.setTextFormat(Qt.PlainText)
        self.label_water_level.setScaledContents(False)
        self.label_water_level.setWordWrap(False)
        self.label_water_level.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.label_water_level)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 2)
        self.horizontalLayout.setStretch(6, 1)
        self.horizontalLayout.setStretch(7, 2)

        self.retranslateUi(ResourcesDataWidget)

        QMetaObject.connectSlotsByName(ResourcesDataWidget)
    # setupUi

    def retranslateUi(self, ResourcesDataWidget):
        pass
    # retranslateUi

