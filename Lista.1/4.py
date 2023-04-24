#4. Faça um programa que leia um número inteiro e exiba se ele é par ou ímpar.
n = int (input ("Insira o número "))
if n <=0:
    print (f"O número {n} é neutro")
elif n % 2 == 0:
    print (f"O número {n} é par")

else:
    print (f"O número {n} é impár")