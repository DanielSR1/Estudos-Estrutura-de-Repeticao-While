#NESSE EXERCICIO DESENVOLVI UM PROGRAMA CAPAZ DE VALIDAR DADOS DE UM REGISTRO UTILIZANDO REPETIÇÃO WHILE CORRETAMENTE.
G=str(input('VOCÊ GOSTA DE MAÇÃ? [SIM/NÃO] ')).upper()[0].strip()
while G not in 'SN':
     G=str(input('Dados inválidos. Por favor informe se você gosta de maçÃ: [SIM/NÃO] ')).upper()[0].strip()
if G =='S':
    print('OK! REGISTRAMOS QUE VOCÊ GOSTA DE MAÇÃ')
elif G == 'N':
    print('OK! REGISTRAMOS QUE VOCÊ NÃO GOSTA DE MAÇÃ')  

