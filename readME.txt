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