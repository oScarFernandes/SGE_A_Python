num = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]

suma_parells = 0
suma_imparells = 0

for x in num:
    if x % 2 == 0:
        suma_parells += x
    else:
        suma_imparells += x

print(f"Suma dels números parells: {suma_parells}")
print(f"Suma dels números imparells: {suma_imparells}")