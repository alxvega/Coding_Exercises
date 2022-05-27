"""### Ejercicio 5

Sacar el porcentaje de un numero. Mandamos tanto el porcentaje como el numero por parametros.

- Input: `(20, 100)` -- El 20% de 100
- Output: `20`"""


def get_percentage(number, total):
    return number*total/100


print(get_percentage(20, 100))
