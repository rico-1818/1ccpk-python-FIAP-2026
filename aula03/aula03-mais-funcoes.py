def boas_vindas(nome):
    print(f'olá, {nome}! seja bem-vindo!')

nome_digitado = input('digite seu nome')
boas_vindas(nome_digitado)

def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado_soma = soma(5, 3)
print(resultado_soma)