import re

regex = re.compile(r'([0-2][0-9]|3[0-1])(/|-)(0[1-9]|1[0-2])\2([0-9]{4})')

fecha = input('Ingrese una fecha: ')

if regex.match(fecha):
    print(f'La fecha {fecha} se encuentra en un formato valido')
else:
    print(f'La fecha {fecha} se encuentra en un formato invalido')
