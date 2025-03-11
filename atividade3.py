import os 

os.system ("cls")

niv_do_professor = int(input("Digite o nível do professor: "))


aulas_por_semana = int(input("Digite a quantidade de aulas: "))


if niv_do_professor == 1:
    valor_por_hora = 12.00
elif niv_do_professor == 2:
    valor_por_hora = 17.00
elif niv_do_professor == 3:
    valor_por_hora = 25.00


salario = (valor_por_hora * aulas_por_semana) *4


print("O salário final do professor é: R$", salario)
