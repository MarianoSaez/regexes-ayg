#!/usr/bin/python3
import re

regex = re.compile(r"([a-z]ñ{1,2}\.[a-z]+@(alumno){1}\.um\.edu\.ar|[a-z]+\.[a-z]+@um\.edu\.ar)")

while True:
    mail = input("\nIngrese su correo de la universidad: ")
    if regex.match(mail):
        print("Log In exitoso")
        break
    print('Introduzca nuevamente su mail')
