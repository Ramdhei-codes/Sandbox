def distribucion_vacia(canales: list):
    existentes = 0
    for element in canales:
        if element == -1:
            existentes += 1
    res = {}
    res['0'] = [1/(2**existentes) for i in range(2**existentes)]
    return res

print(distribucion_vacia([-1,-1,-1]))