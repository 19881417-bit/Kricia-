import random

numero = random.randint(1, 100)
intentos = 0

while True:
    adivinanza = int(input("Adivina el número: "))
    intentos += 1

    if adivinanza < numero:
        print("Muy bajo")
    elif adivinanza > numero:
        print("Muy alto")
    else:
        print("¡Correcto!")
        print("Intentos:", intentos)
        break