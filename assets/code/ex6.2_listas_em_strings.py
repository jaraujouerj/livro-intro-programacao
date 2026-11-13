"""Exercício 6.2: o que das listas funciona em strings?

Parte 1: testa comandos de listas em uma string.
Parte 2: refaz programas do capítulo 5 trocando listas por strings.
Cada teste é executado dentro de um try/except: o programa mostra o
resultado ou o erro e continua com o teste seguinte.
"""
import contextlib
import io


def tenta(rotulo, comandos, entradas=()):
    """Executa os comandos (texto) e mostra o resultado ou o erro."""
    saida = io.StringIO()
    respostas = iter(entradas)
    try:
        with contextlib.redirect_stdout(saida):
            # 'input' é trocado para o teste não esperar o teclado.
            ambiente = {'input': lambda texto='': next(respostas)}
            exec(comandos, ambiente)
        resultado = saida.getvalue().strip().replace('\n', ' | ')
        print(f'OK    {rotulo:<28} {resultado}')
    except Exception as erro:
        print(f'ERRO  {rotulo:<28} {type(erro).__name__}: {erro}')


print('=== Parte 1: comandos de listas aplicados a s = "celacanto" ===')
testes = [
    # --- leitura: funciona ---
    ('s[0], s[-1]', 'print(s[0], s[-1])'),
    ('len(s)', 'print(len(s))'),
    ('for c in s', 'print([c for c in s])'),
    ('enumerate(s)', 'print(list(enumerate(s))[:3])'),
    ('"can" in s', 'print("can" in s)'),
    ('s[2:5]', 'print(s[2:5])'),
    ('s[::2]', 'print(s[::2])'),
    ('s[::-1]', 'print(s[::-1])'),
    ('s + "xx"', 'print(s + "xx")'),
    ('s * 2', 'print(s * 2)'),
    ('s.count("ca")', 'print(s.count("ca"))'),
    ('s.index("can")', 'print(s.index("can"))'),
    ('min(s), max(s)', 'print(min(s), max(s))'),
    ('sorted(s)', 'print(sorted(s))'),
    ('list(s)', 'print(list(s))'),
    ('s == "celacanto"', 'print(s == "celacanto")'),
    # --- erros de índice, tipo e valor ---
    ('s[20]', 'print(s[20])'),
    ('3 in s', 'print(3 in s)'),
    ('s + ["a"]', 'print(s + ["a"])'),
    ('s.index("z")', 'print(s.index("z"))'),
    ('sum(s)', 'print(sum(s))'),
    # --- escrita: não funciona, string é imutável ---
    ('s[0] = "x"', 's[0] = "x"'),
    ('s[1:3] = "xx"', 's[1:3] = "xx"'),
    ('del s[0]', 'del s[0]'),
    ('s.append("x")', 's.append("x")'),
    ('s.extend("xy")', 's.extend("xy")'),
    ('s.insert(1, "x")', 's.insert(1, "x")'),
    ('s.remove("c")', 's.remove("c")'),
    ('s.pop()', 's.pop()'),
    ('s.sort()', 's.sort()'),
    ('s.reverse()', 's.reverse()'),
    ('s.copy()', 's.copy()'),
]
for rotulo, comando in testes:
    tenta(rotulo, f's = "celacanto"\n{comando}')

print()
print('=== Parte 2: programas do capítulo 5 com strings no lugar de listas ===')
programas = {
    '5.1 soma de notas': """
notas = '7894'
soma = notas[0] + notas[1] + notas[2] + notas[3]
print('A média é igual a ', soma / 4)""",
    '5.5 soma com for': """
notas = '7894'
soma = 0
for nota in notas:
    soma += nota
print('A média é igual a ', soma / 4)""",
    '5.5 com int(nota)': """
notas = '7894'
soma = 0
for nota in notas:
    soma += int(nota)
print('A média é igual a ', soma / 4)""",
    '5.6 lista mutável': """
notas = '7819'
notas[3] = '6'""",
    '5.8 dobra os itens': """
lista = '12357'
for i in lista:
    print(i * 2)""",
    '5.9 lista[i] *= 2': """
lista = '12357'
for i in range(len(lista)):
    lista[i] *= 2""",
    '5.15 compreensão': """
lista = '12357'
print([x * x for x in lista])""",
    '5.15 com int(x)': """
lista = '12357'
print([int(x) ** 2 for x in lista])""",
    '5.17 bom dia': """
nomes = 'José João Joaquim'
print(['Bom dia, ' + x for x in nomes][:3])""",
    '5.17 com split()': """
nomes = 'José João Joaquim'
print(['Bom dia, ' + x for x in nomes.split()])""",
    '5.18 lista *= 3': """
lista = '123'
lista *= 3
print(lista)""",
    '5.19 diferença': """
a = '2345547'
b = '745'
print([x for x in a if x not in b])""",
    '5.20 fatiamento': """
planetas = 'MVTMSJUN'
print(planetas[2:5], planetas[:3], planetas[4:-1])""",
    '5.21 insere por fatia': """
primos = '23131719'
primos[2:2] = '57'""",
    '5.21 com concatenação': """
primos = '23131719'
primos = primos[:2] + '57' + primos[2:]
print(primos)""",
    '5.22 passo negativo': """
lista = '0123456789'
print(lista[::-1], lista[4::-1], lista[5:2:-1])""",
    '5.23 i in primos': """
primos = '235711131719'
for i in range(3, 20, 2):
    print(i, i in primos)""",
    '5.23 com str(i)': """
primos = '235711131719'
print([i for i in range(3, 20, 2) if str(i) in primos])""",
    '5.24 del': """
primos = '23571113'
del primos[1:3]""",
    '5.25 count/index/min/max': """
lista = '1230124'
print(lista.count('1'), lista.index('4'), min(lista), max(lista))""",
    '5.25 append': """
lista = '123'
lista.append('3')""",
    '5.26 append': """
numeros = ''
for i in range(3):
    numeros.append(int(input()))""",
    '5.26 com +=': """
numeros = ''
for i in range(3):
    numeros += str(int(input()))
print(numeros)""",
    '5.27 atribuição': """
lista1 = '123'
lista2 = '123'
lista2[1] = '4'""",
    '5.28 alias': """
lista1 = '123'
lista2 = lista1
lista2 += 'x'
print(lista1, lista2)""",
    '5.29 cópia por fatia': """
lista1 = '123'
lista2 = lista1[:]
print(lista2 is lista1)""",
    '5.30 com lista': """
def muda_valor(param):
    param += 'x'
lista = ['a', 'b', 'c']
muda_valor(lista)
print(lista)""",
    '5.30 com string': """
def muda_valor(param):
    param += 'x'
lista = 'abc'
muda_valor(lista)
print(lista)""",
    '5.31 matriz': """
matriz = ['0' * 4] * 3
print(matriz)
matriz[0][2] = '3'""",
    '5.a enumerate': """
for i, d in enumerate('DSTQQSS', 1):
    print(i, d, end='; ')""",
}
for rotulo, codigo in programas.items():
    tenta(rotulo, codigo, entradas=('4', '5', '6'))
