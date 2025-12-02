"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    try:
        with open("files/input/data.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
    except FileNotFoundError:
        with open("../files/input/data.csv", "r", encoding="utf-8") as file:
            data = file.readlines()

    conteo = {}

    for line in data:
        line = line.strip()
        columns = line.split('\t')        
        contenido_columna = columns[4]
        
        pares = contenido_columna.split(',')
        for par in pares:
            clave, valor = par.split(':')
            
            if clave in conteo:
                conteo[clave] += 1
            else:
                conteo[clave] = 1

    return dict(sorted(conteo.items()))