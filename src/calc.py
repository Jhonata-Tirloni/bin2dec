# Para converter um número binário para o número decimal equivalente basta multiplicar cada dígito pela potência de 2 
# relativa à posição por ele ocupada e somar os resultados. 
# Assim por exemplo o número binário 101 equivale ao número 5 no sistema decimal. 
import numpy as np
from flask import Blueprint, render_template, redirect, url_for, request, flash

def to_decimal(bin_array: tuple) -> int:
    calc_array = np.array([])
    aux = 0

    if to_decimal >= 0 or to_decimal <= 1:
        try:
            for index, x in enumerate(bin_array):
                calc_array = np.append(calc_array, x * 2 ** index)
                aux = aux + 1
            
            decimal_number = sum(calc_array)

            return decimal_number
        
        except Exception as e:

            return e
    else:
            flash("Digito binário invalido!")

            return redirect(url_for('main.index'))

    return
    