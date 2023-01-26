# Escreva um programa que converta uma temperatura  
# digitada  em °C e converta para °F.

n = float(input("Enter the temperature in °C: "))
print("The temperature of {:.2f}°C corresponds to {:.2f}°F".format(n, n*9/5+32 ))
