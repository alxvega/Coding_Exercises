"""### Ejercicio 13

Dado un array, dividirlo en tantos sub-arrays como sea necesario basandonos en un numero que indique su tamaño.

- Input: `([1,2,3,4], 2)` -- Array y tamaño de divisiones
- Output: `([1,2], [3,4])`"""


def split_list(list_to_split, n_partitions):
    x = [list_to_split[(i*len(list_to_split))//n_partitions:((i+1) *len(list_to_split))//n_partitions] for i in range(n_partitions)]
    print(x)


split_list([1, 2, 3, 4], 2)
