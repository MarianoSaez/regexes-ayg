import re
from pass_generator import random_pass

regex = re.compile(r"(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z].*[a-z])(?=.*\W).{8,}")

eleccion = int(input('Desea ingresar una contraseña o prefiere generar'
               'una aleatoria [1-0]: '))
if eleccion == 1:
    passw = input('Ingrese una contraseña: ')
else:
    passw = random_pass(8)

if regex.match(passw):
    print(f'La contraseña {passw} cumple los requisitos minimos')
else:
    print(f'La contraseña {passw} NO cumple los requisitos minimos')
