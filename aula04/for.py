for count_music in range(3):
     print(f'musica {count_music}')

# #de 1 ate 11, pulando de 2 em 2
for i in range(1, 12, 2):
     print(i)

#atividade 3
qtd_musica = int(input('digite a quanidade de musica que voce tem na playlist (DB) : '))

for i in range(qtd_musica):
    print(f'musica {i}')

for i in range(0, 4):
    for j in range(0, 3, 2):
        print(f'i: {i}, j: {j}')