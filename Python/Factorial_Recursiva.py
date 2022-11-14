def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)
        
numero = int(input('Escribe tu número: '))

if (numero >= 0):
    result = factorial(numero)
    print(result)
else:
    print('Numero Positivo')