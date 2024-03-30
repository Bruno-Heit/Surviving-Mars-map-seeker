# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_difficultydatawidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_DifficultyDataWidget(object):
    def setupUi(self, DifficultyDataWidget):
        if not DifficultyDataWidget.objectName():
            DifficultyDataWidget.setObjectName(u"DifficultyDataWidget")
        DifficultyDataWidget.resize(749, 94)
        DifficultyDataWidget.setMinimumSize(QSize(0, 0))
        DifficultyDataWidget.setMaximumSize(QSize(16777215, 16777215))
        DifficultyDataWidget.setStyleSheet(u"#label_challengedifficulty,\n"
"#label_temperature,\n"
"#label_met_text,\n"
"#label_cw_text,\n"
"#label_dd_text,\n"
"#label_ds_text {\n"
"	color: #F5E002;\n"
"}\n"
"\n"
"\n"
"#label_challengedifficulty {\n"
"	font-size: 21px;\n"
"}\n"
"\n"
"\n"
"#label_temperature {\n"
"	font-size: 19px;\n"
"	letter-spacing: 0px;\n"
"}")
        self.gridLayout = QGridLayout(DifficultyDataWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.label_temperature = QLabel(DifficultyDataWidget)
        self.label_temperature.setObjectName(u"label_temperature")
        self.label_temperature.setMinimumSize(QSize(120, 0))
#if QT_CONFIG(tooltip)
        self.label_temperature.setToolTip(u"<html><head/><body><p><span style=\" font-size:14pt;\">La temperatura media del mapa representada en grados Celsius.</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.label_temperature.setText(u"")
        self.label_temperature.setTextFormat(Qt.PlainText)
        self.label_temperature.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_temperature.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.label_temperature, 2, 0, 1, 1)

        self.label_challengedifficulty = QLabel(DifficultyDataWidget)
        self.label_challengedifficulty.setObjectName(u"label_challengedifficulty")
        self.label_challengedifficulty.setMinimumSize(QSize(120, 0))
#if QT_CONFIG(tooltip)
        self.label_challengedifficulty.setToolTip(u"<html><head/><body><p><span style=\" font-size:14pt;\">El nivel de dificultad general del mapa. </span></p><p><span style=\" font-size:14pt;\">Este valor representa la dificultad del mapa sin tener en cuenta modificadores de dificultad, como lo son las reglas del mapa por ejemplo.</span></p><p><span style=\" font-size:14pt;\">Cuanto mayor sea el valor m\u00e1s dif\u00edcil ser\u00e1 la dificultad en el mapa.</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.label_challengedifficulty.setText(u"")
        self.label_challengedifficulty.setTextFormat(Qt.PlainText)
        self.label_challengedifficulty.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.label_challengedifficulty, 0, 0, 2, 1)

        self.frame_dustdevils = QFrame(DifficultyDataWidget)
        self.frame_dustdevils.setObjectName(u"frame_dustdevils")
        self.frame_dustdevils.setMinimumSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.frame_dustdevils.setToolTip(u"<html><head/><body><p><span style=\" font-size:14pt;\">Frecuencia de aparici\u00f3n de remolinos de polvo.</span></p><p><span style=\" font-size:14pt;\">El nivel var\u00eda de 1 a 4, siendo 1 una baja frecuencia de remolinos de polvo y 4 una alta frecuencia.</span></p><p><span style=\" font-size:14pt;\">Los remolinos de polvo ensucian todas las construcciones en el exterior que tocan, y cada transporte cercano reduce su velocidad en un 60%.</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.frame_dustdevils.setFrameShape(QFrame.NoFrame)
        self.frame_dustdevils.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_dustdevils)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 5, 0)
        self.label_dd_icon = QLabel(self.frame_dustdevils)
        self.label_dd_icon.setObjectName(u"label_dd_icon")
        self.label_dd_icon.setMinimumSize(QSize(110, 27))
        self.label_dd_icon.setMaximumSize(QSize(166, 41))
        self.label_dd_icon.setText(u"")
        self.label_dd_icon.setTextFormat(Qt.PlainText)
        self.label_dd_icon.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.label_dd_icon)

        self.label_dd_text = QLabel(self.frame_dustdevils)
        self.label_dd_text.setObjectName(u"label_dd_text")
        self.label_dd_text.setMinimumSize(QSize(55, 0))
        self.label_dd_text.setMaximumSize(QSize(16777215, 16777215))
        self.label_dd_text.setText(u"Remolinos de polvo")
        self.label_dd_text.setTextFormat(Qt.PlainText)
        self.label_dd_text.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.label_dd_text)


        self.gridLayout.addWidget(self.frame_dustdevils, 0, 1, 2, 1)

        self.frame_duststorms = QFrame(DifficultyDataWidget)
        self.frame_duststorms.setObjectName(u"frame_duststorms")
        self.frame_duststorms.setMinimumSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.frame_duststorms.setToolTip(u"<html><head/><body><p><span style=\" font-size:14pt;\">Frecuencia de las tormentas de polvo.</span></p><p><span style=\" font-size:14pt;\">El nivel var\u00eda de 1 a 4, siendo 1 una baja frecuencia de tormentas de polvo y 4 una alta frecuencia.</span></p><p><span style=\" font-size:14pt;\">Durante las tormentas de polvo los edificios en el exterior se ensuciar\u00e1n constantemente a un ritmo mayor y algunos dejar\u00e1n de funcionar (por ejemplo, los evaporadores de agua), los cohetes no podr\u00e1n despegar ni aterrizar y las lanzaderas no despegar\u00e1n, las tuber\u00edas podr\u00edan da\u00f1arse, las turbinas e\u00f3licas producir\u00e1n m\u00e1s energ\u00eda.</span></p><p><span style=\" font-size:14pt;\">Adem\u00e1s se pueden producir tormentas de polvo electrost\u00e1ticas, que son tormentas de polvo cargadas de electricidad. Estas tormentas pueden apagar edificios que sean alcanzados por los rayos, drenar la bater\u00eda de los drones, destruir el combustible almacenado en el exterior, reduce la energ"
                        "\u00eda almacenada en acumuladores de energ\u00eda e incluso matar colonos si son alcanzados por rayos.</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.frame_duststorms.setFrameShape(QFrame.NoFrame)
        self.frame_duststorms.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_duststorms)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 5, 0)
        self.label_ds_icon = QLabel(self.frame_duststorms)
        self.label_ds_icon.setObjectName(u"label_ds_icon")
        self.label_ds_icon.setMinimumSize(QSize(110, 27))
        self.label_ds_icon.setMaximumSize(QSize(166, 41))
        self.label_ds_icon.setText(u"")
        self.label_ds_icon.setTextFormat(Qt.PlainText)
        self.label_ds_icon.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.label_ds_icon)

        self.label_ds_text = QLabel(self.frame_duststorms)
        self.label_ds_text.setObjectName(u"label_ds_text")
        self.label_ds_text.setText(u"Tormentas de polvo")
        self.label_ds_text.setTextFormat(Qt.PlainText)
        self.label_ds_text.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label_ds_text)


        self.gridLayout.addWidget(self.frame_duststorms, 2, 1, 1, 1)

        self.frame_meteors = QFrame(DifficultyDataWidget)
        self.frame_meteors.setObjectName(u"frame_meteors")
        self.frame_meteors.setMinimumSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.frame_meteors.setToolTip(u"<html><head/><body><p><span style=\" font-size:14pt;\">Frecuencia con la que los meteoritos suelen caer en el mapa.</span></p><p><span style=\" font-size:14pt;\">El nivel var\u00eda de 1 a 4, siendo 1 una baja frecuencia de meteoritos y 4 una alta frecuencia.</span></p><p><span style=\" font-size:14pt;\">Los impactos de meteoritos crean nubes de polvo alrededor que ensucian los edificios exteriores cercanos, los domos alcanzados por meteoritos sufren fracturas en el casco, los edificios exteriores alcanzados directamente son destru\u00eddos, los dep\u00f3sitos de combustible alcanzados son destru\u00eddos y se pueden provocar explosiones por el combustible que destruir\u00e1 veh\u00edculos y edificios cercanos, y en las zonas de impacto pueden aparecer anomal\u00edas, metales o pol\u00edmeros.</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.frame_meteors.setFrameShape(QFrame.NoFrame)
        self.frame_meteors.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_meteors)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_met_icon = QLabel(self.frame_meteors)
        self.label_met_icon.setObjectName(u"label_met_icon")
        self.label_met_icon.setMinimumSize(QSize(110, 27))
        self.label_met_icon.setMaximumSize(QSize(166, 41))
        self.label_met_icon.setText(u"")
        self.label_met_icon.setTextFormat(Qt.PlainText)
        self.label_met_icon.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_4.addWidget(self.label_met_icon)

        self.label_met_text = QLabel(self.frame_meteors)
        self.label_met_text.setObjectName(u"label_met_text")
        self.label_met_text.setText(u"Meteoritos")
        self.label_met_text.setTextFormat(Qt.PlainText)
        self.label_met_text.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.label_met_text)


        self.gridLayout.addWidget(self.frame_meteors, 0, 2, 2, 1)

        self.frame_coldwaves = QFrame(DifficultyDataWidget)
        self.frame_coldwaves.setObjectName(u"frame_coldwaves")
        self.frame_coldwaves.setMinimumSize(QSize(0, 0))
