def generar_secuencia_little_endian(n):
    # Generar lista de números decimales del 0 al 2^n - 1
    numeros_decimales = list(range(2**n))

    # Convertir cada número a binario y darle formato de n bits
    numeros_binarios = [format(num, '0' + str(n) + 'b') for num in numeros_decimales]

    # Invertir cada cadena binaria para seguir la convención Little Endian
    numeros_little_endian = [num[::-1] for num in numeros_binarios]

    return numeros_little_endian

# Ejemplo para n = 3
n = 4
secuencia_little_endian = generar_secuencia_little_endian(n)
print(secuencia_little_endian)
