a, b = 48, 18

while b != 0:
    a, b = b, a % b

print("MCD:", a)