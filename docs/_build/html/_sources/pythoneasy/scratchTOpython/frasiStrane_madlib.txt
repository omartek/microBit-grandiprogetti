Storie sciocche
===============

Esercizio da svolgere
+++++++++++++++++++++

Possiamo iniziare scrivendo una storia semplice e poi cercando parole da sostituire. Questa è una sezione leggermente modificata dalla voce Simple English Wikipedia sul gelato

  Il gelato è un dessert surgelato a base di panna, con aggiunta di aromi e dolcificanti. Questa miscela viene rapidamente congelata mentre viene agitata, in modo che non si formino cristalli di ghiaccio grandi. Alcuni gelati sono fatti con carragenina, estratto da alghe, in modo che non sia appiccicoso. Ci sono molti diversi gusti di gelato, come cioccolato e vaniglia. Il gelato spesso ha delle aggiunte per sapore, come gocce di cioccolato, noci o frutta.

Puoi usare questo passaggio per il tuo gioco, se lo desideri, o trovare la tua versione. Ora che abbiamo il testo di base, possiamo sostituire alcune delle parole, come nomi e verbi. Ecco un esempio.

  Il gelato è un dessert surgelato a base di **nome plurale**, con aggiunta di aromi e dolcificanti. Questa miscela viene rapidamente congelata mentre viene **verbo terminate in -ato**, in modo che non si formino **nome plurale**. Alcuni gelati sono fatti con **nome**, estratto da alghe, in modo che non sia **aggettivo**. Ci sono molti diversi gusti di gelato, come **cibo** e **cibo**. Il gelato spesso ha delle aggiunte per insaporire, come **cibo**, **cibo** o **cibo**.

Vediamo ora come usare Python per creare un gioco in stile Mad Libs. L'algoritmo è abbastanza semplice:

#. Chiedi all'utente di inserire alcune parole, come nomi plurali e cibi
#. Assegna questi input alle variabili
#. Inserisci questi valori variabili nelle stringhe per completare il paragrafo.

Passo 1 e 2
++++++++++++
In Python, chiedere all'utente l'input e assegnare il valore a una variabile può essere eseguito in un'unica riga::

  risposta = input('Qual è il senso della vita? ')

Passo 3
++++++
È quindi possibile utilizzare questa variabile in un'istruzione di stampa utilizzando la semplice concatenazione di stringhe::

  print('I senso della vita è ' + risposta + '.')

Quindi, per rendere il gioco Mad Libs, puoi iniziare chiedendo all'utente un carico di parole, e finiscilo inserendole in alcune stringhe che verranno stampate.

Ecco il codice per un programma Python completo, e qui sotto c'è una versione di Trinket che puoi testare::

  nome_1 = input('Dammi un nome di cosa plurale ')
  verbo = input('Dammi un verbo terminante in -ato ')
  nome_2 = input('Dammi un altro nome di cosa plurale ')
  nome_3 = input('Dammi un nome di cosa ')
  aggettivo = input('Dammi un aggettivo')
  cibo_1 = input('Dammi un cibo')
  cibo_2 = input('Dammi un altro cibo')
  nome_4 = input('Dammi un nome di cosa ')
  nome_5 = input('un altro ancora ')
  nome_6 = input('e un ultimo ancora.')

  print('Il gelato è un dessert surgelato a base di ' + nome_1 + ', con aggiunta di aromi e dolcificanti.')
  print('Questa miscela viene rapidamente congelata mentre viene ' + verb + ', in modo che non si formino ' + nome_2)
  print('Alcuni gelati sono fatti con ' + nome_3 + ', estratto da alghe, in modo che non sia ' + aggettivo + '.')
  print('Ci sono molti diversi gusti di gelato, come ' + cibo_1 + ' e ' + cibo_2+ '.')
  print('Il gelato spesso ha delle aggiunte per insaporire, come ' + nome_4 + ', ' + nome_5 + ' o ' + nome_6 + '.')

Prova a riprodurre questo programma in Scratch!
