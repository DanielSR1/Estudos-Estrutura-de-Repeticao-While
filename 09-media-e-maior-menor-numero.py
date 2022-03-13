print('\033[4mVAMOS CALCULAR A MÉDIA DE TODOS OS NÚMERO DIGITDOS\033[m')
resposta='s'
media=soma=quantidade=maior=menor=0
while resposta in'Ss':
    nu=int(input('Digite um número: '))
    soma=soma+nu
    quantidade=quantidade+1
    if quantidade==1:
        maior=menor=nu
    else:
        if nu>maior:
         maior=nu
        if nu < menor:
                menor=nu
    resposta=str(input('\033[34mDeseja continuar? [S/N]\033[m')).upper() .strip()[0]
media=soma/quantidade
print(f'\033[32ma média entre os números digitados é {media}\033[m')
print(f'\033[32mO maior número digitado foi {maior} e o manor número digitado foi {menor}.\033[m')
print('ACABOU')