"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    try:
        with open("files/input/data.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
    except FileNotFoundError:
        with open("../files/input/data.csv", "r", encoding="utf-8") as file:
            data = file.readlines()

    agrupacion = {}

    for line in data:
        line = line.strip()
        columns = line.split('\t')
        letra = columns[0]
        valor = int(columns[1]) 
        if letra in agrupacion:
            agrupacion[letra].append(valor)
        else:
            agrupacion[letra] = [valor]

    resultado = []
    
    for letra in sorted(agrupacion.keys()):
        valores = agrupacion[letra]
        maximo = max(valores)
        minimo = min(valores)        
        resultado.append((letra, maximo, minimo))

    return resultado