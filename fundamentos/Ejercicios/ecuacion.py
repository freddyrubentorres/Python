'''
Descipcion: Permite calcular ecuaciones de segundo grado
Autor:Freddy Torres
Fecha: 04-02_2022
'''

import math
from os import system

system("cls")

print('***************************')
print('ECUACION 2 GRADO')
print('***************************')

print('Polinomio de la forma : ax^2+bx+c')



a=int(input('Ingrese a : '))
b=int(input('Ingrese b : '))
c=int(input('Ingrese c : '))

print('***************************')

x1=(-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
x2=(-b-math.sqrt((b**2)-(4*a*c)))/(2*a)

print('la ecuación : ',a,'-> ax^2 ',b,'-> bx',c,'-> c   tiene las soluciones :')
print('x1:',x1)
print('x2:',x2)






