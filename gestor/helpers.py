""" Funciones de ayuda """

import os
import platform


def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def input_text(min_length, max_length):
    while True:
        text = input("> ")
        if len(text) >= min_length and len(text) <= max_length:
            return text
