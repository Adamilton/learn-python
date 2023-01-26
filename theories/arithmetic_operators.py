n1 = int(input('Enter a number: '))
n2 = int(input('Enter another number: '))
print('A soma é {} \n o produto é {} \n e a divisão é {:.3f}'.format(n1+n2, n1*n2, n1/n2), end=' >>> ')
print(f'A divisão inteira é  {n1//n2} e a potência é {n1**n2}')
pow(5,2)
print(5%2)

#orden de precedência

# 1 -> ()
# 2 -> **
# 3 -> *, /, //, %
# 4 -> +, -