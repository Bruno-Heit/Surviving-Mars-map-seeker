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
    QHBoxLayout, QHeaderView, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(757, 550)
        MainWindow.setMinimumSize(QSize(600, 550))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"* {\n"
"	font-family: \"VertigoFLF\", \"Tw Cen MT\", \"Arial\";\n"
"	font-weight: bold;\n"
"	font-size: 23px;\n"
"	color: rgba(51, 9, 0, 1);\n"
"}\n"
"\n"
"\n"
"#centralwidget {\n"
"	background-color: qradialgradient(spread:pad, cx:0, cy:0, radius:1.034, fx:0.16, fy:0.152, stop:0 rgba(23, 20, 27, 255), stop:1 rgba(175, 79, 52, 255));\n"
"}\n"
"\n"
"\n"
"QLineEdit,\n"
"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(8, 58, 117, 180), stop:0.450282 rgba(61, 156, 210, 160), stop:1 rgba(67, 239, 224, 140));\n"
"	color: #F5E002;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	border: 1px solid;\n"
"	border-color: rgb(61, 146, 210);\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton:pressed {\n"
"	border-top: 1px inset;\n"
"	border-left: 1px inset;\n"
"	border-color: rgb(67, 239, 224);\n"
"}\n"
"QPushButton:!enabled {\n"
"	border-color: #444;\n"
"	background-color: rgba(254, 242, 216, 1);\n"
"	color: #888;\n"
"}\n"
"\n"
"\n"
"QTableWidget,\n"
"QListWidget,\n"
"QHeaderView:"
                        ":section {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.749, fx:0.5, fy:0.5, stop:0 rgba(113, 238, 254, 140), stop:1 rgba(8, 58, 117, 160));\n"
"}\n"
"QHeaderView::section {\n"
"	border: none;\n"
"	border-right: 1px solid;\n"
"	border-left: 1px solid;\n"
"	border-color: rgba(113, 238, 254, 1);\n"
"}\n"
"\n"
"\n"
"QListWidget {\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"\n"
"QTableWidget {\n"
"	background-image: url(\"C:/Users/Bruno/Desktop/PROGRAMACION/Proyectos/Surviving Mars map seeker/images/bkgnd_honeycomb_ptrn.png\")\n"
"}\n"
"\n"
"\n"
"/* scrollbars */\n"
"QScrollBar {\n"
"	background-color: transparent;\n"
"	border: 1px solid rgba(113, 238, 254, 1);\n"
"	border-radius: 5px;\n"
"}\n"
"QScrollBar:groove {\n"
"	border-radius: 5px;\n"
"}\n"
"QScrollBar::handle {\n"
"	background-color: rgba(245, 224, 2, 1);\n"
"	border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:pressed {\n"
"	background-color: rgba(255, 244, 22, 1);\n"
"}\n"
"QScrollBar::sub-line {\n"
"	width: 0;\n"
"	height: 0;\n"
"	"
                        "background: none;\n"
