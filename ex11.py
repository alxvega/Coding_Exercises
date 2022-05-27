"""### Ejercicio 11

Dado un String y una busqueda, censurar las coincidencias de la busqueda en el String con [-CENSURADO-]
Si ambos llegan vacios, devolver un "No se puede leer el texto y la busqueda". Y si llega un solo parametro, devolver "No se puede hacer la busqueda"

- Input: `('holi como va', 'holi)` -- Frase y palabra a censurar
- Output: `[-CENSURADO-] como va`
"""

def censor_string(sentence:str, word:str):
    return sentence.replace(word, "[-CENSORED-]")

print(censor_string("holi como va?", "holi"))