"""Dado un String y un numero, repetir el String las veces que diga el numero

- Input: `('denu', 2)` -- Palabra y veces que se debe repetir
- Output: `'denu' 'denu'`"""


def repeat_string(word: str, number: int):
    return f'{word}' * number

print(repeat_string('popaj',10))