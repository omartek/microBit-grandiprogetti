#!/bin/python3

from random import choice, randint

# apertura salvataggio del contenuto del file nomi.txt in una lista
file = open("nomi.txt", "r")
giocatori=[]
giocatori = (file.read().splitlines())
file.close()

# apertura salvataggio del contenuto del file nomiTeam.txt in una lista
file = open("nomiTeam.txt", "r")
nomiTeam_import=[]
nomiTeam_import = (file.read().splitlines())
file.close()

# creazione di un file per la scrittura 'w' o 'a'
file = open("store.txt", "w")

N_squadre = str(input("Quante squadre vuoi?"))
N_giocatori = str(input("Quanti giocatori per squadra?"))

# verifica del contenuto delle liste create
print ("Ecco i Team:\n", nomiTeam_import, "\n")
print ("Ecco i giocatori:\n", giocatori, "\n", len(giocatori))

# verifica della presenza di un valore
# verifica_nome = input("Dimmi un nome da verificare: ")
# if verifica_nome in giocatori:
#   print ("La posizione è", giocatori.index(verifica_nome))
# else:
#   print ("Nome non presente nella lista.")
    
teamNomi = []
teamA = []
teamB = []

# verifica numero di giocatori sufficiente
# if len(giocatori)<
while len(giocatori)>0:
  giocatoreA = choice(giocatori)
  teamA.append(giocatoreA)
  giocatori.remove(giocatoreA)
  
  # controllo inserito per le liste di giocatori dispari
  if giocatori == []:
    break
  
  giocatoreA = choice(giocatori)
  teamB.append(giocatoreA)
  giocatori.remove(giocatoreA)

# estrazione dei nomi per due squadre
nome_random = choice(nomiTeam_import)
teamNomi.append(nome_random)
# verifica che il secondo nome estratto non sia uguale al primo
while nome_random in teamNomi:
  nome_random = choice(nomiTeam_import)
teamNomi.append(nome_random)

print ("Nomi estratti", teamNomi)
print ("Ecco le squadre.")
print ("Team",teamNomi[0], teamA)
print ("Team ",teamNomi[1], teamB)

# salvataggio su file dell'estrazione
for i in range(len(teamA)):
 file.write(teamA[i] + "\n")

file.close()

# ToDo
# inserire un numero elevato di giocatori da distribuire in un numero
# di squadre a scelta
# Salvare tutto su file


