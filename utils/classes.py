from ui.mainwindow import Ui_MainWindow
from ui.coordinatesdatawidget import Ui_CoordinatesDataWidget
from ui.resourcesdatawidget import Ui_ResourcesDataWidget
from ui.difficultydatawidget import Ui_DifficultyDataWidget
from ui.showbreakthroughswidget import Ui_ShowBreakthroughsWidget
from ui.breakthroughslistwidget import Ui_BreakthroughsListWidget

from resources import (rc_icons, rc_images)

from PySide6.QtWidgets import (QMainWindow, QWidget, QFrame)
from PySide6.QtGui import (QIcon, QPixmap, QRegularExpressionValidator)
from PySide6.QtCore import (QPropertyAnimation, QEasingCurve, QSize, QThread, QObject, Signal, 
                            Slot, Qt, QPoint)

from utils.functionutils import *

import pandas



class MainWindow(QMainWindow):
    begin_filtering:Signal = Signal(pandas.DataFrame, str)
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lw_breakthroughs.hide()
        self.ui.pb_searchingdata.hide()

        # coloco un QValidator a le_searchbar
        validator = QRegularExpressionValidator("[\w ,=!<>]*", self.ui.le_searchbar)
        self.ui.le_searchbar.setValidator(validator)

        # coloca el ícono en btn_sidebar_toggle
        icon = QIcon()
        icon.addFile(":/icons/menu.svg", QSize(24, 24))
        self.ui.btn_sidebar_toggle.setIcon(icon)
        # coloca el ícono en btn_show_search_info
        icon2 = QIcon()
        icon2.addFile(":/icons/show-info.ico", QSize(30, 30))
        self.ui.btn_show_search_info.setIcon(icon2)

        # añado efecto box-shadow fluorescente a los widgets
        addGlowToBorder(self.ui.btn_sidebar_toggle)
        addGlowToBorder(self.ui.le_searchbar)
        addGlowToBorder(self.ui.btn_show_more)
        addGlowToBorder(self.ui.pb_searchingdata)

        # ventana flotante para mostrarse en tw_mapdata cuando se haga click en algún botón de columna de innovaciones
        self.br_floating_window:QWidget = BreakthroughsListWidget()

        # dataframe con innovaciones
        pandas_usecols:list[str] = [
            "Coordenadas",
            "Topografia",
            "Dificultad_del_desafio",
            "Altitud",
            "Temperatura",
            "Metales",
            "Metales_raros",
            "Concreto",
            "Agua",
            "Remolinos_de_polvo",
            "Tormentas_de_polvo",
            "Meteoritos",
            "Olas_de_frio",
            "Innovacion_1",
            "Innovacion_2",
            "Innovacion_3",
            "Innovacion_4",
            "Innovacion_5",
            "Innovacion_6",
            "Innovacion_7",
            "Innovacion_8",
            "Innovacion_9",
            "Innovacion_10",
            "Innovacion_11",
            "Innovacion_12"
            ]
        pandas_dtype:dict[str:str] = {
            "Coordenadas":"string",
            "Topografía":"string",
            "Dificultad_del_desafío":"uint16",
            "Altitud":"int16",
            "Temperatura":"int16",
            "Metales":"uint8",
            "Metales_raros":"uint8",
            "Concreto":"uint8",
            "Agua":"uint8",
            "Remolinos_de_polvo":"uint8",
            "Tormentas_de_polvo":"uint8",
            "Meteoritos":"uint8",
            "Olas_de_frío":"uint8",
            "Innovacion_1":"string",
            "Innovacion_2":"string",
            "Innovacion_3":"string",
            "Innovacion_4":"string",
            "Innovacion_5":"string",
            "Innovacion_6":"string",
            "Innovacion_7":"string",
            "Innovacion_8":"string",
            "Innovacion_9":"string",
            "Innovacion_10":"string",
            "Innovacion_11":"string",
            "Innovacion_12":"string"
        }
        self.dataframe:pandas.DataFrame = pandas.read_csv("MapData_Breakthroughs.csv", header=0, usecols=pandas_usecols, dtype=pandas_dtype)
        
        # lista de términos de búsqueda
        self.search_terms:str = None
        # lista de índices coincidentes
        self.filtered_indexes:list[int] = []
        # último índice coincidente (para btn_show_more)
        self.last_index:int = None

        # determina las políticas del ancho de las columnas de la tabla
        setTableWidthPolitics(self.ui.tw_mapdata)

        # Thread y worker para QThread
        self.filter_worker = FilterMapsWorker()
        self.filter_thread = QThread()

        self.filter_worker.moveToThread(self.filter_thread)

        # ############ señales ############################################################
        self.ui.btn_sidebar_toggle.clicked.connect(self.toggleSidebar)
        self.ui.le_searchbar.returnPressed.connect(lambda: self.handleFillTableWidget(self.ui.le_searchbar.text()) )
        self.ui.lw_breakthroughs.itemPressed.connect(lambda item: self.handleFillTableWidget(item.text(), True) )
        self.ui.btn_show_more.clicked.connect(self.showMoreMaps)
        self.ui.btn_show_search_info.clicked.connect(self.showInfoWidget)

        # señal de filter_worker
        self.filter_worker.progress.connect(lambda index: self.filteringProgressMade(index))
        self.filter_worker.completed.connect(self.filteringMapsFinished)
        self.begin_filtering.connect(self.filter_worker.filterMapsByTerms)

        # inicio el thread (sino no funciona)
        self.filter_thread.start()


    def toggleSidebar(self) -> None:
        '''Abre/cierra la sidebar.
        \nRetorna None.'''
        start_val:int
        end_val:int
        show_list:int
        anim:QPropertyAnimation
        icon:QIcon

        start_val = self.ui.sidebar.width()
        end_val = 250 if start_val < 250 else 40
        show_list = 1 if end_val == 250 else 0

        # funciones de animación
        anim = QPropertyAnimation(self.ui.sidebar, b"minimumWidth", self.ui.body)
        anim.setDuration(150)
        anim.setStartValue(start_val)
        anim.setEndValue(end_val)
        anim.setEasingCurve(QEasingCurve.Type.InOutCubic)
        anim.start()

        # muestra/esconde la lista de breakthroughs
        self.ui.lw_breakthroughs.show() if show_list else self.ui.lw_breakthroughs.hide()
        self.ui.lw_breakthroughs.setEnabled(False if self.ui.lw_breakthroughs.isHidden() else True)

        return None


    def handleFillTableWidget(self, search_text:str, list_selected:bool=False) -> None:
        '''Maneja funciones para leer el archivo ".csv", filtrar por términos y llenar la tabla "tw_mapdata".
        \nSi 'list_selected' es True es porque se selecciona una innovación desde 'lw_breakthroughs', si False \
        se seleccionó desde 'le_searchbar'.
        \nRetorna None.'''
        search_terms:list[str]|str
        expression:str # contiene la expresión de búsqueda que usa pandas.query()

        if search_text.strip() != "": # si el texto no está vacío...
            if not list_selected: # si no se selecciona desde lw_breakthroughs...
                search_text = search_text.rstrip(",") if search_text.endswith(",") else search_text
                
                # convierte el texto a palabras clave
                search_terms = search_text.split(",")
                search_terms = [term.strip() for term in search_terms]
            
            else: # si se seleccionó usando lw_breakthroughs...
                search_terms = search_text

            expression = getFilterPandasQuery(search_terms)

            self.begin_filtering.emit(self.dataframe, expression)

        return None


    def filteringProgressMade(self, index:int) -> None:
        '''Si se logra algún progreso mientras se filtran los criterios de búsqueda, se recibe el índice del \
        mapa encontrado y se lo guarda en la lista 'self.filtered_indexes', pero si el largo de la lista llega \
        a 25 se reinicia la lista.
        \nAdemás anima los cambios entre 'chunks' de la barra de progreso 'pb_searchingdata'.
        \nRetorna None.'''
        self.filtered_indexes.clear() if len(self.filtered_indexes) == 25 else None
        self.filtered_indexes.append(index)

        # si pb_searchingdata está escondido es porque recién comienza a buscar FilterMapsWorker
        if self.ui.pb_searchingdata.isHidden():
            self.ui.pb_searchingdata.show()
            self.ui.pb_searchingdata.setEnabled(True)
            self.ui.pb_searchingdata.reset()

        self.ui.pb_searchingdata.setValue(len(self.filtered_indexes))
        return None


    def filteringMapsFinished(self) -> None:
        '''Una vez que se terminan de filtrar los criterios de búsqueda filtra el DataFrame existente con 
        esos criterios.
        
        Determina la cantidad de filas de la tabla, crea los widgets necesarios para cada columna y asigna los 
        datos. Adicionalmente esconde la barra de progreso 'pb_searchingdata'.
        
        Retorna None.'''
        coords_data_widget:CoordinatesDataWidget # widget que muestra las coordenadas y topografía del mapa
        resources_data_widget:ResourcesDataWidget # widget que muestra datos de los recursos del mapa
        difficulty_data_widget:DifficultyDataWidget # widget que muestra datos sobre la dificultad del mapa
        show_br_widget:WidgetShowBreakthroughs # botón que sirve para mostrar todas las innovaciones del mapa

        # limpia la tabla
        self.ui.tw_mapdata.setRowCount(0) # no hace falta más nada para limpiar la tabla...

        # reinicia el value de pb_searchingdata y lo esconde
        self.ui.pb_searchingdata.reset()
        self.ui.pb_searchingdata.hide()

        # guarda el último índice (para btn_show_more)
        self.last_index = self.filtered_indexes[-1] if self.filtered_indexes else 50901

        # especifica la cantidad de filas inicial de la tabla (muestra 25)
        self.ui.tw_mapdata.setRowCount(len(self.filtered_indexes))

        for row in range(self.ui.tw_mapdata.rowCount()):
            # columna 0: coordenadas/topografía
            coords_data_widget = CoordinatesDataWidget(coords=self.dataframe.at[self.filtered_indexes[row], "Coordenadas"],
                                                       topography=self.dataframe.at[self.filtered_indexes[row], "Topografia"],
                                                       altitude=str(self.dataframe.at[self.filtered_indexes[row], "Altitud"]))
            self.ui.tw_mapdata.setCellWidget(row, 0, coords_data_widget)
            # columna 1: recursos
            resources_data_widget = ResourcesDataWidget(metals_level=self.dataframe.at[self.filtered_indexes[row], "Metales"],
                                                        rare_metals_level=self.dataframe.at[self.filtered_indexes[row], "Metales_raros"],
                                                        concrete_level=self.dataframe.at[self.filtered_indexes[row], "Concreto"],
                                                        water_level=self.dataframe.at[self.filtered_indexes[row], "Agua"])
            self.ui.tw_mapdata.setCellWidget(row, 1, resources_data_widget)
            self.ui.tw_mapdata.setColumnWidth(1, 184)

            # columna 2: dificultad
            difficulty_data_widget = DifficultyDataWidget(self.dataframe.at[self.filtered_indexes[row], "Dificultad_del_desafio"],
                                                          self.dataframe.at[self.filtered_indexes[row], "Temperatura"],
                                                          self.dataframe.at[self.filtered_indexes[row], "Remolinos_de_polvo"],
                                                          self.dataframe.at[self.filtered_indexes[row], "Tormentas_de_polvo"],
                                                          self.dataframe.at[self.filtered_indexes[row], "Meteoritos"],
                                                          self.dataframe.at[self.filtered_indexes[row], "Olas_de_frio"])
            self.ui.tw_mapdata.setCellWidget(row, 2, difficulty_data_widget)

            # columna 3: innovaciones
            show_br_widget = WidgetShowBreakthroughs(
                coords=self.dataframe.at[self.filtered_indexes[row], "Coordenadas"], 
                index=self.filtered_indexes[row])
            # conecto la señal del botón
            show_br_widget.is_clicked.connect(lambda index: showBreakthroughList(
                widget=self.br_floating_window, 
                table_width=self.ui.tw_mapdata.viewport().width(),
                table_height=self.ui.tw_mapdata.viewport().height(),
                breakthroughs=self.dataframe.loc[index, "Innovacion_1":"Innovacion_12"].to_list() ))
            
            self.ui.tw_mapdata.setCellWidget(row, 3, show_br_widget)

        self.ui.tw_mapdata.resizeRowsToContents()

        # por último, si el último índice coincidente es menor a 50901 (el último), activa btn_show_more
        self.ui.btn_show_more.setEnabled(True if self.filtered_indexes[-1] < 50901 else False)

        return None


    def showMoreMaps(self) -> None:
        '''Añade otros 25 mapas a la tabla 'tw_mapdata'.
        \nPara hacerlo, toma el índice del último mapa mostrado en la tabla y busca en el archivo ".csv"\
        los 25 siguientes índices coincidentes guardados en 'self.filtered_indexes'.
        \nRetorna None.'''
        # TODO: buscar cómo llamar a FilterMapsWorker para que busque más mapas
        pass


    def showInfoWidget(self) -> None:
        pass





