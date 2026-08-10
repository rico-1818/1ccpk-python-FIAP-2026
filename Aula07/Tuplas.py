t = ('a', 'b', 'c', 'd', 'e')
print(t[0])

t1 = 'a',
print(type(t1))

t = tuple()

t = tuple('texto')
print(t[0])
print(t[1:3])


#como tuplas são imutaveis
t = ('T', ) + t[1:]
print(t)

#atribuição de tuplas
#trocar a com b


a = b
b = temp
print(f'a: {a}, b: {b}')

a = 5
b = 10
print(f'a: {a}, b: {b}')

a, b = b, a
print(f'a: {a}, b: {b}')

#separação de email

email = 'user@gmail.com'
username, domain = email.split('@')

print(username, domain)

