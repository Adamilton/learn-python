# 9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
# e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.
n = float(input("How much money in reais do you have? R$ "))
print("You can buy US$ {:.2f} ".format(n/5.45))
