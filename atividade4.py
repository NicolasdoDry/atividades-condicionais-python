import os 

os.system("cls")


peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)


print("O seu IMC é:", (imc, 2))


if imc < 16.9:
    print("A situação é: Muito abaixo do peso")
elif 16 <= imc <= 18.4:
    print("A situação é: Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("A situação é: Peso normal")
elif 25 <= imc <= 29.9:
    print("A situação é: Sobrepeso")
elif 30 <= imc <= 34.9:
    print("A situação é: Obesidade grau 1")
elif 35 <= imc <= 39.9:
    print("A situação é: Obesidade grau 2 ")
else:
    print("A situação é: Obesidade grau 3 ")


