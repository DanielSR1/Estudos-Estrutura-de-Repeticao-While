#NESSE EXERCICIO DESENVOLVI UM PROGRAMA CAPAZ DE JOGAR O JOGO DA ADVINHAÇÃO COM O USUÁRIO.
from random import randint
computador= randint(0,10)
print('\033[36mSOU SEU COMPUTADOR E ACABEI DE PENSAR EM UM NÚMERO ENTRE 0 E 10.')
print('VOCÊ CONSEGUE ACERTAR QUAL FOI?\033[m')
acertou=False
palpite=0
while not acertou:
    jogador=int(input('Qual é o seu palpite? '))
    palpite+=1
    if jogador==computador:
        acertou=True
    else:
        if jogador<computador:
            print('\033[31mHUUM... ACHO QUE É UM NÚMERO MAIOR\033[m.') 
        else:
            print('\033[31mOPS... ACHO QUE É UM NÚMERO MENOR.\033[m')
print('\033[32mVOCÊ ACERTOU!!')
print(f'O NÚMERO QUE EU PENSEI FOI {computador}.')
print(f'VOCÊ PRECISOU DE {palpite} PALPITE PARA ACERTAR.')
