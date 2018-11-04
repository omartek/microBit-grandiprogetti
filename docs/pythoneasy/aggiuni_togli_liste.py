from random import choice

giocatori = ['Harry','Hermione']
nome = input("come ti chiami? ")
print "Ciao " + "come stai " + nome

print("Chi vuoi eliminare? Ecco la lista ", giocatori)

eliminato = input()
giocatori.remove(eliminato)
print(giocatori)
