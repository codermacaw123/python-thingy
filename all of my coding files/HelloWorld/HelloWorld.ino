

#include <Wire.h>
#include "rgb_lcd.h"



rgb_lcd lcd;

// const int colorR = 0;
// const int colorG = 255;
// const int colorB = 100;

int score = 1;

void setup() {
    // set up the LCD's number of columns and rows:
    lcd.begin(16, 2);
    
    

    // Print a message to the LCD.
    lcd.print("initalizing...");
    lcd.setCursor(0, 1);
    lcd.print("lets play a game!");

    delay(1000);
}

void loop() {
    // set the cursor to column 0, line 1
    // (note: line 1 is the second row, since counting begins with 0):
    lcd.setCursor(0, 1);
    // print the number of seconds since reset:
  
    
    int colorR=random(255);
    int colorG=random(255);
    int colorB=random(255);
    
    
    lcd.setRGB(colorR, colorG, colorB);


    delay(100);
}

