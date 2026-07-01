banco = {}
historial = []

def crear_cuenta(numero, titular, saldo, tipo):
    banco[numero] = {
        "titular": titular,
        "saldo": saldo,
        "tipo": tipo
    }

def depositar(numero, monto):
    banco[numero]["saldo"] += monto
    historial.append(("Depósito", numero, monto))

def retirar(numero, monto):
    if banco[numero]["saldo"] >= monto:
        banco[numero]["saldo"] -= monto
        historial.append(("Retiro", numero, monto))
    else:
        print("Fondos insuficientes")

def transferir(origen, destino, monto):
    if banco[origen]["saldo"] >= monto:
        banco[origen]["saldo"] -= monto
        banco[destino]["saldo"] += monto
        historial.append(("Transferencia", origen, destino, monto))
    else:
        print("Fondos insuficientes")

crear_cuenta("001", "Ana", 1000, "Ahorro")
crear_cuenta("002", "Luis", 500, "Corriente")

depositar("001", 200)
retirar("002", 100)
transferir("001", "002", 300)

print("Cuentas:")
print(banco)

print("\nHistorial:")
for movimiento in historial:
    print(movimiento)