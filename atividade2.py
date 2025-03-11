import os

os.system ("cls")


nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: "))


total_sem_desconto = quantidade * preco_unitario
print("Total a pagar (sem desconto): R$", total_sem_desconto)


if quantidade <= 5:
    desconto = total_sem_desconto * 0.02  
elif 6 <= quantidade <= 10:
    desconto = total_sem_desconto * 0.03  
else:
    desconto = total_sem_desconto * 0.05  


total_com_desconto = total_sem_desconto - desconto


print("Desconto aplicado: R$", desconto)
print("Total a pagar (com desconto): R$", total_com_desconto)





