Esercizio iniziale
==================

.. toctree::
   :maxdepth: 1
   :caption: Progetti Scratch to Pyhton

   calcola_età_cane.rst
   FizzBuzz_generator.rst
   frasiStrane_madlib.rst
   generatore_Username_casuale.rst
   lista_da_elenco_nomi.rst
   numeriPrimi.rst

Assegnazione di variabili::

  valore = 10
  frase = 'questa è una frase'
  valore = valore + 10
  valore += 10 #equivalente alla precedente

Comandi di output::

  print (valore)
  print (frase)
  print ('Ciao')

Cicli condizionali o per sempre::

  while valore < 10: # termina a condizione non più vera
    print(valore)
    valore += 1

  while True: # ciclo per sempre
    print(frase)

  if valore < 10: # la verifica viene eseguita una volta sola
    print('valore è minore di 10')
  elif valore < 20:
    print('valore è minore di 20 ma non di 10')
  elif valore == 20:
    print('valore è uguale a 20')

Ciclo for::

  nome = 'mario'
  for i in nome: # stampa le lettere di mario
    print (i)
  for a in range(0,9):
    print (a)
  for a in range(0,9):
    print (str(a) + nome) # convertire se si vogliono unire tipi diversi

Assegnazione di liste e utilizzo dei suoi metodi (elenchi di valori)::

  lista1 = ['uno','due','tre']
  lista1.append('quattro')
  lista1.pop(0) # elimina il primo elemento della lista

Estrazione di valori casuali::

  from random import randint, choice # importare il modulo necessario
  valoreCasuale=randint(1,10) # estrarre numeri
  estraiCarta=choice(lista1) # estrarre da una lista

Input::

  nome = input('Come ti chiami? ')
  print ('Ciao '+nome+'. Come stai?')

Ricorda che non si possono unire entità di natura diversa (testo con numeri per esempio), è necessaria prima una conversione.
Conversione di numero in testo e viceversa::

  anni = input('Quanti anno hai? ')
  print (str(anni)+' anni non sono molti')
