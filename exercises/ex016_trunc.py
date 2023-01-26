# Crie um programa que leia um número Real qualquer  
# pelo teclado e mostre  na tela a sua  porção inteira
from math import trunc
n = float(input("Enter a numbe: "))
print("The entered value was {} and its integer portion is {}".format(n, trunc(n)))
# print("The entered value was {} and its integer portion is {:.0f}".format(n, n))
