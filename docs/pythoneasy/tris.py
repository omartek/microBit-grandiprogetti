## TRIS

import os

simbolo = ['X','O']
inserimento = 'Casella non disponibile'

class tris:
    def __init__(self):
        '''
        Inizializzazione di una lista che rappresenta le caselle del Tris e del punteggio.
        '''
        self.caselle=['none','-','-','-','-','-','-','-','-','-']
        self.punteggio = [0,0]

    def stampa(self):
        '''
        Stampa a video delle caselle del Tris con i simboli inseriti dai giocatori fino a questo momento
        '''
        for cont in range(3):
            print (self.caselle[cont*3+1]+self.caselle[cont*3+2]+self.caselle[cont*3+3])

    def inserisci(self,simbolo,pos):
        '''
        Inserimento del simbolo del giocatore nella posizione scelta e stampa delle caselle
        previa verifica che la casella scelta sia libera.

        Attraverso la chiamata al  metodo .vittoria() restituisce il simbolo che vince o la conferma dell'inserimento.
        '''
        if self.caselle[pos] == '-':
            self.caselle[pos] = simbolo
            self.stampa()
            return self.vittoria()
        else:
            return ('Casella non disponibile')

    def vittoria(self):
        '''
        Verifica se qualcuno ha vinto
        '''
        if self.caselle[1] == self.caselle[2] == self.caselle[3] and (self.caselle[1]=='X' or self.caselle[1]=='O'):
            return self.caselle[1]
        if self.caselle[4] == self.caselle[5] == self.caselle[6] and (self.caselle[4]=='X' or self.caselle[4]=='O'):
            return self.caselle[4]
        if self.caselle[7] == self.caselle[8] == self.caselle[9] and (self.caselle[7]=='X' or self.caselle[7]=='O'):
            return self.caselle[7]
        if self.caselle[1] == self.caselle[5] == self.caselle[9] and (self.caselle[1]=='X' or self.caselle[1]=='O'):
            return self.caselle[1]
        if self.caselle[3] == self.caselle[5] == self.caselle[7] and (self.caselle[3]=='X' or self.caselle[3]=='O'):
            return self.caselle[3]
        if self.caselle[1] == self.caselle[4] == self.caselle[7] and (self.caselle[1]=='X' or self.caselle[1]=='O'):
            return self.caselle[1]
        if self.caselle[2] == self.caselle[5] == self.caselle[8] and (self.caselle[2]=='X' or self.caselle[2]=='O'):
            return self.caselle[2]
        if self.caselle[3] == self.caselle[6] == self.caselle[9] and (self.caselle[3]=='X' or self.caselle[3]=='O'):
            return self.caselle[3]
        return('Valore inserito.')
        
os.system('clear')

tris1 = tris()  #creazione dell'istanza

##for lettera in tris1.caselle:
##    print (lettera)

tris1.stampa()  #stampa a video della mano in corso

for giocata in range (9):
    while inserimento == 'Casella non disponibile':
        print('Giocatore', simbolo[giocata%2], 'inserisci la posizione')
        posizione = int(input("Inserisci la posizione: "))
        inserimento = tris1.inserisci(simbolo[giocata%2],posizione)
    if inserimento == 'X':
        print('Ha vinto', inserimento, '!')
        break
    elif inserimento == 'O':
        print('Ha vinto', inserimento, '!')
        break
    else:
        print(inserimento)
    inserimento = 'Casella non disponibile'

print('Finito!')
    
##print(tris1.inserisci('x',1))
##print(tris1.inserisci('x',2))
##print(tris1.inserisci('x',3))

