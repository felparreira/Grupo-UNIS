import math

def num_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False
    return True

for num in range(1, 101):
    if num_primo(num):
        print(f'{num} é um número primo.')
    else:
        print(f'{num} não é um número primo.')