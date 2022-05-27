"""### Ejercicio 4

Dado un String, darle la vuelta, invertir el orden de sus caracteres. No se pueden usar metodos del lenguaje, solo estructuras de control.

Hay dos soluciones. La primera sin el uso de pila y la segunda con, dependiendo de que tipo de solucion estamos buscando.

- Input: `"hola"`
- Output: `aloh`"""


def reverse_string(word: str):
    return word[::-1]


def reverse_string(word: str):
    reversed_word = ""
    for character in reversed(word):
        reversed_word += character
    return reversed_word


print(reverse_string("hola"))
