Come utilizzare un Joypad con Scratch
=====================================

Preparare variabili, liste e valori costanti (le carte)
-------------------------------------------------------

#. CREA LE **VARIABILI** E LE **LISTE** NECESSARIE AL PROGETTO SCRATCH.

.. image:: ./images/7emezzo/7emezzo_01.png

#. E INSERISCI IL **CODICE** CHE ALL’INIZIO LE INIZIALIZZA A ZERO.

.. image:: ./images/7emezzo/7emezzo_02.png

#. LA **LISTA CARTE** VA COMPILATA A MANO CON LE 10 CARTE USANTE NEL GIOCO.

.. image:: ./images/7emezzo/7emezzo_03.png

Creare il codice che estrae  memorizza le carte
-----------------------------------------------

#. USANDO IL BLOCCO **RIPETI FINO A QUANDO**, IL GIOCO PROCEDE E VENGONO ESTRATTE DUE CARTE: UNA PER IL PC E UNA PER IL **GIOCATORE**.
IL NUMERO ESTRATTO VIENE SALVATO NELLE VARIABILI (AD OGNI TURNO IL NUOVO VALORE ESTRATTO SOSTITUISCE IL VECCHIO).

.. image:: ./images/7emezzo/7emezzo_04.png

#. I VALORI ESTRATTI VENGONO LETTI USANDO IL COMANDO **DIRE** ED I VALORI VENGONO SALVATI NELLA **LISTA** CHE CONTIENE TUTTE LE CARTE ESTRATTE DEI GIOCATORI.

.. image:: ./images/7emezzo/7emezzo_05.png

#. LA VARIABILE **CONTAT_CARTE** È UN CONTATORE PER RICORDARE QUANTE CARTE SONO STATE ESTRATTE E SERVIRÀ A FAR APPARIRE LA n-ESIMA CARTA DEL MAZZO.

.. image:: ./images/7emezzo/7emezzo_06.png

#. AL TERMINE DELLA MANO IL PROGRAMMA CHIEDE AL GIOCATORE SE VUOLE ANCORA UNA CARTA. SE PENSA DI AVER VINTO RISPONDE **NO** E VERRÀ ESTRATT ANCORA UNA SOLA CARTA PER IL GIOCATORE **PC** CHE A QUESTO PUNTO AVRÀ VINTO O PERSO, MA VERIFICARSI ANCHE UN PAREGGIO...

.. image:: ./images/7emezzo/7emezzo_07.png

#. AGGIUNGERE I COMANDI PER L’ULTIMA ESTRAZIONE ALDIFUORI DEL CICLO **RIPETI FINO A QUANDO**.

.. image:: ./images/7emezzo/7emezzo_08.png

Creare le carte e gestire la loro comparsa
------------------------------------------

#. CREARE UNO SPRITE CON **10 COSTUMI** ED IL CODICE PER FAR APPARIRE LA CARTA GIUSTA (vedi la prossima slide) E SOLO AL TERMINE DUPLICHIAMO 5 VOLTE LO SPRITE.

.. image:: ./images/7emezzo/7emezzo_09.png

#. LO SPRITE CARTA ESEGUE LE SEGUENTI ISTRUZIONI:
  * ALL’INIZIO DEL GIOCO LA CARTA NON È VISIBILE
  * QUANDO VIENE ESTRATTA UNA CARTA VIENE INVIATO UN MESSAGGIO
  * AL PRIMO TURNO SOLO LA PRIMA CARTA (SE **CONTAT_CARTE=1**) SI MOSTRA CON IL COSTUME DEL NUMERO DELLA CARTA ESTRATTA.

.. image:: ./images/7emezzo/7emezzo_10.png
.. image:: ./images/7emezzo/7emezzo_11.png

#. LE CARTE DEL GIOCATORE UMANO HANNO UN CODICE MOLTO SIMILE.
.. image:: ./images/7emezzo/7emezzo_12.png
.. image:: ./images/7emezzo/7emezzo_13.png
