# Codigo a modo de test para la regex 2.3 del TP1 de Automatas
# y Gramaticas - 3ro Ing. Informatica.

# Encoding=utf-8

from random import randint


# Genera una cadena de caracteres aleatoria de la longitud especificada
# param:
# @min_pass_len: Longitud de la cadena a generar
def random_pass(min_pass_len: int):
    # Alfabeto minusculas
    alfabet_lc = "abcdefghijklmnopqrstuvwxyz"

    # Alfabeto mayusculas
    alfabet_uc = alfabet_lc.upper()

    # Numeros
    numbers = "0123456789"

    # Caracteres especiales (algunos)
    specials = "`~!@#$%^&*()_+[]}{\\|';/?.>,<"

    # Lista de simbolos de donde sacar caracteres desde cadenas
    alfabetos = [alfabet_lc, alfabet_uc, numbers, specials]

    # Password
    password = ""

    for i in range(min_pass_len):
        # Elegir un alfabeto aleatorio de la lista
        alfabeto = alfabetos[randint(0, 3)]
        # Elegir un simbolo aleatorio del alfabeto
        char = alfabeto[randint(0, len(alfabeto)-1)]
        # Agregar a password el simbolo
        password += char

    return password


if __name__ == '__main__':
    print(random_pass(8))