class FilterMapsWorker(QObject):
    '''Clase que maneja la función y las señales que sirven para filtrar mapas en un thread/hilo aparte usando un worker. 
    Filtra de a 25 mapas.'''
    # si se encontraron resultados envía un dataframe filtrado, sino envía None
    progress:Signal = Signal(int)
    completed:Signal = Signal(None)
    

    @Slot(pandas.DataFrame)
    def filterMapsByTerms(self, df:pandas.DataFrame, search_expression:str, from_index:int=0, to_index:int=50901, 
                          from_col:str="Coordenadas", to_col:str="Innovacion_12") -> None:
        '''En un thread paralelo filtra el pandas.DataFrame a partir de los términos de búsqueda introducidos.

        - df: el pandas.DataFrame que hay que filtrar.
        - search_expression: string listo para usar en pandas.query().
        - from_index (opcional): valor entero que representa la fila desde la cual buscar.
        - to_index (opcional): valor entero que representa la fila hasta donde buscar.
        - from_col (opcional): string que representa la columna desde la cual buscar.
        - to_col (opcional): string que representa la columna hasta donde buscar.

        A medida que encuentra pandas.Series coincidentes emite el índice a MainWindow.filteringProgressMade().
        
        Retorna None.
        '''
        filtered_df:pandas.DataFrame

        filtered_df = df.loc[from_index:to_index, from_col:to_col]
        filtered_df = filtered_df.query(search_expression).head(25)

        for index in filtered_df.index:
            self.progress.emit(index)

        self.completed.emit()
        return None





