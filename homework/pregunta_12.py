"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    try:
        with open("files/input/data.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
    except FileNotFoundError:
        with open("../files/input/data.csv", "r", encoding="utf-8") as file:
            data = file.readlines()

    resultados = {}

    for line in data:
        line = line.strip()
        columns = line.split('\t')
        
        letra = columns[0]
        
        columna5 = columns[4]
        
        suma_linea = 0
        pares = columna5.split(',')
        for par in pares:
            valor = int(par.split(':')[1])
            suma_linea += valor
        
        if letra in resultados:
            resultados[letra] += suma_linea
        else:
            resultados[letra] = suma_linea

    return dict(sorted(resultados.items()))