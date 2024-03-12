# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(757, 550)
        MainWindow.setMinimumSize(QSize(600, 550))
        MainWindow.setStyleSheet(u"* {\n"
"	font-family: \"Tw Cen MT\";\n"
"	font-size: 20px;\n"
"}")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.131, x2:1, y2:0.761, stop:0 rgba(175, 79, 52, 255), stop:1 rgba(23, 20, 27, 255));\n"
"}\n"
"\n"
"\n"
"QLineEdit,\n"
"QPushButton {\n"
"	background-color: rgba(244, 191, 145, 1);\n"
"}\n"
"QPushButton {\n"
"	border: none;\n"
"	border-top: 1px outset;\n"
"	border-left: 1px outset;\n"
"	border-color: rgb(126, 57, 39);\n"
"}\n"
"QPushButton:pressed {\n"
"	border-top: 1px inset;\n"
"	border-left: 1px inset;\n"
"	border-color: rgb(126, 57, 39);\n"
"}\n"
"\n"
"\n"
"QTableView {\n"
"	background-color: rgba(244, 191, 145, 0.55);\n"
"}\n"
"\n"
"\n"
"QListWidget {\n"
"	background-color: rgba(244, 191, 145, 0.7);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(40, 0))
        self.gridLayout = QGridLayout(self.sidebar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 5, 0, 5)
        self.horizontalSpacer = QSpacerItem(94, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.btn_sidebar_toggle = QPushButton(self.sidebar)
        self.btn_sidebar_toggle.setObjectName(u"btn_sidebar_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sidebar_toggle.sizePolicy().hasHeightForWidth())
        self.btn_sidebar_toggle.setSizePolicy(sizePolicy)
        self.btn_sidebar_toggle.setMinimumSize(QSize(35, 25))
        self.btn_sidebar_toggle.setMaximumSize(QSize(35, 25))
        self.btn_sidebar_toggle.setText(u"")

        self.gridLayout.addWidget(self.btn_sidebar_toggle, 0, 1, 1, 1, Qt.AlignRight|Qt.AlignTop)

        self.lw_breakthroughs = QListWidget(self.sidebar)
        self.lw_breakthroughs.setObjectName(u"lw_breakthroughs")
#if QT_CONFIG(tooltip)
        self.lw_breakthroughs.setToolTip(u"<html><head/><body><p><span style=\" font-size:12pt;\">Filtrar mapas por las tecnolog\u00edas del campo de innovaciones</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.lw_breakthroughs.setFrameShape(QFrame.NoFrame)
        self.lw_breakthroughs.setFrameShadow(QFrame.Plain)
        self.lw_breakthroughs.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lw_breakthroughs.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.lw_breakthroughs.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.lw_breakthroughs.setTabKeyNavigation(True)
        self.lw_breakthroughs.setProperty("showDropIndicator", False)
        self.lw_breakthroughs.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.lw_breakthroughs.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lw_breakthroughs.setProperty("isWrapping", True)
        self.lw_breakthroughs.setResizeMode(QListView.Adjust)
        self.lw_breakthroughs.setWordWrap(True)

        self.gridLayout.addWidget(self.lw_breakthroughs, 1, 0, 1, 2)


        self.horizontalLayout.addWidget(self.sidebar)

        self.body = QWidget(self.centralwidget)
        self.body.setObjectName(u"body")
        self.verticalLayout = QVBoxLayout(self.body)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.le_searchbar = QLineEdit(self.body)
        self.le_searchbar.setObjectName(u"le_searchbar")
#if QT_CONFIG(tooltip)
        self.le_searchbar.setToolTip(u"<html><head/><body><p><span style=\" font-size:12pt;\">Permite buscar mapas a partir de innovaciones que aparecen en ellos, cantidad de agua, cantidad de minerales, entre otros tantos criterios.</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.le_searchbar.setInputMask(u"")
        self.le_searchbar.setText(u"")
        self.le_searchbar.setFrame(False)
        self.le_searchbar.setPlaceholderText(u"Buscar mapas por sus caracter\u00edsticas")

        self.verticalLayout.addWidget(self.le_searchbar)

        self.tv_mapdata = QTableView(self.body)
        self.tv_mapdata.setObjectName(u"tv_mapdata")
        self.tv_mapdata.setFrameShape(QFrame.NoFrame)
        self.tv_mapdata.setFrameShadow(QFrame.Plain)
        self.tv_mapdata.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tv_mapdata.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tv_mapdata.setProperty("showDropIndicator", False)
        self.tv_mapdata.setDragDropOverwriteMode(False)
        self.tv_mapdata.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tv_mapdata.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tv_mapdata.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tv_mapdata.verticalHeader().setVisible(True)

        self.verticalLayout.addWidget(self.tv_mapdata)


        self.horizontalLayout.addWidget(self.body)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

