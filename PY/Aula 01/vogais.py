qtd_vogais = 0
texto = input('Digite um texto: ')

for letra in texto:
    if letra in ['a', 'e', 'i', 'o', 'u']:
        qtd_vogais += 1

# for letra in texto:
#     letra = letra.lower()
#     if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#         qtd_vogais += 1


print(f'Total Vogais: {qtd_vogais}')
    