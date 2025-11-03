# Pedido de Notas em Estrutura de Repetição
# nota1 = float(input('Digite a 1ª nota: '))
# nota2 = float(input('Digite a 2ª nota: '))
# nota3 = float(input('Digite a 3ª nota: '))

soma = 0
qtd_notas = int(input('Digite a quantidade de notas: '))

for n in range(qtd_notas):
    nota = float(input(f'Digite a {n + 1}ª nota: '))
    soma += nota

media = soma / qtd_notas

print(f'A media das notas é igual a {media:.2f}')