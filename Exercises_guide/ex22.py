"""### Ejercicio 23

Dado un String poner en mayuscula la primera letra de cada palabra en la cadena y devolverla.

- Input: `hola soy denu lemon`
- Output: `Hola Soy Denu Lemon`"""


def capitalize_words(sentence: str):
    return " ".join(map(str.capitalize, sentence.split()))

print(capitalize_words('probando hola probando a ver que onda'))
