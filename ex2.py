"""### Ejercicio 2

Dado un String comprobar si es un palindromo o no (se leen igual del derecho y del revés), por ejemplo Bob, Pop, etc...
No tener en cuenta espacios ni simbolos.

- Input: `"otto"`
- Output: `true`

Posee dos soluciones. Una validada con metodos de JS y otro con manejos de datos.

Pueden venir strings con todo tipo de caracteres y espacios. Un caso de uso quedo sin funcionar, a corregir."""


def reverse_string(word: str):
    reversed_word = ""
    for letter in reversed(word):
        reversed_word += letter
    return True if reversed_word == word else False


print(reverse_string("sdsfg"))
