from PySide6.QtWidgets import (QTableWidget, QHeaderView)
import pandas



def setTableWidthPolitics(tableWidget:QTableWidget) -> None:
    '''Recibe un 'QTableWidget' y especifica las políticas de ancho de las columnas. 
    \nRetorna None.'''
    header:QHeaderView = tableWidget.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeToContents)
    header.setSectionResizeMode(3, QHeaderView.Stretch)
    header.setMinimumSectionSize(130)
    return None


def filterMaps(df:pandas.DataFrame, search_terms:str) -> pandas.DataFrame:
    '''Recibe un 'pandas.DataFrame' sin filtrar junto con los criterios de búsqueda y lo filtra. 
    \nRetorna un 'pandas.DataFrame' filtrado, o None si no hubo coincidencias.'''
    filtered_res:pandas.DataFrame | None
    row_indexes:list = []

    # el for recorre todas las filas, iterrows() devuelve el índice y la Serie...
    for row_idx, serie in df.loc[:, "Coordenadas":"Innovación 12"].iterrows():

        # en cada Serie verifica que TODAS los 'search_terms' estén en las columnas (no importa en cuáles, pero entre todas)...
        if all(word.lower() in ' '.join(map(str, serie)).lower() for word in search_terms):
            # si están todas las palabras, guarda el índice de la Serie
            row_indexes.append(row_idx)
    
    # si se encontraron resultados, crea un DataFrame con los índices encontrados...
        filtered_res = df.loc[row_indexes] if row_indexes else None

    return filtered_res