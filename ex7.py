"""### Ejercicio 7

Dados dos numeros, devolver cuantos numeros impares hay ENTRE ellos

- Input: `(1, 100)`
- Output: `49`
"""


def get_odd_in_range(start: int, end: int):
    counter = 0
    for i in range(start+1, end):
        if i % 2 != 0:
            counter += 1
    return counter

print(get_odd_in_range(1,100))