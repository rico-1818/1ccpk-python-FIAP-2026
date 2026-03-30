idade = int(input('digite sua idade:'))

if idade >= 16 and idade < 18:
    print('seu voto é opcional')
elif idade > 70:
    print('seu voto é opcional')
else:
    print('seu voto é obrigtorio')