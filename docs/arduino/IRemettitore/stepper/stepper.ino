#include <Stepper.h>
#define STEPS 100

Stepper small_stepper(STEPS, 2, 4, 3, 5);
int Steps2Take;

void setup() {

}

void loop() {
 small_stepper.setSpeed(200);
 Steps2Take = 100; //se cambiato il valore 100 con un altro numero, 
//lo step motor di muoverà in un'analtra maniera
 small_stepper.step(Steps2Take);
 delay(2000);

small_stepper.setSpeed(200);
 Steps2Take = -100;
 small_stepper.step(Steps2Take);
 delay(2000);

small_stepper.setSpeed(200);
 Steps2Take = 500;
 small_stepper.step(Steps2Take);
 delay(2000);

small_stepper.setSpeed(200);
 Steps2Take = -500;
 small_stepper.step(Steps2Take);
 delay(2000);

small_stepper.setSpeed(200);
 Steps2Take = 1000;
 small_stepper.step(Steps2Take);
 delay(2000);

small_stepper.setSpeed(200);
 Steps2Take = -1000;
 small_stepper.step(Steps2Take);
 delay(2000);

small_stepper.setSpeed(200);
 Steps2Take = 2000;
 small_stepper.step(Steps2Take);
 delay(2000);

small_stepper.setSpeed(200);
 Steps2Take = -2000;
 small_stepper.step(Steps2Take);
 delay(2000);
}
