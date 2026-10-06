def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed = speed - 5

    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2


# Pruebas
print(caught_speeding(60, False))  # 0
print(caught_speeding(65, False))  # 1
print(caught_speeding(65, True))   # 0
print(caught_speeding(81, False))  # 2
print(caught_speeding(85, True))   # 1