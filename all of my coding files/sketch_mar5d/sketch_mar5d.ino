#include <Wire.h>
#include "rgb_lcd.h"



rgb_lcd lcd;



const int buttonPin = 2;     // the number of the pushbutton pin
     // the number of the LED pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
    // initialize the LED pin as an output:
    lcd.begin(16, 2);
    // initialize the pushbutton pin as an input:
    pinMode(buttonPin, INPUT);
}

void loop(){
    // read the state of the pushbutton value:
    buttonState = digitalRead(buttonPin);

    // check if the pushbutton is pressed.
    // if it is, the buttonState is HIGH:
    if (buttonState == HIGH) {
        // turn LED on:
        lcd.print("yes");
        delay(1000);
        
    }
    else {
        // turn LED off:
        lcd.print("no");
        delay(1000);

    }
}