class CoordinatesDataWidget(QWidget):
    '''Clase simple que muestra las coordenadas del mapa y la topografía.'''
    def __init__(self, coords:str, topography:str, altitude:str):
        super(CoordinatesDataWidget, self).__init__()
        self.coord_ui = Ui_CoordinatesDataWidget()
        self.coord_ui.setupUi(self)

        self.coord_ui.label_coords.setText(coords)
        self.coord_ui.label_topography.setText(topography)
        self.coord_ui.label_altitude.setText(altitude)





class ResourcesDataWidget(QWidget):
    '''Clase simple que muestra los 4 recursos disponibles en el mapa al comienzo.'''
    def __init__(self, metals_level:int, rare_metals_level:int, concrete_level:int, water_level:int):
        super(ResourcesDataWidget, self).__init__()
        self.resrc_ui = Ui_ResourcesDataWidget()
        self.resrc_ui.setupUi(self)

        # coloca los íconos de cada recurso
        metals_icon = QPixmap(":/icons/metals.ico")
        self.resrc_ui.label_metals_icon.setPixmap(metals_icon)
        rare_metals_icon = QPixmap(":/icons/rare_metals.ico")
        self.resrc_ui.label_rare_metals_icon.setPixmap(rare_metals_icon)
        concrete_icon = QPixmap(":/icons/concrete.ico")
        self.resrc_ui.label_concrete_icon.setPixmap(concrete_icon)
        water_icon = QPixmap(":/icons/water.ico")
        self.resrc_ui.label_water_icon.setPixmap(water_icon)

        # coloca los valores de los recursos del mapa en los labels
        self.resrc_ui.label_metals_level.setText(f"{metals_level}")
        self.resrc_ui.label_rare_metals_level.setText(f"{rare_metals_level}")
        self.resrc_ui.label_concrete_level.setText(f"{concrete_level}")
        self.resrc_ui.label_water_level.setText(f"{water_level}")




