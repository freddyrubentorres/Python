numero = int(input("Ingresa un número : "))

if numero % 2 == 0:
    if numero > 0:
        print('numero par positivo')
    else:
        print('numero par negativo')
else:
    print('numero impar')
