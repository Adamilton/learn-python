something = input('type something: ')
print('the primitive type of this value is {0}'.format(type(something)))
print('Just spaces? {0}'.format(something.isspace()))
print("It's a number? {0}".format(something.isnumeric()))
print("It's alphabetic? {0}".format(something.isalpha()))
print("It's alphanumeric {0}".format(something.isalnum()))
print("Is it uppercase? {0}".format(something.isupper()))
print("Is it lowercase? {0}".format(something.islower()))
print("Is it capitalized? {0}".format(something.istitle()))
#print(" {0}".format(something.islower()))
