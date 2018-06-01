Utilizzo di un servo
====================

Servo pilotato direttamente con comandi e delay
***********************************************

::

    // include the servo library
    #include <Servo.h>

    Servo myServo;  // create a servo object 
    
    
    void setup() {
    pinMode(A0,INPUT);
    myServo.attach(9); // attaches the servo on pin 9 to the servo object  
    Serial.begin(9600); // open a serial connection to your computer
    }
    
    void loop() {
  
    // print out the angle for the servo motor 
    Serial.print(", angle: ");
    Serial.println(0); 

    // set the servo position  
    myServo.write(0);
    
    // wait for the servo to get there 
    delay(500);
  
    Serial.print(", angle: ");
    Serial.println(30); 
    myServo.write(30);
    delay(500);
  
    Serial.print(", angle: ");
    Serial.println(60); 
    myServo.write(60);
    delay(500); 
  
    }

Servo pilotato con potenziometro
********************************

::

    // include the servo library
    #include <Servo.h>
    
    Servo myServo;  // create a servo object 
    int pot,potPrec=0;
    
    void setup() {
    pinMode(A0,INPUT);
    myServo.attach(9); // attaches the servo on pin 9 to the servo object 
    Serial.begin(9600); // open a serial connection to your computer
    pot=map(analogRead(A0),0,1024,0,179);
    potPrec=pot;
    }

    void loop() {
      
    // print out the angle for the servo motor 
    
    pot=map(analogRead(A0),0,1024,0,179);
    
    if (abs(potPrec-pot)>10){
    Serial.print(analogRead(A0));
    Serial.print(",");
    Serial.println(pot);
    potPrec=pot;
    }

    // set the servo position  
    myServo.write(pot);
    delay(10);
    }
