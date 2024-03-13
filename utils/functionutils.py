from PySide6.QtWidgets import (QTableWidget, QHeaderView)



def setTableWidthPolitics(tableWidget:QTableWidget) -> None:
    '''Recibe un 'QTableWidget' y especifica las políticas de ancho de las columnas. 
    \nRetorna None.'''
    header:QHeaderView = tableWidget.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeToContents)
    header.setSectionResizeMode(3, QHeaderView.Stretch)
    header.setMinimumSectionSize(130)
    return None



def searchTextToRegex(search_text:str) -> str:
    '''Convierte el texto introducido en una expresión regular. 
    \nRetorna un str con la regex.'''
    terms:list[str]
    search_regex:str = ".*("

    # separa los términos de búsqueda en los espacios en blanco
    terms = search_text.split()

    # convierte los términos a regex
    for term in terms:
        search_regex += f"{term.strip()}|"

    search_regex = search_regex.rstrip("|") + ").*"
    return search_regex

