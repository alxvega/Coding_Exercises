"""### Ejercicio 15

Dado un String devolver el caracter mas usado.

- Input: `denuuu`
- Output: `u`"""


def most_used_char(sentence: str):
    previous_char = 0

    for char in sentence:
        if sentence.count(char) > previous_char:
            most_used_n = char
    return print(most_used_n)

most_used_char('denuuu')