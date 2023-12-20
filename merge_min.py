def merge_sort_select_min(arr):
    if len(arr) <= 1:
        return arr

    # Divide la lista en mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Llamada recursiva para ordenar y seleccionar el mínimo en las mitades
    left_half = merge_sort_select_min(left_half)
    right_half = merge_sort_select_min(right_half)

    # Fusionar las mitades ordenadas
    result = merge(left_half, right_half)

    return result

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # Comparar elementos y seleccionar el menor
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Agregar los elementos restantes, si los hay
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Ejemplo de uso
lista_original = [5, 2, 9, 1, 5, 6]
minimo = merge_sort_select_min(lista_original)
print(minimo)
print("El elemento mínimo es:", minimo[0])
