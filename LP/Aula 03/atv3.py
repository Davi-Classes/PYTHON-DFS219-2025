num1 = int(input('Digite o 1º numero: '))
num2 = int(input('Digite o 2º numero: '))


if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 == num2:
    print('Os numeros são iguais.')
else:
    print(f'{num2} é maior que {num1}')