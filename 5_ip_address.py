import re

re = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))$')

while True:
    ip = input("Ingrese dirección IP: ")
    if re.match(ip):
        print("La dirección IP es válida")
        break
    print("La dirección IP NO es válida")
