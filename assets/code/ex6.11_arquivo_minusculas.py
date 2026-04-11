# Converte todas as letras de um arquivo em minúsculas

nome_arquivo = input('Digite o nome do arquivo: ')
with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
print(conteudo.lower())
