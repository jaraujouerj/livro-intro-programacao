# Função que dada uma nota entre 0.0 e 10.0 imprime na tela um
# conceito entre ‘A’ e ‘E’, segundo a tabela:
# A ≥ 9.0 9.0 > B ≥ 8.0 8.0 > C ≥ 7.0 7.0 > D ≥ 5.0 E < 5.0
# Se nota for menor que 0 ou maior que 10 imprime nota inválida

def conceito(nota):
    if nota < 0.0 or nota > 10.0:
        return "Nota inválida"
    elif nota >= 9.0:
        return 'A'
    elif nota >= 8.0:
        return 'B'
    elif nota >= 7.0:
        return 'C'
    elif nota >= 5.0:
        return 'D'
    else:
        return 'E' 
    
# Testando a função com algumas notas
notas_teste = [9.5, 8.5, 7.5, 6.0, 4.5, -1.0, 10.5]
print(f"Nota: {9.5} -> Conceito: {conceito(9.5)}")
print(f"Nota: {8.5} -> Conceito: {conceito(8.5)}")
print(f"Nota: {7.5} -> Conceito: {conceito(7.5)}")
print(f"Nota: {6.0} -> Conceito: {conceito(6.0)}")
print(f"Nota: {4.5} -> Conceito: {conceito(4.5)}")
print(f"Nota: {-1.0} -> Conceito: {conceito(-1.0)}")
print(f"Nota: {10.5} -> Conceito: {conceito(10.5)}")
print()


