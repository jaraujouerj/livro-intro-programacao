# Tabela Fahrenheit para Celsius com validação usando try...except

def fahr_para_celsius(f):
    """Converte temperaturas Fahrenheit para Celsius."""
    return (5 / 9) * (f - 32)

def cria_tabela_celsius(fahr):
    """Cria tabela Celsius a partir de tab Fahr."""
    celsius = [None] * len(fahr)
    for i, temp in enumerate(fahr):
        celsius[i] = fahr_para_celsius(fahr[i])
    return celsius

def main():
    """Programa principal."""
    while True:
        try:
            inicio = int(input('Qual o início das temperaturas Fahrenheit? '))
            fim = int(input('Qual o final das temperaturas Fahrenheit? '))
            passo = int(input('Qual o passo das temperaturas Fahrenheit? '))
            if passo == 0:
                print('O passo não pode ser zero.')
                continue
            break
        except ValueError:
            print('Valor inválido. Digite um número inteiro.')

    fahr = range(inicio, fim + 1, passo)
    celsius = cria_tabela_celsius(fahr)
    print('Tabela de conversão de Fahrenheit para Celsius')
    for i, temp in enumerate(fahr):
        print('{:>5d} -> {:>5.1f}'.format(temp, celsius[i]))

main()
