#faça um programa que leia um  ângulo qualquer 
# e  mostre na tela  o valor  do seno, cosseno 
# e tangente desse ângulo.

from math import sin, cos, tan, radians

n = float(input("Enter the angle: "))
print("The angle of {:.2f} has the sine of {:.2f}".format(n, sin(radians(n))))
print("The angle of {:.2f} has the cosine of {:.2f}".format(n, cos(radians(n))))
print("The angle of {:.2f} has the tangent of {:.2f}".format(n, tan(radians(n))))