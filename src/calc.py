# Para converter um número binário para o número decimal equivalente basta multiplicar cada dígito pela potência de 2 
# relativa à posição por ele ocupada e somar os resultados. 
# Assim por exemplo o número binário 101 equivale ao número 5 no sistema decimal. 
import numpy as np


def to_decimal(bin_array: tuple) -> int:
    calc_array = np.array([])
    aux = 0

    for index, x in enumerate(bin_array):
        calc_array = np.append(calc_array, x * 2 ** index)
        aux = aux + 1
    
    decimal_number = sum(calc_array)

    return decimal_number