Gioco di carte: 7 e mezzo
=========================

.. contents:: Indice
  :depth: 1
  :local:

.. note::
:download:`File .odp con slide del progetto <./file/7eMEZZO.odp>`
:download:`File .pdf del progetto <./file/7eMEZZO.pdf>`
`Google slides <https://docs.google.com/presentation/d/1hQcIxclsxsYGWUUAe2GRT9Ng8iuPFZZ-gmwNeYFR9Ns/edit?usp=sharing>`_

Preparare variabili, liste e valori costanti (le carte)
-------------------------------------------------------

1. CREA LE **VARIABILI** E LE **LISTE** NECESSARIE AL PROGETTO SCRATCH.

.. image:: ./images/7emezzo/7emezzo_01.png

2. E INSERISCI IL **CODICE** CHE ALL’INIZIO LE INIZIALIZZA A ZERO.

.. image:: ./images/7emezzo/7emezzo_02.png

3. LA **LISTA CARTE** VA COMPILATA A MANO CON LE 10 CARTE USANTE NEL GIOCO.

.. image:: ./images/7emezzo/7emezzo_03.png

Creare il codice che estrae  memorizza le carte
-----------------------------------------------

4. USANDO IL BLOCCO **RIPETI FINO A QUANDO**, IL GIOCO PROCEDE E VENGONO ESTRATTE DUE CARTE: UNA PER IL PC E UNA PER IL **GIOCATORE**.
IL NUMERO ESTRATTO VIENE SALVATO NELLE VARIABILI (AD OGNI TURNO IL NUOVO VALORE ESTRATTO SOSTITUISCE IL VECCHIO).

.. image:: ./images/7emezzo/7emezzo_04.png

5. I VALORI ESTRATTI VENGONO LETTI USANDO IL COMANDO **DIRE** ED I VALORI VENGONO SALVATI NELLA **LISTA** CHE CONTIENE TUTTE LE CARTE ESTRATTE DEI GIOCATORI.

.. image:: ./images/7emezzo/7emezzo_05.png

6. LA VARIABILE **CONTAT_CARTE** È UN CONTATORE PER RICORDARE QUANTE CARTE SONO STATE ESTRATTE E SERVIRÀ A FAR APPARIRE LA n-ESIMA CARTA DEL MAZZO.

.. image:: ./images/7emezzo/7emezzo_06.png

7. AL TERMINE DELLA MANO IL PROGRAMMA CHIEDE AL GIOCATORE SE VUOLE ANCORA UNA CARTA. SE PENSA DI AVER VINTO RISPONDE **NO** E VERRÀ ESTRATT ANCORA UNA SOLA CARTA PER IL GIOCATORE **PC** CHE A QUESTO PUNTO AVRÀ VINTO O PERSO, MA VERIFICARSI ANCHE UN PAREGGIO...

.. image:: ./images/7emezzo/7emezzo_07.png

8. AGGIUNGERE I COMANDI PER L’ULTIMA ESTRAZIONE ALDIFUORI DEL CICLO **RIPETI FINO A QUANDO**.

.. image:: ./images/7emezzo/7emezzo_08.png

Creare le carte e gestire la loro comparsa
------------------------------------------

9. CREARE UNO SPRITE CON **10 COSTUMI** ED IL CODICE PER FAR APPARIRE LA CARTA GIUSTA (vedi la prossima slide) E SOLO AL TERMINE DUPLICHIAMO 5 VOLTE LO SPRITE.

.. image:: ./images/7emezzo/7emezzo_09.png

10. LO SPRITE CARTA ESEGUE LE SEGUENTI ISTRUZIONI:
  * ALL’INIZIO DEL GIOCO LA CARTA NON È VISIBILE
  * QUANDO VIENE ESTRATTA UNA CARTA VIENE INVIATO UN MESSAGGIO
  * AL PRIMO TURNO SOLO LA PRIMA CARTA (SE **CONTAT_CARTE=1**) SI MOSTRA CON IL COSTUME DEL NUMERO DELLA CARTA ESTRATTA.

.. image:: ./images/7emezzo/7emezzo_10.png
.. image:: ./images/7emezzo/7emezzo_11.png

11. LE CARTE DEL GIOCATORE UMANO HANNO UN CODICE MOLTO SIMILE.

.. image:: ./images/7emezzo/7emezzo_12.png
.. image:: ./images/7emezzo/7emezzo_13.png
