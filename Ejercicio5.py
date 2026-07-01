lado1 = 3
lado2 = 4
lado3 = 5

# Aplicamos el teorema de la desigualdad triangular:
# La suma de la longitud de cualesquiera dos lados debe ser mayor que el tercer lado.
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Los lados pueden formar un triángulo.")
else:
    print("Los lados NO pueden formar un triángulo.")
