def generar_combinaciones(posiciones_restantes, combinacion_actual, todas_combinaciones):
    if not posiciones_restantes:
        todas_combinaciones.append(tuple(combinacion_actual))
        return

    # Recursivamente generar combinaciones para cada posición
    for valor in posiciones_restantes[0]:
        generar_combinaciones(posiciones_restantes[1:], combinacion_actual + [valor], todas_combinaciones)


combinaciones = []
generar_combinaciones([[0, -1], [1, -1], [2, -1]], [], combinaciones)
print(combinaciones)