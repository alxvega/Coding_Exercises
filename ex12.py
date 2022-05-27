"""### Ejercicio 12

Dado un numero mostrar todos los numeros desde ese al 0 de 8 en 8 en una lista con guiones y cada numero debe empezar por "n"

- Input: `100`
- Output:

```javascript
-n 100
-n 92
-n 84
etc..
```"""

def reverse_step_int(number:int, step:int):
    return [f"-n {i}" for i in range(number, 0, -step)]
    
print(reverse_step_int(100,8))