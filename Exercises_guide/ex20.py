from pprint import pprint
"""### Ejercicio 20

Dados dos String crear un algoritmo que compruebe si son anagramas entre si (Si ambos usan los mismos caracteres en una misma cantidad)

- Input: `(Riesgo, Sergio)`
- Output: `true`"""


def check_anagram(word_one: str, word_two: str):
    word_one, word_two = word_one.lower(), word_two.lower()
    characters_used_a = {char: word_one.count(char) for char in word_one}
    coincidences = 0

    for character in word_two:
        if character not in characters_used_a.keys():
            return f'{character} is missing in the first word. These terms are not an anagram.'

        if character in characters_used_a.keys() and characters_used_a[character] == word_two.count(character):
            coincidences += 1

    if coincidences == len(word_two):
        return 'These terms are anagrams.'
    else:
        return 'The characters between these terms are the same, not their quantity.'


print(check_anagram('Riesgo', 'Sergiooo'))
