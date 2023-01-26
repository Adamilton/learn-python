# O mesmo professor do desafio anterior que sorteara ordem de 
# apresentação  de trabalhos dos alunos. Faça um programa  que
# leia o nome  dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
n1 = str(input('Enter first student: '))
n2 = str(input('Enter second student: '))
n3 = str(input('Enter third student: '))
n4 = str(input('Enter fourth student: '))

array = [n1, n2, n3, n4]
shuffle(array)
print('The order of presentation will be: \n{}'.format(array))