#if QT_CONFIG(tooltip)
        self.frame_coldwaves.setToolTip(u"<html><head/><body><p><span style=\" font-size:14pt;\">Frecuencia de olas de fr\u00edo que suele haber en el mapa.</span></p><p><span style=\" font-size:14pt;\">El nivel var\u00eda de 1 a 4, siendo 1 una baja frecuencia de olas de fr\u00edo y 4 una alta frecuencia.</span></p><p><span style=\" font-size:14pt;\">Durante las olas de fr\u00edo los edificios exteriores y los domos requieren 3 veces m\u00e1s energ\u00eda, los drones usan un 40% m\u00e1s energ\u00eda, los dep\u00f3sitos de agua se congelan, los edificios exteriores que no tienen energ\u00eda el\u00e9ctrica o no se usan se congelan lentamente, los edificios congelados se rompen y s\u00f3lo se les puede dar mantenimiento cuando se descongelen.</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.frame_coldwaves.setFrameShape(QFrame.NoFrame)
        self.frame_coldwaves.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_coldwaves)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_cw_icon = QLabel(self.frame_coldwaves)
        self.label_cw_icon.setObjectName(u"label_cw_icon")
        self.label_cw_icon.setMinimumSize(QSize(110, 27))
        self.label_cw_icon.setMaximumSize(QSize(166, 41))
        self.label_cw_icon.setText(u"")
        self.label_cw_icon.setTextFormat(Qt.PlainText)
        self.label_cw_icon.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_3.addWidget(self.label_cw_icon)

        self.label_cw_text = QLabel(self.frame_coldwaves)
        self.label_cw_text.setObjectName(u"label_cw_text")
        self.label_cw_text.setText(u"Olas de fr\u00edo")
        self.label_cw_text.setTextFormat(Qt.PlainText)
        self.label_cw_text.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.label_cw_text)


        self.gridLayout.addWidget(self.frame_coldwaves, 2, 2, 1, 1)


        self.retranslateUi(DifficultyDataWidget)

        QMetaObject.connectSlotsByName(DifficultyDataWidget)
    # setupUi

    def retranslateUi(self, DifficultyDataWidget):
        DifficultyDataWidget.setWindowTitle("")
    # retranslateUi

