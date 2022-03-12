print('GERADOR DE P.A')
print('-=-'*10)
termo=int(input('Digite o primeiro termo:'))
razão=int(input('Digite a razão:'))
primeiro=termo
cont=1
while cont <=10:
    print(f'{termo}', end=' ')
    termo=termo+razão
    cont=cont+1
print('FIM')

