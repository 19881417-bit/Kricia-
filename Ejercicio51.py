mensaje = "Hola Mundo"
desplazamiento = 3

resultado = ""

for letra in mensaje:
    if letra.isalpha():
        base = ord('A') if letra.isupper() else ord('a')
        nueva = chr((ord(letra) - base + desplazamiento) % 26 + base)
        resultado += nueva
    else:
        resultado += letra

print("Mensaje cifrado:", resultado)