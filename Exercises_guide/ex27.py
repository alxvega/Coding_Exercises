"""### Ejercicio 27

Dado un numero mostrar a cuantos años, meses y dias equivale.

- Input: `920`
- Output: `2 años, 6 meses y 2 dias`
"""


def int_to_date(day_count: int):
    years = int(day_count//365)
    months = (years*31)/12
    days = (months*12)/31
    print(int(map(round, years, months, days)))


int_to_date(920)
