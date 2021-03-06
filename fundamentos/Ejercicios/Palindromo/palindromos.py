from os import system

system("cls")

print('***************************')
print('PALÍNDROMO')
print('***************************\n')

print('Los palíndromos son palabras, frases o números que leídos de atrás hacia adelante se leen igual que de adelante hacia atrás.\n')


texto = input("Ingrese la palabra que desea evaluar : ").lower().replace(' ', '')
caracteres = len(texto)


def validaPalindromo(text):
    igual, aux = 0, 0
    for ind in reversed(range(0, len(text))):
        if text[ind].lower() == text[aux].lower():
            igual += 1
            aux += 1
    if len(text) == igual:
        return True
    else:
        return False

def validaPalindromo1(text):
    if text == text[::-1]:
        return True
    else:
        return False

if caracteres > 1:
    if validaPalindromo1(texto):
        print("\nEl texto es palindromo!\n")
    else:
        print("\nEl texto no es palindromo!\n")
else:
    print("\nLa cadena no contiene los caracteres suficientes!\n")
