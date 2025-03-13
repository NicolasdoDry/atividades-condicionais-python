import os 
os.system ("cls")

numero = int(input("Digite um número para calcular a tabuada: "))

for i in range(11):
    print(numero, "x", i, "=", numero * i)
