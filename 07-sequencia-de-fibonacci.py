print('\033[4mVAMOS CALCULAR A SEQUENCIA DE FIBONACCI.\033[m')
n=int(input('\033[32mQUANTOS TERMOS VOCÊ QUER MOSTRAR? '))
t1=0
t2=1
print(f'{t1} {t2}', end=' ')
cont=3
while cont<=n:
    t3=t1+t2
    print(f'{t3}', end=' ')
    cont=cont+1
    t1=t2
    t2=t3
print('\033[35mFIM')
