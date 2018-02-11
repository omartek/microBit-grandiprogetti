Primo esercizio
===============

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
  frase[5]

Usiamo un ciclo numerato::

 for i in range (4):
  print frase[3-i]

Utilizzando il comando ``len(frase)`` si ottiene la lunghezza della stringa::

  for i in range(len(frase)):
    print frase[len(frase)-1-i]


.. note::
  Questa è una nota.

.. warning::
  Questo è un warning.
