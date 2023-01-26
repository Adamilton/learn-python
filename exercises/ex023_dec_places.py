
n = int(input("Enter a number: "))

print('Analyzing the number...')
print(f"unity : {n // 1 % 10}")
print(f"ten : { n // 10 % 10}")
print(f"hundred : {n // 100 % 10}")
print(f"thousand : {n // 1000 % 10}")