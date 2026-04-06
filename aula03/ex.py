numero = int(input('digite seu numero:'))
if numero % 2 == 0:
    print('seu numero é par')
else:
    print('seu numero é ímpar')

print('='*30)
#exercicio 2

num1 = float(input('digite seu numero:'))
num2 = float(input('digite seu numero:'))
if num1 > num2:
    print(f'o {num1} é o maior numero')
elif num2 > num1:
    print(f'o {num2} é o maior numero')
elif num1 == num2:
    print(f'os numeros são iguais')

print('='*30)
#exercicio 3

print('digite os seus numeros')
nota1 = float(input('digite sua primeira nota:'))
nota2 = float(input('digite sua segunda nota:'))
nota3 = float(input('digite sua terceira nota:'))
nota4 = float(input('digite sua quarta nota:'))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(media)

if media >= 7:
    print('você foi aprovado')
elif media >= 5:
    print('voce esta de recuperação')
elif media < 5:
    print('voce foi reprovado')

print('='*30)
#exercicio 5
nume1 = int(input('digite seu numero:'))
nume2 = int(input('digite seu numero:'))
if nume1 % nume2 == 0:
    print('eles são multiplos')
else:
    print('eles não são multiplos')

print('='*30)
#exercicio 6
number1 = int(input('digite seu numero:'))
number2 = int(input('digite seu numero:'))
conta = input('qual conta voce deseja efetuar:(+, -, *, /)')
if conta == '+':
    soma = number1 + number2
    print(f'a soma de {number1} e {number2} é {soma}')
elif conta == '-':
    diferenca = number1 - number2
    print(f'a subtração de {number1} e {number2} é {diferenca}')
elif conta == '*':
    produto = number1 * number2
    print(f'a multiplicação de {number1} e {number2} é {produto}')
elif conta == '%':
    if number2 != 0:
        quociente = number1 / number2
        print(f'a divisão de {number1} e {number2} é {quociente}')
    else:
        print('não é possivel realizar a conta')
        exit()

else:
    print('sem dados o suficiente')
    exit()

print('='*30)
#exercicio 7

idade = int(input('digite sua idade:'))

if idade >= 16 and idade < 18:
    print('seu voto é opcional')
elif idade > 70:
    print('seu voto é opcional')
else:
    print('seu voto é obrigtorio')

print('='*30)
#exercicio 8

salario = float(input('digite o seu salário:'))
if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
elif salario >= 1500:
    percentual = 5

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print("\n--- Resultado ---")
print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")








