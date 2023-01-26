# Crie  um programa que leia  o nome  completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espeços).
# Quantas letras tem o primeiro nome.

full_name = str(input("Enter your full name: "))
print('Analyzing your name...')
print("Your name in capital letters is {}".format(full_name.upper()))
print("Your lowercase name is {}".format(full_name.lower()))
print("Your name has a total of {} letters".format(len(full_name) - full_name.count(' ')))
# print("Your first name has {} letters".format(full_name.find(' ')))
part = full_name.split(' ')
print("His first name is {} and he has {} letters".format(part[0], len(part[0])))