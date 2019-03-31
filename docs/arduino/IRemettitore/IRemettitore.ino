/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/

int ledPIN= 9;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(ledPIN, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(ledPIN,HIGH);
  // read the input on analog pin 0:
  int sensorValue_A0= analogRead(A0);
  int sensorValue_A1 = analogRead(A1);
  int sensorValue_A2 = 0;
  // print out the value you read:
  Serial.println(sensorValue_A0);
  Serial.println(sensorValue_A1);
  Serial.println(sensorValue_A2);
  delay(500);        // delay in between reads for stability
}