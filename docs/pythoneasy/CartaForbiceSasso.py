from random import randint
from time import sleep
import os

## carta
## _____
##|     |
##|     |
##|_____|
##
## forbici
## \  /
##  \/
##  /\
## o  o
##
## sasso
##   _
##  ( )
## (___)

os.system("clear")

def mescola():
    """ Esegue un'animazione di mescolamento delle carte"""
    ## alterna 30 disegni
    for mescolateN in range(30):
        cartacasuale=randint(0,2)
        for carta_rigaN in range(4):
            print(carte[cartacasuale][carta_rigaN])
        print("")
        cartacasuale=randint(0,2)
        for carta_rigaN in range(4):
            print(carte[cartacasuale][carta_rigaN])
        sleep(0.1)
        os.system("clear")

def mescola_cartaN(cartaestratta):
    """
    Esegue due animazioni di mescolamento delle carte
    Prima viene estratta una carta ed in seguito la seconda
    """
    ## alterna 30 disegni
    for mescolateN in range(10):
        for count in range(3):
            cartacasuale=count
            if cartaestratta!=10:
                cartacasuale=cartaestratta
            stampaCarta(cartacasuale)
            print("")
            cartacasuale=count
            stampaCarta(cartacasuale)
            sleep(0.05)
            os.system("clear")
        
def stampaCarta(carta_N):
    """ Stampa a  video una singola carta"""
    for carta_rigaN in range(4):
        print(carte[carta_N][carta_rigaN])

##grafica ASCII delle carte
carte=[[" _____ ","|     |","|     |","|_____|"],
       ["\  /"," \/ "," /\\ ","o  o"],
       ["     ","  _  "," ( ) ","(___)"]]

##definizione varibaili dei giocatori
plA_nome="Omar"
plA_punteggio=0
plB_nome="Sabrina"
plB_punteggio=0

##inizio ciclo principale: estrazione delle mani, grafica ASCII, verifica vincitore
for count in range(10):
    ##estrazione casuale delle carte
    plA=randint(0,2)
    plB=randint(0,2)
    os.system("clear")
    ##ciclo delle animazioni
    mescola_cartaN(10)
    mescola_cartaN(plA)
      
    stampaCarta(plA)
    print("")
    stampaCarta(plB)

    if plA==0:
        if plB==0:
            print("Patta")
        elif plB==1:
            print("Vince "+plB_nome)
            plB_punteggio += 1
        else:
            print("Vince "+plA_nome)
            plA_punteggio += 1

    if plA==1:
        if plB==1:
            print("Patta")
        elif plB==2:
            print("Vince "+plB_nome)
            plB_punteggio += 1
        else:
            print("Vince "+plA_nome)
            plA_punteggio += 1

    if plA==2:
        if plB==2:
            print("Patta")
        elif plB==0:
            print("Vince "+plB_nome)
            plB_punteggio += 1
        else:
            print("Vince "+plA_nome)
            plA_punteggio += 1
    sleep(1)

print("Punteggio totale: ")
print(plA_nome+" : "+str(plA_punteggio))
print(plB_nome+" : "+str(plB_punteggio))
