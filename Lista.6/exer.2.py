salario = 1000
porcento = 1.5
for ano in range (2006, 2024):
    salario *= (1+ porcento/100)
    if ano >2006:
        porcento *=2
        print (f"Salário em {ano}: R${salario: 2f}")
