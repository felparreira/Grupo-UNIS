print(f'Informe 3 números inteiros:')
print('')

num1 = int(input(f'Primeiro número -> '))
num2 = int(input(f'Segundo número -> '))
num3 = int(input(f'Terceiro número -> '))

nao_tringulo = num1 > (num2 + num3)
if not nao_tringulo:    
    calcula = (num1 + num2 + num3) /2
    area = (calcula * (calcula * num1) * (calcula - num2) * (calcula - num3))

    print(f'A área do triângulo é: {area:.2f}')
else:
    print(f'Os valores {num1}, {num2}, {num3} não formam um triângulo.')
