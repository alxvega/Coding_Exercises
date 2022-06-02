"""### Ejercicio 16

Dado una cadena de texto, devolver cuantas vocales tiene la misma.

- Input: `denu`
- Output: `2`
"""


def check_vowels(string: str):
    vowels = "aeiouAEIOU"
    vowels_used = 0
    for char in string:
        if char in vowels:
            vowels_used += 1

    return print(vowels_used)

check_vowels('denu')