Carta Forbice sasso
===================

Si vuole realizzare un gioco in cui il computer esegue una sfida tra due giocatori.
Il pc estrae valori casuali per i tre simboli disponibili ed esegue un confronto per calcolare il vincitore.

Questi i simboli disegnati con caratteri ASCII:

**Carta**::

  _____
 |     |
 |     |
 |_____|

**Forbice**::

  \  /
   \/
   /\
  o  o

**Sasso**::

    _
   ( )
  (___)


Prima fase
----------
Iniziare la programmazione scrivendo una struttura base del codice che poi completeremo in passaggi successivi.
Il codice inizialmente sarà così strutturato:

* **import** azione dei moduli **randint** e **sleep** per estrarre numeri casuali e rallentare l'esecuzione dell'estrazione::

   from random import randint
   from time import sleep

* creazione della lista **carte[][]** contenente i disegni ASCII, tre disegni separati su quattro linee::

   carte=[[" _____ ","|     |","|     |","|_____|"],
          ["\  /"," \/ "," /\\ ","o  o"],
          ["     ","  _  "," ( ) ","(___)"]]

* estrazione di due valori casuali con **randint(0,2)**::

   plA=randint(0,2)
   plB=randint(0,2)

* verifica tra i valori estratti per determinare il vincitore. La verifica deve essere eseguita tre volte. Ai valori **0,1,2** corrispondo i tre simboli ::

   if plA==0:
       if plB==0:
           print("Patta")
       elif plB==1:
           print("Vince plB")
       else:
           print("Vince plA")

Seconda fase
------------

In seguito aggiungeremo le istruzioni per far comparire i due simboli scelti::

   for riga in range(4):
        print(carte[plA][riga])

   print()

   for riga in range(4):
        print(carte[plB][riga])

.. _variabili:

e le variabili necessarie a memorizzare i nomi dei giocatori e il punteggio::

  plA_nome="Omar"
  plA_punteggio=0

  plB_nome="Sabrina"
  plB_punteggio=0

In seguito a ciò, i
l codice che esegue la verifica deve essere aggiornato inserendo le variabili appena create::

  if plA==0:
    if plB==0:
        print("Patta")
    elif plB==1:
        print("Vince "+plB_nome)
        plB_punteggio += 1
    else:
        print("Vince "+plA_nome)
        plA_punteggio += 1

Se non si inserisce il codice dentro un ciclo che lo ripeta più volte, la partita verrà giocata una sola volta.

Dopo la definizione delle variabili_ aggiungere quindi un contatore, selezionare il codice ed indentarlo premendo TAB::

  for count in range(100):
    sleep(1) #pausa inserita per permettere la visualizzazione delle singole mani
    .....
    .....
    else:
        print("Vince "+plA_nome)
        plA_punteggio += 1

Il programma termina visualizzando il punteggio totale::

    print("Punteggio totale: ")
    print(plA_nome+" : "+str(plA_punteggio))
    print(plB_nome+" : "+str(plB_punteggio))

Aggiungere le seguenti istruzioni se si vuole che la shell venga pulita dopo ogni mano::

    import os
    os.system("clear")

Terza fase
----------

Aggiungere un'animazione che mostra il mescolamento delle carte.

Quarta fase
-----------

Introdurre l'impiego degli oggetti per la creazione di giocatori e relative proprietà.

.. raw:: html

 <iframe src="https://trinket.io/embed/python/d9fe76d76b" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


