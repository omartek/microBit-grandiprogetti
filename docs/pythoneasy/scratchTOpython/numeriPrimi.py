import time
t1=time.time() # funzione introdotta per calcolare il tempo impiegato nel calcolo in secondi
t=time.time()-t1 # time.time() restituisce il tempo trascorso dal capodanno del 1970
print(t)

for i in range(2,100):
    primo=False     # variabili di controllo per verificare numero e terminare ciclo
    nonPrimo=False
    
    numero = i      # numero da controllare
    cont = 2        # valore iniziale del contatore
    
    while cont<numero+1 and nonPrimo==False:
      if numero%cont == 0:  # se la divisione è nulla verifichiamo
        if numero==cont:    # se numero e contatore coincidono allora abbiamo un numero_primo
          primo=True
          print(str(numero)+' è primo.')
        else:               # altrimenti no, terminiamo il ciclo
          nonPrimo=True
      cont +=1


t=time.time()-t1
print(t)
    
intervallo=int(input('In quale intervallo vuoi fare la ricerca? '))
t2=time.time()

for i in range(2,intervallo):
    primo=False     # variabili di controllo per verificare numero e terminare ciclo
    nonPrimo=False
    
    numero = i      # numero da controllare
    cont = 2        # valore iniziale del contatore
    
    while cont<numero+1 and nonPrimo==False:
      if numero%cont == 0:  # se la divisione è nulla verifichiamo
        if numero==cont:    # se numero e contatore coincidono allora abbiamo un numero_primo
          primo=True
          print(str(numero)+' è primo.')
        else:               # altrimenti no, terminiamo il ciclo
          nonPrimo=True
      cont +=1

t3=time.time()
t=t3-t2
print(t)
