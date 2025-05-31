"""
    Crie um programa que importe as bibliotecas: os e math.
    e utilize suas respectivas funcoes para demostrar o so
"""
import math
import os

x = 16
raiz = math.sqrt(x)
print(f"raiz quadrada:  {raiz}")

angulo = 45
seno = math.sin(angulo)
print(f"Seno:  {seno: .2f}")

diretorio = os.getcwd() #pemite ver caminho
print(diretorio)

os.system("ls -1") #permite invocar cmandos do terminal


lista = [10, 20, 30]
tamanho = len(lista)
print(tamanho)

soma= sum(lista)
print(f"Soma da lista: {soma}")