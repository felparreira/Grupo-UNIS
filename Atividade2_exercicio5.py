def inverter(frase):
    palavras = frase.split()
    reverse = ' '.join([palavra[::-1] for palavra in palavras])
    return reverse

frase_inserida = input(f'Digite uma frase para inverter: ')
frase_invertida = inverter(frase_inserida)

print(f'Frase com as palavras invertidas: {frase_invertida}')