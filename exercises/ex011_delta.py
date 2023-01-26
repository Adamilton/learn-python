# 11) Desenvolva uma lógica que leia os valores de A, B e C 
# de uma equação do segundo grau e mostre o valor de Delta.

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

print("The delta of the equation is {:.2f}".format(b**2 -4*a*c))
