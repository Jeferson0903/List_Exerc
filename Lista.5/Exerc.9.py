h = float(input("Qual sua altura? "))
ideal = 0
res = str(input("Digite 'M' se for mulher ou 'H' se for homem: "))

if res == "f":
    ideal = (62.1*h) - 44.7
else:
    ideal = (72.7*h) - 58
    

print("O peso ideal para você é :", ideal, "Kg")