"}\n"
"QScrollBar::add-line {\n"
"	width: 0;\n"
"	height: 0;\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"/*vertical scrollbars*/\n"
"QScrollBar:vertical {\n"
"	width: 13px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	min-height: 15px;\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"/*horizontal scrollbars*/\n"
"QScrollBar:horizontal {\n"
"	height: 13px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	min-width: 15px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QSize(40, 0))
        self.sidebar.setMaximumSize(QSize(40, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.btn_sidebar_toggle = QPushButton(self.sidebar)
        self.btn_sidebar_toggle.setObjectName(u"btn_sidebar_toggle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_sidebar_toggle.sizePolicy().hasHeightForWidth())
        self.btn_sidebar_toggle.setSizePolicy(sizePolicy1)
        self.btn_sidebar_toggle.setMinimumSize(QSize(35, 25))
        self.btn_sidebar_toggle.setMaximumSize(QSize(35, 25))
        self.btn_sidebar_toggle.setText(u"")
        self.btn_sidebar_toggle.setIconSize(QSize(24, 24))
#if QT_CONFIG(shortcut)
        self.btn_sidebar_toggle.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.btn_sidebar_toggle.setAutoRepeatInterval(200)

        self.verticalLayout_2.addWidget(self.btn_sidebar_toggle, 0, Qt.AlignRight|Qt.AlignTop)

        self.lw_breakthroughs = QListWidget(self.sidebar)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        QListWidgetItem(self.lw_breakthroughs)
        self.lw_breakthroughs.setObjectName(u"lw_breakthroughs")
        self.lw_breakthroughs.setEnabled(False)
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
        self.lw_breakthroughs.setAlternatingRowColors(False)
        self.lw_breakthroughs.setTextElideMode(Qt.ElideNone)
        self.lw_breakthroughs.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lw_breakthroughs.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.lw_breakthroughs.setProperty("isWrapping", False)
        self.lw_breakthroughs.setResizeMode(QListView.Adjust)
        self.lw_breakthroughs.setSpacing(3)
        self.lw_breakthroughs.setUniformItemSizes(True)
        self.lw_breakthroughs.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.lw_breakthroughs)


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

        self.tw_mapdata = QTableWidget(self.body)
        if (self.tw_mapdata.columnCount() < 4):
            self.tw_mapdata.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_mapdata.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_mapdata.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_mapdata.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_mapdata.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tw_mapdata.setObjectName(u"tw_mapdata")
        self.tw_mapdata.setStyleSheet(u"#tw_mapdata::item:selected {\n"
"	background-color: rgb(255, 211, 165);\n"
"	border: 1px solid;\n"
"	border-color: rgb(188, 96, 71);\n"
"}")
        self.tw_mapdata.setFrameShape(QFrame.NoFrame)
        self.tw_mapdata.setFrameShadow(QFrame.Plain)
        self.tw_mapdata.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tw_mapdata.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tw_mapdata.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_mapdata.setProperty("showDropIndicator", False)
        self.tw_mapdata.setDragDropOverwriteMode(False)
        self.tw_mapdata.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tw_mapdata.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tw_mapdata.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tw_mapdata.verticalHeader().setVisible(True)

        self.verticalLayout.addWidget(self.tw_mapdata)

        self.btn_show_more = QPushButton(self.body)
        self.btn_show_more.setObjectName(u"btn_show_more")
        self.btn_show_more.setEnabled(False)

        self.verticalLayout.addWidget(self.btn_show_more)


        self.horizontalLayout.addWidget(self.body)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        __sortingEnabled = self.lw_breakthroughs.isSortingEnabled()
        self.lw_breakthroughs.setSortingEnabled(False)
        ___qlistwidgetitem = self.lw_breakthroughs.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Pilotaje avanzado de drones", None));
        ___qlistwidgetitem1 = self.lw_breakthroughs.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Planos alien\u00edgenas", None));
        ___qlistwidgetitem2 = self.lw_breakthroughs.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"M\u00fasculos artificiales", None));
        ___qlistwidgetitem3 = self.lw_breakthroughs.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Centros de mando aut\u00f3nomos", None));
        ___qlistwidgetitem4 = self.lw_breakthroughs.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Clonaci\u00f3n", None));
        ___qlistwidgetitem5 = self.lw_breakthroughs.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Nanites de construcci\u00f3n", None));
        ___qlistwidgetitem6 = self.lw_breakthroughs.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Metales del n\u00facleo", None));
        ___qlistwidgetitem7 = self.lw_breakthroughs.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Metales raros del n\u00facleo", None));
        ___qlistwidgetitem8 = self.lw_breakthroughs.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Agua del n\u00facleo", None));
        ___qlistwidgetitem9 = self.lw_breakthroughs.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Criptosue\u00f1o", None));
        ___qlistwidgetitem10 = self.lw_breakthroughs.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Optimizaci\u00f3n de c\u00fapulas", None));
        ___qlistwidgetitem11 = self.lw_breakthroughs.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Agricultura seca", None));
        ___qlistwidgetitem12 = self.lw_breakthroughs.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Fusi\u00f3n eterna", None));
        ___qlistwidgetitem13 = self.lw_breakthroughs.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Extractor IA", None));
        ___qlistwidgetitem14 = self.lw_breakthroughs.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Automatizaci\u00f3n de f\u00e1bricas", None));
        ___qlistwidgetitem15 = self.lw_breakthroughs.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Siempre joven", None));
        ___qlistwidgetitem16 = self.lw_breakthroughs.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Compuestos sin fricci\u00f3n", None));
        ___qlistwidgetitem17 = self.lw_breakthroughs.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Arquitectura de gema", None));
        ___qlistwidgetitem18 = self.lw_breakthroughs.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Selecci\u00f3n de genes", None));
        ___qlistwidgetitem19 = self.lw_breakthroughs.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Cultivos gigantes", None));
        ___qlistwidgetitem20 = self.lw_breakthroughs.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Buenas vibraciones", None));
        ___qlistwidgetitem21 = self.lw_breakthroughs.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Mente colmena", None));
        ___qlistwidgetitem22 = self.lw_breakthroughs.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Polarizaci\u00f3n del casco", None));
        ___qlistwidgetitem23 = self.lw_breakthroughs.item(23)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Fotovoltaicos hipersensibles", None));
        ___qlistwidgetitem24 = self.lw_breakthroughs.item(24)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Arquitectura inspiradora", None));
        ___qlistwidgetitem25 = self.lw_breakthroughs.item(25)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Aprendizaje interplanetario", None));
        ___qlistwidgetitem26 = self.lw_breakthroughs.item(26)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Extracci\u00f3n magn\u00e9tica", None));
        ___qlistwidgetitem27 = self.lw_breakthroughs.item(27)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Dieta marciana", None));
        ___qlistwidgetitem28 = self.lw_breakthroughs.item(28)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Acero marciano", None));
        ___qlistwidgetitem29 = self.lw_breakthroughs.item(29)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Ingenuidad marciana", None));
        ___qlistwidgetitem30 = self.lw_breakthroughs.item(30)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Arquitectura multiespiral", None));
        ___qlistwidgetitem31 = self.lw_breakthroughs.item(31)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Nanorefinamiento", None));
        ___qlistwidgetitem32 = self.lw_breakthroughs.item(32)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Neo-concreto", None));
        ___qlistwidgetitem33 = self.lw_breakthroughs.item(33)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Empat\u00eda neural", None));
        ___qlistwidgetitem34 = self.lw_breakthroughs.item(34)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Adaptaci\u00f3n nocturna", None));
        ___qlistwidgetitem35 = self.lw_breakthroughs.item(35)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Amplificaciones de sobrecarga", None));
        ___qlistwidgetitem36 = self.lw_breakthroughs.item(36)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Cohetes de plasma", None));
        ___qlistwidgetitem37 = self.lw_breakthroughs.item(37)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("MainWindow", u"S\u00edntesis de plutonio", None));
        ___qlistwidgetitem38 = self.lw_breakthroughs.item(38)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Compresi\u00f3n de prefabricados", None));
        ___qlistwidgetitem39 = self.lw_breakthroughs.item(39)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Impresi\u00f3n de electr\u00f3nica", None));
        ___qlistwidgetitem40 = self.lw_breakthroughs.item(40)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Proyecto F\u00e9nix", None));
        ___qlistwidgetitem41 = self.lw_breakthroughs.item(41)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Sue\u00f1o r\u00e1pido", None));
        ___qlistwidgetitem42 = self.lw_breakthroughs.item(42)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Modo seguro", None));
        ___qlistwidgetitem43 = self.lw_breakthroughs.item(43)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Bots de servicio", None));
        ___qlistwidgetitem44 = self.lw_breakthroughs.item(44)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Soylent Green", None));
        ___qlistwidgetitem45 = self.lw_breakthroughs.item(45)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Rehabilitaci\u00f3n espacial", None));
        ___qlistwidgetitem46 = self.lw_breakthroughs.item(46)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Computaci\u00f3n superconductora", None));
        ___qlistwidgetitem47 = self.lw_breakthroughs.item(47)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Superhongos", None));
        ___qlistwidgetitem48 = self.lw_breakthroughs.item(48)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Cables superiores", None));
        ___qlistwidgetitem49 = self.lw_breakthroughs.item(49)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Tuber\u00edas superiores", None));
        ___qlistwidgetitem50 = self.lw_breakthroughs.item(50)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Carga de trabajo sostenida", None));
        ___qlistwidgetitem51 = self.lw_breakthroughs.item(51)
        ___qlistwidgetitem51.setText(QCoreApplication.translate("MainWindow", u"El cerebro positr\u00f3nico", None));
        ___qlistwidgetitem52 = self.lw_breakthroughs.item(52)
        ___qlistwidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Bomba de vector", None));
        ___qlistwidgetitem53 = self.lw_breakthroughs.item(53)
        ___qlistwidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Sociedad vocacional", None));
        ___qlistwidgetitem54 = self.lw_breakthroughs.item(54)
        ___qlistwidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Energ\u00eda inal\u00e1mbrica", None));
        ___qlistwidgetitem55 = self.lw_breakthroughs.item(55)
        ___qlistwidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Computaci\u00f3n de espacio cero", None));
        self.lw_breakthroughs.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem = self.tw_mapdata.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"coords.", None));
        ___qtablewidgetitem1 = self.tw_mapdata.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"recursos", None));
        ___qtablewidgetitem2 = self.tw_mapdata.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"dificultad", None));
        ___qtablewidgetitem3 = self.tw_mapdata.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"innovaciones", None));
        self.btn_show_more.setText(QCoreApplication.translate("MainWindow", u"Mostrar m\u00e1s resultados", None))
    # retranslateUi

