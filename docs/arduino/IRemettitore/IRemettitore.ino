/*
Robot comandato a carte
*/

int ledPIN= 9;
int istruzioni[30]; // matrice contenente le istruzioni
int cont_istruzioni = 0; // contatore per scrivere nella matrice
int stato_lettura = 0; // variabile che memorizza se è in corso una lettura

// routine di setup
void setup() {
  Serial.begin(9600);
  pinMode(ledPIN, OUTPUT);
}

// routine principale
void loop() {
  digitalWrite(ledPIN,HIGH);
  // read the input on analog pin 0:
  int sensorValue_A0= analogRead(A0); // lettura dei sensori IR
  int sensorValue_A1 = analogRead(A1);
  int sensorValue_A2 = analogRead(A2);
  // print out the value you read:
  Serial.println(sensorValue_A0); // stampa via seriale per controllo
  Serial.println(sensorValue_A1);
  Serial.println(sensorValue_A2);
  Serial.println(sensorValue_A2*0);

  if (sensorValue_A0 > 900 && sensorValue_A1 > 900 && sensorValue_A2 > 900){
    stato_lettura = 0; }
  
  if ((sensorValue_A0 < 900 || sensorValue_A1 < 900 || sensorValue_A2 < 900) && stato_lettura == 0){ // se si appoggia una carta

  delay(1000);
  
  if (sensorValue_A0 < 900) { // se il valore è minore di 900 è stato coperto il ricevitore
   if (sensorValue_A0 < 100){ // se è minore di 0 il colore è riflettente (bianco) e quindi viene registrata l'operazione
         istruzioni[cont_istruzioni] == 1; 
         cont_istruzioni += 1;
         Serial.println("lettura A0");
         stato_lettura = 1;
         delay(1000);
   }
  }
  
  if (sensorValue_A1 < 900){ // come sopra ma per il secondo sensore
   if (sensorValue_A1 < 100){
         istruzioni[cont_istruzioni] == 2; 
         cont_istruzioni += 1;
         Serial.println("lettura A1");
         delay(1000); // attesa per permettere la rimozione di ciò che ha coperto il ricevitore
   }
  }
  
  if (sensorValue_A2 < 900){ // come sopra ma per il terzo sensore
   if (sensorValue_A2 < 100){
         istruzioni[cont_istruzioni] == 3; 
         cont_istruzioni += 1;
         Serial.println("lettura A2");
         delay(1000); // attesa per permettere la rimozione di ciò che ha coperto il ricevitore
   }
  }
  stato_lettura = 1;
  } // fine appoggio carta
  
  delay(500);        // attesa tra un ciclo ed il successivo
}


void stampa(){ // procedura per visualizzare i dati letti
  
}
