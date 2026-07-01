inventario = {
    "Laptop": [(800, 5)],
    "Mouse": [(25, 3)],
    "Teclado": [(50, 10)]
}

total = 0

for producto, datos in inventario.items():
    for precio, stock in datos:
        total += precio * stock

print("Valor total:", total)

for producto, datos in inventario.items():
    for precio, stock in datos:
        if stock < 5:
            print("Bajo stock:", producto)