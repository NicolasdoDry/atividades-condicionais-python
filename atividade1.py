import os 

os.system ("cls")

num1 = int(input("Digite um numero: ")) 
num2 = int(input("Digite outro numero: "))
operação = input("Escolha a operação que você deseja: ")

if(operação == "+"):
 resultado = num1 + num2
print("Resultado: ", resultado)

if(operação == "-"):
 resultado = num1 - num2
print("Resultado: ", resultado)


if(operação == "*"):
 resultado = num1 * num2
print("Resultado: ", resultado)

if(operação == "/"): 
 resultado = num1 / num2
print("Resultado: ", resultado)
