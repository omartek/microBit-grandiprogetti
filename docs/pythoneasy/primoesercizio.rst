Esercizi con le stringhe: print e ripetizioni
====================================================

Prima istruzione di scrittura a video (output standard)
------------------------------------------------------------
Inseriamo la nostra prima istruzione che invia al monitor (standard I/O) di visualizzare una stringa di caratteri::

 print ("Ciao")

Ciclo infinito:
mentre la condizione è vera esegui il comando **indentato**::

  while True:
    print("Ciao")

Interrompi premendo Ctrl+x

Crea una variabile contenente qualcosa tipo **Ciao**::

 frase="Ciao"

Ora visualizza i singoli caratteri::

  frase[0]
  frase[1]
  frase[3]
  frase[4]

Anche in ordine inverso::

  print (frase[0])
  print (frase[1])
  print (frase[2])
  print (frase[3])
  print (frase)

Usiamo ora un ciclo per compiere la stessa operazione::

 for i in range (4):
  print frase[3-i]

Utilizzando il comando ``len(frase)`` si ottiene la lunghezza della stringa::

  for i in range(len(frase)):
    print frase[len(frase)-1-i]

Esercizi di inversione e codifica di stringhe di testo
------------------------------------------------------

Faciamo un'animazione ASCII. Per impostare una velocità serve la libreria ``time`` che contiene la funzione ``sleep``::

  #ASCII animati
  import time

  frase="ciao"

  while 5>3:          #fintantochè si verifica la condizione
  print("->")         #e cioè per sempre
  time.sleep (0.2)    #si potrebbe usare la costante True
  print("-->")
  time.sleep (0.2)
  print("--->")
  time.sleep (0.2)
  print("---->")
  time.sleep (0.2)
  print("----->")
  time.sleep (0.2)
  print("---->")
  time.sleep (0.2)
  print("--->")
  time.sleep (0.2)
  print("-->")
  time.sleep (0.2)
  print("-->")

Visualizzare il contenuto di una lista di stringhe::

  frase=["ciao","tutto bene","sto bene"]
  for i in frase:
  print (i)

Codificare sostituendo le vocali::

  # sostituire le vocali
    frase="ciao"
    for i in frase:
    if i=="a":
      print ("8")
    elif i=="e":
        print ("5")
    elif i=="i":
        print ("3")
    elif i=="o":
      print ("2")
    elif i=="e":
      print ("9")
    else:
      print (i)

O sostituendo tutte le lettere::

  # conversione in ascii
  frase="ciao"

  for i in frase:
    print (ord(i))

  # conversione in ascii con incremento
  frase="ciao"
  chiavesegreta=4;

  for i in frase:
  print (chr(ord(i)+chiavesegreta))

Acquisizione dati tramite INPUT
-------------------------------

Per ottenere informazione dall'utente si memorizza una stringa dentro una variabile utilizzando il comando ``ìnput``::

  nome=input("Come ti chiami? ")
  while True:
    print("Ciao ",nome)
  print(type(nome))

.. note::
  Questa è una nota.

.. warning::
  Questo è un warning.
