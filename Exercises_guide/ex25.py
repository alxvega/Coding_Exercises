"""### Ejercicio 25

Dado un word, si hay mas mayusculas, pasar todo a mayuscula, y viceversa.

- Input: `"DENu"`
- Output: `DENU`
"""


def capital_or_lower(word: str):
    return word.upper() if len(list(filter(str.isupper, word))) > len(list(filter(str.islower, word))) else word.lower()


print(capital_or_lower('DENu'))
