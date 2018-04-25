Creare una lista di nomi da una stringa
=======================================

Data un elenco di nomi separati da virgola, creare una lista, ordinarla ed estrarre un nome a caso::

  from random import choice

  nomi='omar,alberto,gianni'
  lista_nomi=nomi.split(',')

  print(lista_nomi)
  print(choice(lista_nomi))

Se vuoi puoi chiedere l'inserimento dell'elenco::

  nomi=input('inserisci i nomi separati da virgole')
