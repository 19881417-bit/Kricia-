decimal = 42
binario = ""

while decimal > 0:
    binario = str(decimal % 2) + binario
    decimal //= 2

print("Binario:", binario)