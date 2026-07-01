contraseña = "Python3.9!"

tiene_mayuscula = False
tiene_numero = False
tiene_especial = False

for caracter in contraseña:
    if caracter.isupper():
        tiene_mayuscula = True
    elif caracter.isdigit():
        tiene_numero = True
    elif not caracter.isalnum():
        tiene_especial = True

if len(contraseña) >= 8 and tiene_mayuscula and tiene_numero and tiene_especial:
    print("Contraseña válida")
else:
    print("Contraseña no válida")