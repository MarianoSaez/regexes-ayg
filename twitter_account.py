import re

re = re.compile(r'^@(\w){4,15}$')

while True:
    cuenta = (input("Ingrese su usuario de Twitter: "))
    letras = len(cuenta)
    if re.match(cuenta):
        print("Su usuario es válido")
        break
    if letras < 5 or letras > 16:
        print("Su usuario debe tener entre 4 y 15 caracteres. Intente nuevamente") 
    else:
        print("Su usuario no es válido. Intente nuevamente")
