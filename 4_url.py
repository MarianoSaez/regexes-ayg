#!/usr/bin/python3
import re

regex = re.compile(r"(http|https)?:?(\/\/)?(www)?\.?[a-zA-Z]*\.(com|org|gov|edu|net){1}\/?[a-zA-Z\d!#$%&?¿]*")

while True:
    url = input("\nurl: ")
    if regex.match(url):
        print("----------------------SU PAGINA WEB-----------------------")
        break
    print('No se puede acceder a este sitio. Intentelo nuevamente')
