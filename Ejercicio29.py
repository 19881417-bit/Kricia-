peso = 70
altura = 1.75

imc = peso / (altura ** 2)

print("IMC:", round(imc, 2))

if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")