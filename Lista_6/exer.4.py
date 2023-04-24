# Sendo H=1 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

N = int(input("Digite o valor de N: ")) 
H = 0

for i in range(1, N+1):
    H += 1/i
H = round(H)
print("O valor de H com", N, "termos é:", H)