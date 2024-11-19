salari = 5000

if salari < 15000:
    iva = 0
elif salari < 30000:
    iva = 10
elif salari < 60000:
    iva = 21
else:
    iva = 21

salari_iva = salari * (1 - iva / 100)
print("El salari amb IVA descomptat és:", salari_iva)