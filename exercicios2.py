salario = float(input("Qual o salario Base:"))
porc = float(input("Qual a porcentagem de Aumento:"))

aumento = salario * (porc / 100)
NovoSalario = salario + aumento 

print(f"o Aumento so seu salario foi de R$:{aumento}\nO novo salario é de R$:{NovoSalario:.2f} ")