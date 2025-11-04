# variavel auxiliar
soma = 0
qtd_notas = int(input('Quantas notas deseja calcular a média? '))

# 0, 1, 2, 3, 4
for n in range(qtd_notas):
    nota = float(input('Digite uma nota: '))
    soma += nota

media = soma / qtd_notas

print(f'Média: {media:.2f}')
