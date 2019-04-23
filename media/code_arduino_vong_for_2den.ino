#include <Arduino.h>
#include <Wire.h>
#include <SoftwareSerial.h>

int ledpin[]={9,10};
int n;

void setup(){
    n=sizeof(ledpin);
    for(int i=0;i<n;i++)
    {
        pinMode(ledpin[i],OUTPUT);
        digitalWrite(ledpin[i],LOW);
    }
    
}

void loop(){
   for( int i=0;i<n;i++)
   {
    digitalWrite(ledpin[i],HIGH);
    digitalWrite(ledpin[i+1],HIGH);
    delay(1000);
    digitalWrite(ledpin[i],LOW);
    digitalWrite(ledpin[i+1],LOW);
    delay(1000);
   }
}
    
  
