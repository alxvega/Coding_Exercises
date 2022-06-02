"""### Ejercicio 3

Dado un String y una frase decir cuantas veces se repite la palabra en esa frase dada.

- Input: `("Hola", "Hola cómo andas?")`
- Output: `1`
"""

def repeated_word(word:str, sentence:str):
    return sentence.count(word)
print(repeated_word("Hola", "Hola cómo andas?"))
