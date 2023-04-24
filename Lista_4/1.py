#Analise o programa abaixo e, para cada uma das saídas (comandosprint), detalhe passo a passo como o Python (segundo suas prioridades) resolveria as equações e o resultado final obtido.
x = 3
y = 4
z = 0.6

print (x+x*x**(y*x)/z)
print (((not (x+z<y)) or (x+x*z >= y)) and True)

#'O python primeiro avalia a expressão y*x, resultando em 12. Em seguida, avalia a expressão x**(y*x), resultando em 3 ** 12 = 531441. Depois, multiplica x por 531441, resultando em 1594323.' 
#'Por fim, divide 1594323 por 0.6, resultando em 2657205.0.'

#'Primeiro, o programa avalia a expressão (x+z<y). Como x=3, y=4 e z=0.6, temos x+z = 3.6 e x+z<y, portanto (x+z<y) é False. Em seguida, o programa avalia a expressão (x+x*z >= y).' 
#'Substituindo os valores, temos x+x*z = 3 + 3 * 0.6 = 4.8 e x+x*z >= y, portanto (x+x*z >= y) é True. O programa então avalia a expressão not (x+z<y), resultando em not False = True.'
#'Por fim, o programa avalia a expressão True and True, resultando em True. Portanto, a saída será:'