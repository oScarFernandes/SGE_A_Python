num = 200

while num < 400:
    if 100 <= num <= 400:
        print(f"El número {num} està entre 100 i 400.")
    break
else:
    print(f"El número {num} no està entre 100 i 400.")