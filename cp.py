#!/usr/bin/python3
import re

regex = re.compile(r"([A-Z]{1}[\d]{4}[A-Z]{3}|[\d]{4})$")

while True:
    cp = input("\ncodigo postal: ")
    if regex.match(cp):
        print("Codigo postal Existe")
        break
    print('El codigo postal es invalido')
