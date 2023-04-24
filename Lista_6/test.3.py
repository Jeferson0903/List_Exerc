#A série de Fibonaci é formada pela sequencia 1,1,2,3,5,8,13,21,35,55,... Faça um programa capaz de gerar a série até o n-ésimo termo

n = int(input("digite um número:"))
fib = [1, 1]
while fib[-1] < n:
    next_fib = fib[-1] + fib[-2]
    fib.append(next_fib)
for f in fib:
    if f <= n:
        print (f,",", end="")

