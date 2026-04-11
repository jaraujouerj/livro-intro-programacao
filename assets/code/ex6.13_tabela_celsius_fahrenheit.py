# Salva em arquivo a tabela de conversão Celsius → Fahrenheit de 0 a 300

def celsius_para_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

with open('tabela_temperaturas.txt', 'w') as arquivo:
    arquivo.write(f'{"Celsius":>10} {"Fahrenheit":>12}\n')
    arquivo.write('-' * 24 + '\n')
    for c in range(0, 301, 10):
        f = celsius_para_fahrenheit(c)
        arquivo.write(f'{c:>10} {f:>12.1f}\n')

print('Tabela salva em tabela_temperaturas.txt')
