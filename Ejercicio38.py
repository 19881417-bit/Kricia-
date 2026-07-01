inicio, fin = 10, 50

primos = []

for n in range(inicio, fin + 1):
    es_primo = True

    if n < 2:
        es_primo = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                es_primo = False
                break

    if es_primo:
        primos.append(n)

print(primos)