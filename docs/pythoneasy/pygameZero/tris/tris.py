## TRIS
import pgzrun
import os

WIDTH = 460	# dimesioni della finestra
HEIGHT = 520
manoInCorso = 0 # contatore del numero di mano in corso
manoInCorso_imm = ['simboloo', 'simbolox']  
evidenzia_imm = [(70, HEIGHT-30), (WIDTH-70, HEIGHT-30)] # posizione tasto evidenzia mano in corso

caselle=[]      # lista degli sprite utilizzati
for c_riga in range(3):
    for c_colonna in range(3):
        caselle.append( Actor('casella',(80+c_riga*150, 80+c_colonna*150)) )
caselle.append( Actor('riavvio',(WIDTH/2, HEIGHT-30)) )
caselle.append( Actor('o',(50, HEIGHT-30)) )
caselle.append( Actor('x',(WIDTH-100, HEIGHT-30)) )
caselle.append( Actor('evidenzia',(70, HEIGHT-30)) )
                     
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

def draw():
    screen.clear()
    screen.fill((250,250,250))
    for c_caselle in range(len(caselle)):
        caselle[c_caselle].draw()

def update():
    pass

def on_mouse_down(pos):
    if caselle[9].collidepoint(pos):
        for c_controlla in range (9):
            caselle[c_controlla].image = 'casella'
    else:
        for c_controlla in range (9):   # controlla ognuna delle 9 caselle e ne cambia il simbolo
            if caselle[c_controlla].collidepoint(pos): caselle[c_controlla].image = cambiacasella(caselle[c_controlla].image)

def on_mouse_up(pos):
    pass

def cambiacasella(immagine):
    '''
    Funzione per il cambio del simbolo contenuto nella casella.
    In base al parametro 'immagine' passato ne cambia il contenuto e lo restituisce.
    Se la casella è libera passa la mano al giocatore seguente altrimenti no e aspetta
    un inserimento corretto.
    '''
    global manoInCorso, manoInCorso_imm
    
    if immagine == 'casella':   # se la casella è libera la occupa e passa la mano
        simbolo = manoInCorso%2
        manoInCorso += 1
        caselle[12].pos = evidenzia_imm[manoInCorso%2] 
        return manoInCorso_imm[simbolo]
    elif immagine == manoInCorso_imm[manoInCorso%2]:
        return immagine
    else:
        return immagine
    
def gioco_da_shell():
    tris1 = tris()  # creazione dell'istanza

    ##for lettera in tris1.caselle:
    ##    print (lettera)

    tris1.stampa()  # stampa a video della mano in corso

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


pgzrun.go()