class DifficultyDataWidget(QWidget):
    '''Clase simple que muestra el nivel de dificultad, la temperatura y los niveles
    de desastres del mapa.'''
    def __init__(self, challenge_difficulty:int, temperature:int, dust_devils_lvl:int, dust_storms_lvl:int, 
                 meteors_lvl:int, cold_waves_lvl:int):
        super(DifficultyDataWidget, self).__init__()
        self.diff_ui = Ui_DifficultyDataWidget()
        self.diff_ui.setupUi(self)

        self.diff_ui.label_challengedifficulty.setText(f"DIF. DEL DESAFÍO: {challenge_difficulty}")

        self.diff_ui.label_temperature.setText(f"{temperature}°C")

        # íconos
        match dust_devils_lvl:
            case 1:
                dd_pixmap = QPixmap(":/icons/threat-level1.png")
            case 2:
                dd_pixmap = QPixmap(":/icons/threat-level2.png")
            case 3:
                dd_pixmap = QPixmap(":/icons/threat-level3.png")
            case 4:
                dd_pixmap = QPixmap(":/icons/threat-level4.png")
            case _:
                pass
        self.diff_ui.label_dd_icon.setPixmap(dd_pixmap)

        match dust_storms_lvl:
            case 1:
                ds_pixmap = QPixmap(":/icons/threat-level1.png")
            case 2:
                ds_pixmap = QPixmap(":/icons/threat-level2.png")
            case 3:
                ds_pixmap = QPixmap(":/icons/threat-level3.png")
            case 4:
                ds_pixmap = QPixmap(":/icons/threat-level4.png")
            case _:
                pass
        self.diff_ui.label_ds_icon.setPixmap(ds_pixmap)

        match meteors_lvl:
            case 1:
                met_pixmap = QPixmap(":/icons/threat-level1.png")
            case 2:
                met_pixmap = QPixmap(":/icons/threat-level2.png")
            case 3:
                met_pixmap = QPixmap(":/icons/threat-level3.png")
            case 4:
                met_pixmap = QPixmap(":/icons/threat-level4.png")
            case _:
                pass
        self.diff_ui.label_met_icon.setPixmap(met_pixmap)
        
        match cold_waves_lvl:
            case 1:
                cw_pixmap = QPixmap(":/icons/threat-level1.png")
            case 2:
                cw_pixmap = QPixmap(":/icons/threat-level2.png")
            case 3:
                cw_pixmap = QPixmap(":/icons/threat-level3.png")
            case 4:
                cw_pixmap = QPixmap(":/icons/threat-level4.png")
            case _:
                pass
        self.diff_ui.label_cw_icon.setPixmap(cw_pixmap)





