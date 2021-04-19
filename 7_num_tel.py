import re

re = re.compile(r'^\+5426115[0-9]{7}$')

while True:
    tel = input("Ingrese su numero de telefono: ")

    if re.match(tel):
        print("El número ingresado es válido")
        break
    print("Número no válido. Intente nuevamente")
