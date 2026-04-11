# Média de números digitados pelo usuário

numeros = []
while True:
    entrada = input('Digite um número (ou "fim" para encerrar): ')
    if entrada.lower() == 'fim':
        break
    try:
        numeros.append(float(entrada))
    except ValueError:
        print('Valor inválido. Tente novamente.')

if len(numeros) > 0:
    media = sum(numeros) / len(numeros)
    print(f'Média: {media:.2f}')
else:
    print('Nenhum número digitado.')
