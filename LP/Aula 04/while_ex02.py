num = int(input('Digite um numero: '))

passo = 1 if num > 0 else -1
contador = 1 if num > 0 else -1

# if num > 0:
#     passo = contador = 1
# else:
#     passo = contador = -1

while contador != num + passo:
    print(contador, end=' ')
    # contador += passo
    contador = contador + passo

print()