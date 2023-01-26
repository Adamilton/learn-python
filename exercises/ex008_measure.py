# Desenvolva um programa que leia uma distância em metros 
# e mostre os valoresrelativos em outras medidas.

n = float(input("Enter  number: "))
print(f"The distance of {n}m corresponds to:")
print("{:.3f}Km{:^20}{:.1f}dm".format(n/1000, '', n*10))
print("{:.3f}Hm{:^20}{:.1f}cm".format(n/100, '', n*100))
print("{:.3f}Dam{:^19}{:.1f}mm".format(n/10, '', n*1000))
