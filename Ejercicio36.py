texto = "Anita lava la tina"

texto = texto.replace(" ", "").lower()

if texto == texto[::-1]:
    print("Es palíndromo")
else:
    print("No es palíndromo")