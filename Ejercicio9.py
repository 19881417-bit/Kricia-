texto = "Hola Mundo Python"
contador = 0

for letra in texto.lower():
    if letra in "aeiou":
        contador += 1

print("Cantidad de vocales:", contador)