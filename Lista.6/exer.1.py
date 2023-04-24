#A série de Fibonaci é formada pela sequencia 1,1,2,3,5,8,13,21,35,55,... Faça um programa capaz de gerar a série até o n-ésimo termo.

n1 = 1
n2 = 1  
n3 = 0
g = 0

nf = int(input("Quer fazer quantas vezes? "))
print("1")
print("1")
for i in range(1,nf-1):
    g = n2
    n3 = n1 + n2
    print(n3)
    n2=n3
    n1=g
