num = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]
parells = []
imparells = []
for x in num:
    if x % 2 == 0:
        parells.append(x)
    else:
        imparells.append(x)
print(f"Números parells: {parells}")
print(f"Números imparells: {imparells}")