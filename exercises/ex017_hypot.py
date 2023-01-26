# faça um programa que leia  o comprimento  do  cateto  oposto 
# e cateto adjacente  de um triangulo  rêtangulo, calcule 
# e mostre  o comprimento  da hipotenusa

from math import hypot
co = float(input("Enter the length of the opposite leg: "))
ca = float(input("Enter length of adjacent leg: "))

print("The hypotenuse will measure {:.2f}".format(hypot(co,ca)))