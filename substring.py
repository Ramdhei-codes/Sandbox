import numpy as np
def marginalizar_fila(diccionario, indice):
    nuevo_diccionario = {}

    for clave, valores in diccionario.items():
        nueva_clave = clave[:indice] + clave[indice + 1:]
        if nueva_clave in nuevo_diccionario:
            nuevo_diccionario[nueva_clave] = [sum(x)/2 for x in zip(nuevo_diccionario[nueva_clave], valores)]
        else:
            nuevo_diccionario[nueva_clave] = valores

    return nuevo_diccionario

def marginalizar_columna(diccionario, indice):
    nuevo_diccionario = {}

    for clave, valores in diccionario.items():
        nueva_clave = clave[:indice] + clave[indice + 1:]
        if nueva_clave in nuevo_diccionario:
            nuevo_diccionario[nueva_clave] = [sum(x) for x in zip(nuevo_diccionario[nueva_clave], valores)]
        else:
            nuevo_diccionario[nueva_clave] = valores

    return nuevo_diccionario




def trasponerMatrizDict(diccionario: dict, keys: list) -> dict:
    matriz = np.array(list(diccionario.values()))
    matrizTranspuesta = np.transpose(matriz)
    return {key: matrizTranspuesta[i].tolist() for i, key in enumerate(diccionario)}

def trasponerMatrizDictKeys(diccionario: dict, keys: list) -> dict:
    matriz = np.array(list(diccionario.values()))
    matrizTranspuesta = np.transpose(matriz)
    return {key: matrizTranspuesta[i].tolist() for i, key in enumerate(keys)}
    

# Ejemplo de uso
diccionario_original = {
    '000': [0.0, 0.0, 0.0, 0.0, 0.25, 0.25, 0.0, 0.5],
    '100': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0],
    '010': [0.0, 0.0, 0.0, 0.0, 0.25, 0.5, 0.0, 0.25],
    '110': [0.0, 0.0, 0.0, 0.0, 0.0, 0.3333333333333333, 0.6666666666666666, 0.0],
    '001': [0.0, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.0, 0.0, 0.0, 0.0],
    '101': [0.0, 0.2, 0.4, 0.0, 0.0, 0.0, 0.2, 0.2],
    '011': [0.25, 0.0, 0.0, 0.25, 0.0, 0.25, 0.0, 0.25],
    '111': [0.4, 0.0, 0.2, 0.2, 0.2, 0.0, 0.0, 0.0]
}

indice_a_quitar = 0  # Cambia este valor según el índice que desees quitar

nuevo_diccionario = marginalizar_fila(diccionario_original, indice_a_quitar)

columnas = trasponerMatrizDictKeys(diccionario_original, diccionario_original.keys())
# print(columnas)
nuevo_col = marginalizar_columna(columnas, indice_a_quitar)
print(trasponerMatrizDictKeys(nuevo_col, list(diccionario_original.keys())))
