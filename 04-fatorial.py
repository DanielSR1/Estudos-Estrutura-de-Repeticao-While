#NESSE EXERCICO DESENOLVI UM POROGRAMA CAPAZ DE CALCULAR O FATORIAL DO NÚMERO ESCOLHIDO PELO USUÁRIO.
from math import factorial
print('\033[7mVamos verificar qual fatorial do número escolhido.\033[m')
n=int(input('\033[36mDigite um número: \033[m'))
f=factorial(n)
c=n
fa=1
print(f'o valor de  {n}! é:')
while c >0: 
    print(f'\033[32m{c}', end=' ')
    print(f'x' if c>1 else '=', end=' ')
    fa=fa*c
    c-=1
print(f'{fa}')

