#6. Faça um programa que leia três números e exiba o menor deles.
n1 = int (input ("Insira o número: "))
n2 = int (input ("Insira o número: "))
n3 = int (input ("Insira o número: "))
if n1<n2 and n1<n3:
    print (f"{n1} é o menor dos três números")
elif n2<n1 and n2<n3:
    print (f"{n2} é o menor dos três números")
else:
    print (f"{n3} é o menor dos três números")