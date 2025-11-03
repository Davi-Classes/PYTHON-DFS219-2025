fatorial = 1
num = int(input('Digite um numero para calcular o fatorial: '))

for i in range(1, num + 1):
    # fatorial = fatorial * i
    fatorial *= i

print(f'O fatorial de {num} é igual a {fatorial}')
