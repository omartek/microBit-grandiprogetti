#!/bin/python3

from random import choice, randint
import os

os.system("clear")

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

N_squadre = int(input("Quante squadre vuoi?"))
N_giocatori = int(input("Quanti giocatori per squadra?"))

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

# verifica che ci sia un numero di giocatori sufficiente
if len(giocatori) < (N_squadre * N_giocatori):
  print("I giocatori non sono sufficienti")
  teamA.append("None")
else:
  for count_s in range(N_squadre):
    for count_g in range(N_giocatori):
      giocatore_n = choice(giocatori)
      teamA.append(giocatore_n)
      giocatori.remove(giocatore_n)

# estrazione dei nomi per due squadre se ci sono nomi sufficienti
if len(nomiTeam_import) < N_squadre:
  print("Nomi squadre non sufficienti")
  teamNomi.append("None")
else:
  for count_t in range(N_squadre):
    nome_random = choice(nomiTeam_import)
    # verifica che il secondo nome estratto non sia uguale al primo
    while nome_random in teamNomi:
      nome_random = choice(nomiTeam_import)
    teamNomi.append(nome_random)

print(len(teamA))
print(len(teamNomi))

# se squadre e giocatori sono state formate vengono visualizzate e salvate
if len(teamA)==N_squadre*N_giocatori and len(teamNomi)==N_squadre:
  print ("Nomi estratti", teamNomi)
  print ("Ecco le squadre.")

  # stampa e video e salva su file: nome squadra e componenti
  squadra_N = 0
  for squadra in teamNomi:
    print ("Team", squadra)
    file.write(squadra + "\n")
    for count in range(N_giocatori):
      print ("Giocatore n.", str(count+1), teamA[squadra_N*N_giocatori + count])
      file.write(teamA[squadra_N*N_giocatori + count] + "\n")
  squadra_N += 1
else:
  print("Non è stato possibile formare le squadre.")

# salvataggio su file dell'estrazione
#for i in range(len(teamA)):
#  file.write(teamA[i] + "\n")

file.close()

# ToDo
# creare una classe per creare le squadre
# creare una lista di squadre


