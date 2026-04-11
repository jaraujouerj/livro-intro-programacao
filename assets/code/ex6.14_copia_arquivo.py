# Copia o conteúdo de um arquivo para outro, verificando se o destino já existe

import os

origem = input('Digite o nome do arquivo de origem: ')
destino = input('Digite o nome do arquivo de destino: ')

if os.path.exists(destino):
    resposta = input(f'O arquivo "{destino}" já existe. Sobrescrever? (s/n): ')
    if resposta.lower() != 's':
        print('Operação cancelada.')
    else:
        with open(origem, 'r') as arq_origem:
            conteudo = arq_origem.read()
        with open(destino, 'w') as arq_destino:
            arq_destino.write(conteudo)
        print(f'Arquivo copiado para "{destino}".')
else:
    with open(origem, 'r') as arq_origem:
        conteudo = arq_origem.read()
    with open(destino, 'w') as arq_destino:
        arq_destino.write(conteudo)
    print(f'Arquivo copiado para "{destino}".')
