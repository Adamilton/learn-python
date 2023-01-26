# 13) Faça um algoritmo que leia o salário de um funcionário, 
# calcule e mostre o seu novo salário, com 15% de aumento.

n = float(input("Enter employee salary: R$ "))
print("An employee who earned R$ {:.2f}, with a 15% increase, now receives R$ {:.2f}".format(n, n*1.15))
