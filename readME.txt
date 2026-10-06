# Reto Martin:

Given 3 int values, a b c, return their sum.
However, if one of the values is 13 then it does not count towards
the sum and values to its right do not count. So for example,
if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1

### Solución

Se guardaron los argumentos en una lista y se recorrió con un `for`.
En cada iteración, si el valor es `13` se rompe el bucle con `break`;
en caso contrario, se suma al resultado.

---

# Reto Paulo:

Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4

### Solución

Se iteró sobre la lista de números usando un ciclo `for` y una variable booleana (`ignore`) como bandera. Al encontrar un `6`, la bandera se cambia a `True` para ignorar la suma de los valores siguientes. Si se encuentra un `7` mientras la bandera está activa, esta se cambia a `False` para reanudar la suma. Los números se suman al total únicamente cuando la bandera es `False`.

--- 

# Reto Rigo:

We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars before small bars.
Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2

### Solución

Primero sacamos la mayor cantidad de barras grandes que podemos usar sin pasarnos del objetivo (goal), luego calculamos lo que falta después de usar las grandes actuales que tenemos actualmente, Y al final, comprobamos si tenemos más o igual de cantidad de chocolates pequeños para cubrir lo restantes. Si es posible, se regresa la cantidad restante, sino se regresa un -1.

---
# Reto Owen:

Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().


no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3

### Solución
Lo que hice fue crear primero la funcion principal no_teen_sum(a, b, c) que se encarga de sumar los tres numeros, pero pasando cada uno por una funcion ayudante llamada fix_teen
la funcion fix_teen(n) recibe un numero y revisa si esta en el rango entre 13 y 19. Si está en ese rango y no es ni 15 ni 16, lo convierte en 0. Si es cualquier otro numero lo deja tal cual.
---

# Notas Martin:

## Corrección de commit en rama incorrecta

**Problema:** El commit `b247bc1` fue subido por error a `origin/main` en lugar de `origin/branch-team-bonaicero`.

**Solución:**

1. **Mover el commit a la rama correcta:**
   ```bash
   git switch branch-team-bonaicero
   git cherry-pick b247bc1
   git push   

2. **Limpiar main**
   git switch main
   git reset --hard 82de0b9
   git push origin main --force   

---
---

# Reto Baruch:

You are driving a little too fast, and a police officer stops you.
Write code to compute the result, encoded as an int value:
0=no ticket, 1=small ticket, 2=big ticket.

If speed is 60 or less, the result is 0.
If speed is between 61 and 80 inclusive, the result is 1.
If speed is 81 or more, the result is 2.
Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0

### Solución

Se creó la función `caught_speeding`, que recibe la velocidad y un valor booleano que indica si es cumpleaños. Si es cumpleaños, se restan 5 a la velocidad para aplicar la tolerancia adicional. Después, mediante condicionales `if`, `elif` y `else`, se determina el resultado: 0 si no hay multa, 1 si corresponde una multa pequeña y 2 si corresponde una multa grande.

---