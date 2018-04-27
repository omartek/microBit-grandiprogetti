Giocare con le stringhe
=======================

Di seguito vengono illustrati i metodi esistenti in Python per manipolare le stringhe. Per utilizzarli basta aggiungere un **.** alla stringa seguito dal metodo voluto. Guarda l'insieme dei metodi a `quest'indirizzo <https://docs.python.org/release/2.5.2/lib/string-methods.html>`_

Separare in base ad un carattere
++++++++++++++++++++++++++++++++

Creare una lista da un elenco diviso da spazi::

  vowels = "a e i o u"
  list_of_vowels = vowels.split() # crea una lista di vocali
  print(list_of_vowels)

  vowels = "a,e,i,o,u"
  list_of_vowels = vowels.split(',')
  print(list_of_vowels)

Rendere tutto minuscolo/MAIUSCOLO
+++++++++++++++++++++++++++++++++

::

  angry = 'THIS IS SOME TEXT'
  calm = angry.lower()
  print(calm)

Sostituire una parola
+++++++++++++++++++++

::

  original = 'I wandered lonely as a cloud'
  new_1 = original.replace('cloud', 'clown')
  new_2 = new_1.replace('wandered', 'juggled')
  new_3 = new_2.replace('lonely', 'madly')
  print(original)
  print(new_1)
  print(new_2)
  print(new_3)
