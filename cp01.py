def question(text):
    print(text)
    return input('> ')

nome = question('qual é o seu nome: ')
valor_de_hora_de_trabalho = float(question('qual foi o tempo de trabalho: '))
DiasTrabalho = int(question('quantos dias voce trabalhou: '))

quantidade_de_horas_no_mes = valor_de_hora_de_trabalho * DiasTrabalho
bonus = float(question('qual foi o bonus do mes: '))
desconto = float(question('qual é o desconto total do mes: '))

ValorBruto = valor_de_hora_de_trabalho * quantidade_de_horas_no_mes + bonus
ValorLiquido =  ValorBruto * (desconto * 0.01)

print(f'nome: {nome}')
print(f'valor_de_hora_de_trabalho: {valor_de_hora_de_trabalho} Horas')
print(f'quantidade_de_horas_no_mes {quantidade_de_horas_no_mes} Horas')
print(f'bonus: R${bonus}')
print(f'desconto: R${desconto:2f} ({desconto:.0f}%)')
print(f'ValorBruto: R${ValorBruto}')
print(f'ValorLiquido: R${ValorLiquido}')