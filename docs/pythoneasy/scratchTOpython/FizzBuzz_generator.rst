FizzBuzz generator
==================

Esercizio da svolgere
+++++++++++++++++++++

Si deve realizzare un programma che analizza i primi cento numeri e si comporta come descritto di seguito:
* scrive/emette FizzBuzz se è divisibile sia per 3 che per 5
* scrive/emette Fizz se è divisibile solo per 3
* scrive/emette Buzz se è divisibile solo per 5
* altrimenti scrive il valore

In Python il calcolo del resto di una divisione si esegue con l'operatore ``%``::

  for i in range(0,100):
      if i%3==0 and i%5==0:
          print('FizzBuzz')
      elif i%3==0:
          print('Fizz')
      elif i%5==0:
          print('Buzz')
      else:
          print(i)
