from random import choice

nomi='omar,alberto,gianni'
lista_nomi=nomi.split(',')
print(lista_nomi)
lista_nomi.sort()

print(lista_nomi)

print(choice(lista_nomi))
