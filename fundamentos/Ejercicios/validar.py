from os import system

system("cls")

print('***************************')
print('VALIDAR CADENA')
print('***************************\n')


link1 = 'https://wwww.epn.edu.ec.ecuador'
link2 = 'https://modemat.com'
link3 = 'http:/fis.edu.lat'


def valida(text):
    if text.startswith('https'):
        if text.endswith('.com'):
           return True
        else:
           return False
    else:
        return False
def valida1(text):
    if text.startswith('https') and text.endswith('.com'):
           return True
    else:
        return False

print ('link1:' ,valida(link1));
print ('link2:' ,valida(link2));
print ('link3:' ,valida(link3));
print ('link1:' ,valida1(link1));
print ('link2:' ,valida1(link2));
print ('link3:' ,valida1(link3));
