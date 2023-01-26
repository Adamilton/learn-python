# 10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e
# mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
# sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

width = float(input("Enter wall width: "))
height = float(input("Enter wall height: "))

print("The area of {:.2f} square meters needs {:.2f} liters of paint".format( width*height,  width*height/2))

