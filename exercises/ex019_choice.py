# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faço um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
n1 = str(input('Enter first student: '))
n2 = str(input('Enter second student: '))
n3 = str(input('Enter third student: '))
n4 = str(input('Enter fourth student: '))

array = [n1, n2, n3, n4]
print('The chosen student was {}'.format(choice(array)))