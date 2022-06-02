"""Dado un numero mostrar una escalera con escalones de guiones usando el numero para los niveles de la escalera.

- Input: `4`
- Output:

```javascript
  [-]
  [-][-]
  [-][-][-]
  [-][-][-][-]
```"""


def draw_steps(number_int=4):
    for i in range(number_int+1):
        step = "[-]" * i
        print(f"{step}\n")
    
draw_steps()
