musicas = [
    ['november rain', 'guns´n roses'],
    ['breath', 'pink floyd'],
    ['6 sinf', 'beethoven']
]

for musica in musicas:
    for info in musica:
        print(info)
    print()

matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

for numero in matriz:
    print(numero)


import random

num = int(input('digite um numero maior que 0 :'))
vetor = [random.random() for _ in range(num)]

for num in vetor:
    print(num)

n = int(input("Digite a quantidade de alunos: "))

notas = []
for i in range(n):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

media = sum(notas) / n

iguais = acima = abaixo = 0

for nota in notas:
    if nota == media:
        iguais += 1
    elif nota > media:
        acima += 1
    else:
        abaixo += 1

print("Média:", media)
print("Iguais à média:", iguais)
print("Acima da média:", acima)
print("Abaixo da média:", abaixo)
