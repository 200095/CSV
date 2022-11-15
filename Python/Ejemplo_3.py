import sys

x = 0
y = 0

try:
    x = int(input("x :"))
    y = int(input("y :"))
        
except ValueError:
    print("Error: NO HAS PUESTO UN NÚMERO")     
try:
    resultado = x/y
except ZeroDivisionError:
    print("Error: No se puede dividir por eso")
    sys.exit(1)

print(f"{x} / {y} = {resultado}")