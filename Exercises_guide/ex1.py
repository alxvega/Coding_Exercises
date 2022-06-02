"""### Ejercicio 1

Dado un numero devolver su tabla de multiplicar completa. Por ejemplo:

- Input: `5`
- Output:

```javascript
Tabla del 5
5 x 1 = 5
5 x 2 = 10
(...)
```"""


def multiply(number: int):
    table = []
    for i in range(1, 10+1):
        item = f'{number} * {i} = {number*i}'
        table.append(item)
    return f'Tabla del {number}\n{table}'


print(multiply(5))
