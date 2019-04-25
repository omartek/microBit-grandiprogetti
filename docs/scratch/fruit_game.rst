Fruit Game
==========

Prerequisiti
------------

Saper disegnare con il computer (utilizzo di Paint): Scratch ha al suo interno uno strumento per disegnare simile a Paint. Saper cercare immagini in Internet e manipolare fotografie/immagini.

Esercizio
---------

Il gatto deve mangiare la frutta che scende dal cielo ed evitare la bomba. Il gatto ha tre vite a disposizione.

Concetti di programmazione veicolati
------------------------------------

Inizializzazione, sincronizzazione, uso delle variabili.

**Soluzione**

Con questo gioco si imparano ad usare diversi nuove istruzioni.
L’istruzione per generare un numero casuale per far si che i frutti cadano da posizioni sempre diverse e con tempi di comparsa differenti.
Anche la velocità di caduta degli oggetti è diversa, questa si può ottenere facendo compiere un numero diverso di passi ai diversi sprite.
L’istruzione ripeti fino a quando viene presentata con una condizione composta: sto toccando il colore del terreno oppure sto toccando il gatto. Questa condizione è soddisfatta quando o il frutto tocca il terreno oppure tocca il gatto ma potrebbe anche essere che vi sia la contemporaneità degli eventi ovvero che tocca il gatto ed il terreno contemporaneamente.
Quando il gatto perde tutte e tre le vite è necessario far comparire la dicitura Game Over e quindi fermare il gioco. Questo è possibile utilizzando una sincronizzazione tramite messaggio tra lo sprite bomba che lo invia e lo sprite Game Over che ne è in attesa.
Da notare infine l’utilizzo dell’istruzione Ferma tutto che permette di concludere tutti gli script in esecuzione, in particolare quelli del gatto e dei frutti.

Gli script da progettare sono i seguenti:


