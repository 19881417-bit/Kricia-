texto = "programacion en python"

frecuencia = {}

for caracter in texto:
    if caracter != " ":
        frecuencia[caracter] = frecuencia.get(caracter, 0) + 1

print(frecuencia)