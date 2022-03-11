#NESSE EXERCICIO DESENVOLVI UM PROGRAMA CAPZ DE FAZER OPERAÇÕES MATEMÁTICAS SIMPLES ENTRE 2 NÚMEROS ESCOLHIOS PELO USUÁRIO.
from time import sleep
v1=int(input('Digite o primeiro valor '))
v2=int(input('Digite o segundo valor '))
opcao=0
while opcao !=5:
    print(f'\033[35mO que você deseja fazer com os valores {v1} e {v2}?\033[m')
    print('\033[34mDigite [1] para SOMAR')
    print('Digite [2] para MULTIPLICAR')
    print('Digite [3] para sabe QUAL É MAIOR')
    print('Digite [4] par ESCOLHER OUTROS NÚMEROS')
    print('Digite [5] para SAIR DO PROGRAMA\033[m')
    opcao=int(input('QUAL A SUA OPÇÃO? '))
    if opcao==1:
        soma=v1+v2
        print(f'A soma entre {v1} e {v2} é {soma}.')
    elif opcao==2:
        multi=v1*v2
        print(f'A multiplicação entre {v1} e {v2} é {multi}.')
    elif opcao==3:
        if v1>v1:
            print(f'{v1} É MAIOR QUE {v2}')
        else:
            print(f'{v2} É MAIOR QUE {v1}')
    elif opcao==4:
        v1=int(input('Digite o primeiro valor '))
        v2=int(input('Digite o segundo valor '))
    elif opcao==5:
        print('FINALIZANDO...')
    else:
        print('OPÇÃO INVÁLIDA.')
    print('=-='*15)
    sleep(2)
print('FIM DO PROGRAMA, VOLTE SEMPRE!')
    

