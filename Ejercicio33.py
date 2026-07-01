filas = 4

for i in range(1, filas + 1):
    asc = ""
    desc = ""

    for j in range(1, i + 1):
        asc += str(j)

    for j in range(i - 1, 0, -1):
        desc += str(j)

    print(" " * (filas - i) + asc + desc)