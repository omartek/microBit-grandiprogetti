Ricerca dei numeri primi
========================

Esercizio da svolgere
+++++++++++++++++++++

Scivere un programma per la ricerca dei numeri primi contenuti nei primi n.

Per verificare se un numero è primo devi controllare che sia divisibile solo per se stesso ed 1.

::

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

La verifica si ferma a 100. Se si vuole eseguire la ricerca su un intervallo più grande aggiungere le istruzioni di input necessari::

  intervallo=int(input('In quale intervallo vuoi fare la ricerca? '))

  for i in range(2,intervallo):  # è quindi si procede con lo script di cui sopra
