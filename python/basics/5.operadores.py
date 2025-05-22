"""
    Cri um programa que peca ao usuario que informe  2 numeros.
    Calcule a adicao,subtraccao,multiplicacao e divisao entre 2 
    numeros. Imprima os resultados encontrados no final.
"""

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

print(f"Adicao: {num1 + num2}")
print(f"Subtracao: {num1 - num2}")
print(f"Divisao: {num1 / num2}")
print(f"Resto: {num1 % num2 : .2f}")
print(f"Multiplicacao: {num1 * num2}")