"""### Ejercicio 18

Dado un numero, mostrar sus divisores (hasta el número)

- Input: `5`
- Output: `1 5`"""


def check_divisors(number):
    divisors = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)
    print(divisors)


check_divisors(5)