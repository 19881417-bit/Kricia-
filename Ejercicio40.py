lista = [1, 2, 3, 4, 5]
k = 2

k = k % len(lista)

resultado = lista[-k:] + lista[:-k]

print(resultado)