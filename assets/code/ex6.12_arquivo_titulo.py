# Converte a primeira letra de cada palavra de um arquivo em maiúscula

nome_arquivo = input('Digite o nome do arquivo: ')
with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
print(conteudo.title())
