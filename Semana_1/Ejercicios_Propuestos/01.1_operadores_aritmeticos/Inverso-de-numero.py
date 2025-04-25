# Inverso de número de tres cifras

numero= int(input("Ingresa un número de tres cifras: "))

C= numero//100
D= (numero//10)%10
U= numero%10

print(f"El número invertido es: {U}{D}{C}")