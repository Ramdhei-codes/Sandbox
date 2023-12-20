import pyphi

import numpy as np


# Obtén las claves ordenadas para asegurarte de que la matriz esté en el orden correcto

# Convierte el diccionario en una matriz NumPy
matriz = np.array([
    [0.0, 0.0, 0.0, 0.0, 0.25, 0.25, 0.0, 0.5],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.25, 0.5, 0.0, 0.25],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.3333333333333333, 0.6666666666666666, 0.0],
    [0.0, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.2, 0.4, 0.0, 0.0, 0.0, 0.2, 0.2],
    [0.25, 0.0, 0.0, 0.25, 0.0, 0.25, 0.0, 0.25],
    [0.4, 0.0, 0.2, 0.2, 0.2, 0.0, 0.0, 0.0]
])
tpm_filas_ordenadas = ['000', '001', '010', '011', '100', '101', '110', '111']

print(matriz)

def calculate_small_phi(network, partition):
    # Calcular el valor de small-phi para una partición dada
    subsystem = network.subsystem(partition)
    mechanism = pyphi.compute.find_mechanism(subsystem)
    if mechanism is not None:
        small_phi = pyphi.compute.small_phi(subsystem, mechanism)
        return small_phi
    else:
        return float('inf')  # Devolver infinito si no se encuentra un mecanismo

def find_min_phi_mip(network):
    mip = pyphi.compute.big_mip(network)
    all_partitions = list(mip.partitions)

    min_phi = float('inf')
    min_phi_partition = None

    for partition in all_partitions:
        small_phi = calculate_small_phi(network, partition)
        if small_phi < min_phi:
            min_phi = small_phi
            min_phi_partition = partition

    return mip.subsystem(min_phi_partition)


network = pyphi.Network(matriz)
min_phi_mip = find_min_phi_mip(network)

# Imprimir la MIP con el menor small-phi
print(matriz)
print("MIP con el menor small-phi:")
print(min_phi_mip)



