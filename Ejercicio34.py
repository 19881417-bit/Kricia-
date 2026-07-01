numero = 1234
suma = 0

while numero > 0:
    suma += numero % 10
    numero //= 10

print("Suma:", suma)