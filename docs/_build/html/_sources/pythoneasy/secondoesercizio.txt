Esercizi con i numeri
=====================

Calcoli con la **shell** di Python
----------------------------------
Semplici calcoli e operatori in Python::

  3+5
  3+5*2
  (3+5)*2     # cosa cambia?
  10/7
  10%7        # cosa è questo risultato?
  a*2         # dà errore! a non è definita. Il PC non conosce il valore di a
  a=3         # allora diciamoglielo
  a*2         # ora funziona!


Primo esercizio: i numeri binari
--------------------------------

Il computer rapprenta qualunqeu informazione mediante numeri binari. Per vedere il valore di un numero in binario si può utilizzare quest'istruzione::

  print (bin(1234))
  bin(4)      # il computer però calcola usando i numeri binari
  bin(20)     # eccone alcuni
  bin(1+1)    # quanto fa 1+1?
  int(0b10)   # come convertire un binario in decimale
  ord('a')    # e anche le parole sono numeri
  chr(97)     # esegue la trasformazione inversa

Primo esercizio: le moltiplicazioni
-----------------------------------

Scriviamo un semplice moltiplicazione::

  print (3*5);
  print (4*5);

E una serie di moltiplicazioni::

  # tabelline
  for a in range(0,11):
    for b in range(0,11):
      print (a,'*',b,'=',a*b)
