Generatore ID/username casuale
==============================

Esercizio da svolgere
+++++++++++++++++++++

Per realzizare il seguente programma servirà:
* creare due liste di nome/aggettivi
* estrarre da ogni lista un valore casuale
* estrarre due numeri ad una cifra casuali
* unire le quattro quantità

::
  from random import randint,choice

  nomi=['omar','mario','alberto','giovanni']
  aggettivi=['alto','basso','lungo','colorato']

  nome_a=choice(nomi)
  nome_b=choice(aggettivi)
  num1=randint(0,9)
  num2=randint(0,9)

  print (nome_a+nome_b+str(num1)+str(num2))

In alternativa si può importare tutta la libreria di moduli ``random`` ed utilizzare il punto per richiamare il modulo necessario::

  import random
  num1=random.randin(0,9)
