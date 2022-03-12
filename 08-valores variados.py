#NESSE EXERCICIO DESENVOLVI UM CÓDIGO CAPAZ DE IGNORAR O COMANDO "999" NA SOMA FINAL DOS VALORES
nu=cont=soma=0
nu=int(input('Digite um número [999 para parar] '))
while nu !=999:
    cont=cont+1
    soma=soma+nu
    nu=int(input('Digite um número [999 para parar] '))
print(f'VOCÊ DIGITOU {cont} números. E a soma entre eles foi {soma}')
print('ACABOU')