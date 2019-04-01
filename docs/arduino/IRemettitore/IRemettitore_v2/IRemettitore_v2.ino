/*
Robot comandato a carte
*/

int led_IR_PIN = 9; // accende il led emettitore
int led_control_PIN = 13; // si accende quando registra un valore
int istruzioni[30]; // matrice contenente le istruzioni
int cont_istruzioni = 0; // contatore per scrivere nella matrice
int stato_lettura = 0; // variabile che memorizza se è in corso una lettura
int esegui_prog = 0; // variabile per comandare l'avvio del programma

// routine di setup
void setup() {
  Serial.begin(9600);
  pinMode(led_IR_PIN, OUTPUT);
  pinMode(led_control_PIN, OUTPUT);
}

// routine principale
void loop() {
  digitalWrite(led_IR_PIN,HIGH); // accende il led IR emettitore
 
  if  (stato_lettura == 0){      // accende il led se è stata eseguita una lettura
    digitalWrite(led_control_PIN,LOW);
  }
  else{
    digitalWrite(led_control_PIN,HIGH);
  }

  // read the input on analog pin 0:
  int sensorValue_A0= analogRead(A0);     // lettura dei sensori IR
  int sensorValue_A1 = analogRead(A1);
  int sensorValue_A2 = analogRead(A2);
  // print out the value you read:
  Serial.println(sensorValue_A0);         // stampa via seriale per controllo
  Serial.println(sensorValue_A1);
  Serial.println(sensorValue_A2);
  Serial.println(sensorValue_A2*0);

  if (sensorValue_A0 > 900 && sensorValue_A1 > 900 && sensorValue_A2 > 900){                            // se nessuna carta è appoggiata il valori letti vanno oltre 900
    stato_lettura = 0; }
  
  if ((sensorValue_A0 < 900 || sensorValue_A1 < 900 || sensorValue_A2 < 900) && stato_lettura == 0){    // se si appoggia una carta invece cambiano

  delay(2000);                          // attende un po' per permettere il posizionamento e poi esegue nuovamente la lettura
  int sensorValue_A0= analogRead(A0); 
  int sensorValue_A1 = analogRead(A1);
  int sensorValue_A2 = analogRead(A2);
  Serial.println(sensorValue_A0);       // stampa via seriale per controllo
  Serial.println(sensorValue_A1);
  Serial.println(sensorValue_A2);
  Serial.println(sensorValue_A2*0);

   if (sensorValue_A0 < 100 && sensorValue_A1 < 100 && sensorValue_A2 < 100){ // è stata appoggiata la carta tutta bianca per avviare il programma
     esegui_prog = 1; }
   
   else{                                                                      // altrimenti è stata appoggiata una carta avanti-destra-sinistra
   
   if (sensorValue_A0 < 100){ // se è minore di 0 il colore è riflettente (bianco) e quindi viene registrata l'operazione
         istruzioni[cont_istruzioni] = 1; 
         cont_istruzioni += 1;
         Serial.println("lettura A0");
         stato_lettura = 1;
         delay(100);
   }
  
   if (sensorValue_A1 < 100){
         istruzioni[cont_istruzioni] = 2; 
         cont_istruzioni += 1;
         Serial.println("lettura A1");
         delay(100); // attesa per permettere la rimozione di ciò che ha coperto il ricevitore
   }
  
   if (sensorValue_A2 < 100){
         istruzioni[cont_istruzioni] = 3; 
         cont_istruzioni += 1;
         Serial.println("lettura A2");
         delay(100); // attesa per permettere la rimozione di ciò che ha coperto il ricevitore
   }
   }
   stato_lettura = 1;
  } // fine appoggio carta
  
  delay(500);        // attesa tra un ciclo ed il successivo

  if (cont_istruzioni > 4){
      Serial.println(istruzioni[0]);
      Serial.println(istruzioni[1]);
      Serial.println(istruzioni[2]);
      Serial.println(istruzioni[3]);
      delay(5000);
  }
  
}


void stampa(){ // procedura per visualizzare i dati letti
  
}
