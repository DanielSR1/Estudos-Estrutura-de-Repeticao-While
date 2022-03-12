print('GERADOR DE P.A')
print('-=-'*10)
termo=int(input('Digite o primeiro termo:'))
razão=int(input('Digite a razão:'))
primeiro=termo
cont=1
total=0
mais=10 
while mais !=0:
    total=total+mais
    while cont <=total:
        print(f'{termo}', end=' ')
        termo=termo+razão
        cont=cont+1
    print('PAUSA')
    mais=int(input('Quantos termos você quer mostrar a mais?' ))
print('FIM')

