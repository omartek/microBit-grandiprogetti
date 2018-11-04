Laboratorio Python
==================

Qui trovi la versione .odt e .pdf
:download:`File .odt <./laboratorioPython/pythonLab_per_stampare.odt>`.

:download:`File .pdf <./laboratorioPython/pythonLab_per_stampare.pdf>`.

Avviare IDLE3

Comandi da shell
-----------------

Comandi da **shell** per calcolare ::

  3+5
  3+5*2
  (3+5)*2     # cosa cambia?
  10/7
  10%7        # cosa è questo risultato?
  a*2         # dà errore! a non è definita. Il PC non conosce il valore di a
  a=3         # allora diciamoglielo
  a*2         # ora funziona!
  bin(4)      # il computer però calcola usando i numeri binari
  bin(20)     # eccone alcuni
  bin(1+1)    # quanto fa 1+1?
  int(0b10)   # come convertire un binario in decimale
  ord('a')    # e anche le parole sono numeri
  chr(97)     # esegue la trasformazione inversa

Comandi da **shell** per scrivere ::

  print ciao            # dà errore! dice che servono le parentesi
  print('ciao')
  nome='pippo'          # cosa succede se dico questo
  print('ciao',nome)    # e poi scrivo questa istruzione?
  print(a,'*2='',a*2)   # e questa?
  for i in range(11):   # scriviamo le tabelline
    2*i

Comandi da **editor** di codice
-------------------------------
Dal menù file scegliere ``New File`` (Ctrl+N).
Usando l'editor si possono inserire molte istruzioni ed
eseguirle tutte insieme.
Preme ``F5`` per salvare il file e premerlo ogni volta che si vogliono eseguire le istruzioni.

L'istruzione ``print`` serve a scrivere a video::

  print('ciao') # scrivo una volta 'ciao'

Aggiungi una seconda istruzione identica::

  print('ciao') # scrivo due volte 'ciao'
  print('ciao')

Se voglio scriverlo tante volte è meglio se gli faccio fare la conta::

  for a in range(20): # per a conta che fino a 20
    print('ciao')     # scrivo ogni volta 'ciao'

E se voglio fargli scrivere un nome diverso::

  for i in range(20):
    print(nome)    # come visto prima il pc non sa il mio nome... non funziona

Prima bisogna dirgli il **nome** qual è::

  nome='pippo'
  for i in range(20):
    print(nome)    # adesso funziona!!!

Però il PC sa anche fare delle domande. Come? Con l'istruzione ``input``::

  nome=input('Come ti chiami? ')
  for i in range(20):
    print(nome)    # funziona!!!

Ora convertiamo le lettere del nome in numeri::

  nome=input('Come ti chiami? ')
  for i in nome:
    print(i)           # scrive una lettera alla volta

  nome=input('Come ti chiami? ')
  for i in nome:
    print(ord(i))    # scrive una lettera alla volta in numero

  nome=input('Come ti chiami? ')
  for i in nome:
    print(chr(ord(i)+2))    # scrive una lettera alla volta in numero
