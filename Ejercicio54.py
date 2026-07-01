texto = """Python es un lenguaje de programación. Es muy popular en la actualidad. Python es versátil."""

palabras = texto.lower().replace(".", "").split()

# Total de palabras
total_palabras = len(palabras)

# Frecuencia
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

# Palabra más frecuente
mas_frecuente = max(frecuencia, key=frecuencia.get)

# Longitud promedio
promedio = sum(len(p) for p in palabras) / total_palabras

# Oraciones
oraciones = len([o for o in texto.split(".") if o.strip()])

print("Total palabras:", total_palabras)
print("Palabra más frecuente:", mas_frecuente)
print("Longitud promedio:", round(promedio, 2))
print("Número de oraciones:", oraciones)