class WidgetShowBreakthroughs(QWidget):
    is_clicked:Signal = Signal(int) # cuando se hace click en el botón se envía a MainWindow el índice del mapa

    def __init__(self, coords:str, index:int): # index es el índice en el DataFrame (0 a 50901)
        super(WidgetShowBreakthroughs, self).__init__()
        self.showbr_ui = Ui_ShowBreakthroughsWidget()
        self.showbr_ui.setupUi(self)
        self.setObjectName(f"widget_show_{index}")

        icon = QIcon()
        icon.addFile(":/icons/technology.ico", QSize(42, 42))
        self.showbr_ui.btn_show.setIcon(icon)

        self.showbr_ui.btn_show.setText(f"Ver innovaciones de {coords}")

        self.showbr_ui.btn_show.clicked.connect(lambda: self.is_clicked.emit(index))





class CustomLisWidget(QListWidget):
    '''ListWidget con el 'paintEvent' modificado. Es usado en BreakthroughsListWidget.'''
    def __init__(self):
        super(CustomLisWidget, self).__init__()
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setEditTriggers(QListWidget.EditTrigger.NoEditTriggers)
        self.setWrapping(False)
        self.setWordWrap(True)

        self.setStyleSheet("background-image: url(:/images/bg-hexagons.png); background-repeat: repeat;")





class BreakthroughsListWidget(QWidget):
    '''QWidget con un QListWidget con una lista de todas las innovaciones que tiene el mapa actual.'''
    def __init__(self):
        super(BreakthroughsListWidget, self).__init__()
        self.brlist_ui = Ui_BreakthroughsListWidget()
        self.brlist_ui.setupUi(self)

        self.setParent(None)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint | Qt.WindowType.Popup)
        self.setFixedSize(220, 380)
        self.setWindowOpacity(0.88)

        # instancio CustomListWidget
        self.list_widget = CustomLisWidget()
        self.brlist_ui.horizontalLayout.addWidget(self.list_widget)
