"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    try:
        with open("files/input/data.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
    except FileNotFoundError:
        with open("../files/input/data.csv", "r", encoding="utf-8") as file:
            data = file.readlines()

    suma_letras = {}

    for line in data:
        line = line.strip()
        columns = line.split('\t')
        
        valor = int(columns[1])
        

        letras = columns[3].split(',')
        
        for letra in letras:
            if letra in suma_letras:
                suma_letras[letra] += valor
            else:
                suma_letras[letra] = valor

    return dict(sorted(suma_letras.items()))