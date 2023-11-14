idade_dias = int(input(f'Informe sua idade em dias: '))
print('')

anos = idade_dias // 365
meses = (idade_dias % 365) // 30
dias = (idade_dias % 365) % 30

idade_dias  = int(idade_dias)
print(f"Você tem {anos} anos, {meses} meses e {dias} dias de vida! :-) ")   