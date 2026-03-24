vetor = [5, 8, 2, 10, 3, 7, 1, 9, 4, 6]
impar, pares = [], []
totalImpar, totalPares = 0, 0
maior = vetor[0]
menor = vetor[0]
soma = 0

for numero in vetor:
    soma += numero
    if numero > maior:
        maior = numero
    if numero < menor:
            menor = numero
    if numero % 2 == 1:
        totalImpar += 1
        impar.append(numero)
    else:
        totalPares += 1
        pares.append(numero)




media = soma / len(vetor)


print('maior valor:', maior)
print('menor valor:', menor)
print('soma:', soma)
print('media:', media)
print('total de impares:', totalImpar)
print('total de pares:', totalPares)
print('pares:', pares)
print('impares:', impar)