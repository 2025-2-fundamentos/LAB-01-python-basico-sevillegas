"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    try:
        with open("files/input/data.csv", "r", encoding="utf-8") as file:
            data = file.readlines()
    except FileNotFoundError:
        with open("../files/input/data.csv", "r", encoding="utf-8") as file:
            data = file.readlines()

    valores_por_clave = {}

    for line in data:
        line = line.strip()
        columns = line.split('\t')
        diccionario_codificado = columns[4] 
        
        pares = diccionario_codificado.split(',')
        
        for par in pares:
            clave, valor = par.split(':')
            valor = int(valor) 
            
            if clave in valores_por_clave:
                valores_por_clave[clave].append(valor)
            else:
                valores_por_clave[clave] = [valor]

    resultado = []
    
    for clave in sorted(valores_por_clave.keys()):
        lista_valores = valores_por_clave[clave]
        min_val = min(lista_valores)
        max_val = max(lista_valores)
        
        resultado.append((clave, min_val, max_val))

    return resultado