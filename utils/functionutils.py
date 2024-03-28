from PySide6.QtWidgets import (QTableWidget, QHeaderView, QWidget, QGraphicsEffect, 
                               QGraphicsDropShadowEffect, QProgressBar, QListWidget)
from PySide6.QtCore import (QSize, QPropertyAnimation, QEasingCurve, QObject)
from PySide6.QtGui import (QPixmap, QPaintEvent)

from resources import (rc_images)

from re import (match, split as resplit, Match, IGNORECASE)


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


def getFilterPandasQuery(search_terms:list[str]|str) -> str:
    '''Recibe los términos a buscar en un pandas.DataFrame y crea la expresión para la función pandas.query().
    \nRetorna la expresión lista para usarse en pandas.query() en formato str.'''
    expression:str = ""
    int_res:Match|None # regex de una columna con algún número
    str_res:Match|None # regex de una columna con algún string
    term_exp:str # expresión sólo de un término (puede hacerse muy larga 'expression' sino)
    split_term:list[str] = None # sólo se usa si se accede a una columna. Guarda el nombre de la col., el operador y el valor.
    list_exp:list[str] = [] # lista que guarda todas las term_exp

    # columnas agrupadas por tipo de datos
    STR_COLS:tuple[str] = (
        "Coordenadas",
        "Topografia",
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
    )
    INT_COLS:tuple[str] = (
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
        "Olas_de_frio"
    )

    # verifica que search_terms sea una list. Si lo es, tiene que hacer una búsqueda compleja...
    if isinstance(search_terms, list):

        # recorre cada término y lo convierte a una expresión equivalente para pandas.query()...
        for term in search_terms:

            # verifica si se busca en una columna específica (y de paso, si el valor es int)
            int_res = match("[\w ]*(==|!=|<|<=|>|>=){1}[ ]*[0-9]{1}", term, IGNORECASE) # admite todos los operadores de comparación
            int_res = int_res.group() if int_res else None

            # verifica si se busca en una columna específica (y de paso, si el valor es string)
            str_res = match("[\w ]*(==|!=){1}[ ]*[A-Za-z ]+", term, IGNORECASE) # sólo admite igualdad o desigualdad
            str_res = str_res.group() if str_res else None

            # * verifica si el valor luego de ==|!=|<|<=|>|>= es str, int, o si no se accede a una columna.
            # * hago esto para no tener que buscar en todas las columnas, porque al saber el tipo de dato 
            # * que puede tener el valor de la columna puedo saber en qué columnas fijarme (si está bien 
            # * planteada la búsqueda, por supuesto)
            if str_res: # si se busca en una columna y el valor es str...
                split_term = resplit("(==|!=)", term)
                term_exp = f"( {''.join( [ split_term[0].strip().replace(' ','_').capitalize(), split_term[1] ] )}'{split_term[2].strip()}' )"

            elif int_res: # si se busca en una columna y el valor es int...
                split_term = resplit("(==|!=|<|<=|>|>=)", term)
                term_exp = f"( {''.join( [ split_term[0].strip().replace(' ','_').capitalize(), split_term[1], split_term[2].strip() ] )} )"

            elif not str_res and not int_res: # si no se accede a ninguna columna específica, busca en todas...
                if term.isnumeric(): # si es un número busca en las columnas con números...
                    term_exp = f".str.contains('{term.capitalize()}', case=False) | ".join(INT_COLS)
                elif term.isalpha(): # si es alfabético busca en las columnas alfabéticas...
                    term_exp = f".str.contains('{term.capitalize()}', case=False) | ".join(STR_COLS)
                    
                term_exp = f"( {term_exp}.str.contains('{term}', case=False) )"

            list_exp.append(term_exp)
            expression = ' & '.join(list_exp)
    
    else: # si search_terms ES UN STR, es porque se seleccionó desde lw_breakthroughs
        expression = search_terms
        expression = f".str.contains('{search_terms}', case=False) | ".join(STR_COLS[2:])
        expression = f"( {expression}.str.contains('{search_terms}', case=False) )"

    return expression