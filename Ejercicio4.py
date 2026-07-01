num1 = 10
num2 = 5
operador = "+"

# Verificamos qué operación realizar según el operador
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    # Es buena práctica verificar que no se divida por cero
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error (división por cero)"
else:
    resultado = "Operador no válido"

print(f"Resultado: {num1} {operador} {num2} = {resultado}")
