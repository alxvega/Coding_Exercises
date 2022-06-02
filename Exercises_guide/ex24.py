"""### Ejercicio 24

Dado un array de enteros y un numero, detectar si esa lista de numeros es una permutacion del 1 al numero aportado.

Permutacion: Secuencia de numeros en orden sin que falte ninguno entre ellos

- Input: `([1,2,3,4,5], 5)`
- Output: `true`"""


def check_permutation(numbers:list, number:int):
    return True if list(range(1,number+1)) == numbers else False

print(check_permutation([1,2,3,4,5], 5))




