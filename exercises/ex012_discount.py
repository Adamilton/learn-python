# 12) Crie um programa que leia o preço de um produto, calcule 
# e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.

n = float(input("How much money do you have in your wallet? "))
print("The value R${:.2f} with discount is R${:.2f}".format(n, n*0.95))
