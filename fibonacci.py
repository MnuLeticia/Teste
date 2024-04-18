print ('-'*30)
print ('Seguencia de Fibonacci')
print ('-'*30)
n = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
fibonacci = [t1, t2]
print('~'*30)
print ('{} ⤑ {}' .format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    fibonacci.append(t3)
    print(' ⤑ {}' .format(t3), end='') 
    t1 = t2 
    t2 = t3 
    cont = cont + 1
print(' ⤑ FIM')
numerov = int(input('Digite um número para verificar se pertence à sequência de Fibonacci: '))
if numerov in fibonacci:
    print('O número {} pertence à sequência de Fibonacci.'.format(numerov))
else:
    print('O número {} não pertence à sequência de Fibonacci.'.format(numerov))