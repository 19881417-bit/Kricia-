registro = {
    "Ana": {
        "Matematica": [80, 90],
        "Ciencia": [85, 95]
    },
    "Luis": {
        "Matematica": [70, 75],
        "Ciencia": [88, 92]
    }
}

for estudiante, materias in registro.items():
    total = 0
    cantidad = 0

    for notas in materias.values():
        total += sum(notas)
        cantidad += len(notas)

    print(estudiante, "Promedio:", total / cantidad)