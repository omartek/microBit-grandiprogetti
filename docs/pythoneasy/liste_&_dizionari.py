#
# LISTE: operazioni sulle liste
#
lista=[]
print (lista)
lista.append(3)
print (lista)
for cont in range(8):
    lista.append(cont)
print(lista)

# elimina il primo valore corrispondente
lista.remove(3)
print(lista,len(lista))

# elimina il secondo elemento della lista
del lista[1]
print(lista,len(lista))

del lista[1]
print(lista,len(lista))

# clona il contenuto di una lista
# se si utilizza solo l'uguale si ottiene un alias non una nuova variabile
lista2=lista[:]
print ("lista2:",lista2)

del lista[0]
print (lista)
print (lista2)

#
# DIZIONARI
#

Eng2Ita = {}
Eng2Ita['one'] = 'uno'
Eng2Ita['two'] = 'due'

print (Eng2Ita['one'])
print (Eng2Ita.keys())
print (Eng2Ita.values())
print (Eng2Ita.items())





