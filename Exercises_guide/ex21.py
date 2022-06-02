"""### Ejercicio 21

Dada un String y un numero, cortar el string mostrando X cantidad de caracteres dependiendo del numero enviado.

- Input: `(Denu, 2)`
- Output: `De`
"""


def slice_string(string: str, number: int):
    return string[0:number]


print(slice_string('HOLA', 2))
