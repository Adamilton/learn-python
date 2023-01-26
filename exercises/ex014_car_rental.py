# 14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
# um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input("How many days rented?: "))
k = float(input("How many km driven?: "))

print("The total amount to be paid is R${:.2f}".format(d*60+k*0.15))
