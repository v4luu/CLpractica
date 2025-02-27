def es_primo(num):
    # Los números menores o iguales a 1 no son primos
    if num <= 1:
        return False
    # Verificamos si hay algún divisor entre 2 y la raíz cuadrada del número
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True