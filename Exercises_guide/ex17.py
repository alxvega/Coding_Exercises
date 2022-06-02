"""### Ejercicio 17

Dado un numero, mostrar los numeros de 1 hasta el numero. Para multiplos de tres, escribir "denu" en lugar del numero, para los multiplos de cinco, "lemon", y si es multiplo de tres y cinco, "denolemon"

- Input: `6`
- Output: `1 2 denu 4 lemon denu`
"""


def censor_fives(end: int):
    for number in range(1, end+1):
        if number % 5 == 0 and number % 3 == 0:
            print('denulemon')
            continue
        if number % 3 == 0:
            print('denu')
            continue
        if number % 5 == 0:
            print('lemon')
            continue
        print(number)


censor_fives(6)
