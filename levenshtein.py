def levenshtein_distance(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1

    # Inicializar una matriz para almacenar los resultados de los subproblemas
    matrix = [[0] * len_str2 for _ in range(len_str1)]

    # Inicializar la primera fila y columna de la matriz
    for i in range(len_str1):
        matrix[i][0] = i
    for j in range(len_str2):
        matrix[0][j] = j

    # Llenar la matriz utilizando programación dinámica
    for i in range(1, len_str1):
        for j in range(1, len_str2):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,         # Eliminación
                matrix[i][j - 1] + 1,         # Inserción
                matrix[i - 1][j - 1] + cost   # Sustitución
            )
        print(matrix[i])

    # El último elemento de la matriz contiene la distancia de Levenshtein
    return matrix[len_str1 - 1][len_str2 - 1]

# Ejemplo de uso
cadena1 = "kitten"
cadena2 = "sitting"
distancia = levenshtein_distance(cadena1, cadena2)
print(f"La distancia de Levenshtein entre '{cadena1}' y '{cadena2}' es: {distancia}")
