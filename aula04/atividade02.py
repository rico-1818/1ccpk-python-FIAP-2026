def validar_nota(nota):
    while nota < 0 or nota > 10:
        print('a nota deve estra entre 0 e 10')
        nota = float(input('digite novamente a nota: '))
    return nota

notaA = float(input('digite a 1ª nota: '))
notaA = validar_nota(notaA)

notaB = float(input('digite a 2ª nota: '))
while notaB < 0 or notaB > 10:
        print('a nota deve estra entre 0 e 10')
        notaB = float(input('digite novamente a nota: '))


media = (notaA + notaB) / 2
print(media)