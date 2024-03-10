#include <Keypad.h>
#include <Arduino.h>


const byte numRows= 4;
const byte numCols= 4;
const int analogPin = 5;

char keymap[numRows][numCols]= 
{
  {'0','1','2','3'},
  {'4','5','6','7'},
  {'8','9','A','B'},
  {'C','D','E','F'}
};

byte rowPins[numRows] = {2,3,4,5}; 
byte colPins[numCols]= {6,7,8,9};

Keypad myKeypad= Keypad(makeKeymap(keymap), rowPins, colPins, numRows, numCols);


void setup()
{
  Serial.begin(9600);
}

void loop()
{
  char keypressed = myKeypad.getKey();
  int val = analogRead(analogPin);
  static int prevVal = 0;

  if (val != (prevVal + 1) && val != (prevVal - 1) && val != prevVal) {
    Serial.println(val);
    prevVal = val;
  }


  if (keypressed != NO_KEY)
  {
    switch (keypressed)
    {
      case '0':
          Serial.println("Mode");
          delay(100);
        break;
      case '1':
          Serial.println("Drum");
          delay(100);
        break;  
      case '3':
          Serial.println("record");
          delay(10);
      break;
      case '2':
          Serial.println("bass");
          delay(10);
      break; 
      case '4':
          Serial.println("bass");
          delay(10);
      break;
      case '5':
          Serial.println("bass");
          delay(10);
      break;
      case '6':
          Serial.println("bass");
          delay(10);
      break;
      case '7':
          Serial.println("bass");
          delay(10);
      break;
      case '8':
          Serial.println("bass");
          delay(10);
      break;
      case 'A':
          Serial.println("bass");
          delay(10);
      break;
      case 'B':
          Serial.println("bass");
          delay(10);
      break;
      case 'C':
          Serial.println("bass");
          delay(10);
      break;
      case 'D':
          Serial.println("bass");
          delay(10);
      break;
      case 'E':
          Serial.println("bass");
          delay(10);
      break;
      case 'F':
          Serial.println("bass");
          delay(10);
      break;
      default:
        Serial.println(keypressed);
        break;
    }

  }
}
