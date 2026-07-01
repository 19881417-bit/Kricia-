import random
import string

longitud = 12

caracteres = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)

print("Contraseña generada:", contraseña)