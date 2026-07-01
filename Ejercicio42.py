lista_principal = [1, 2, 3, 4, 5, 6]
subsecuencia = [2, 4, 6]

indice = 0

for elemento in lista_principal:
    if indice < len(subsecuencia) and elemento == subsecuencia[indice]:
        indice += 1

if indice == len(subsecuencia):
    print("Sí es subsecuencia")
else:
    print("No es subsecuencia")