#include<Servo.h>
#include <Wire.h>
#include <Adafruit_MLX90614.h>
Adafruit_MLX90614 mlx = Adafruit_MLX90614();

Servo x;
int mask;


void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);
   x.attach(10);
   mlx.begin();
   pinMode(03, OUTPUT);
}

void loop() {
   if (Serial.available() > 0)
  {
    mask = Serial.read();
    if (mask == 'H')
    {
      float celsius = mlx.readObjectTempC();
      if(celsius<=36){
        x.write(180);
        digitalWrite(03, LOW);
      }
      else{
        x.write(40);
        digitalWrite(03, HIGH);
        tone(05, 494, 500);
      }
    }
      
    else if (mask == 'L'){
       x.write(40);
       digitalWrite(03, HIGH);
       tone(05, 494, 500);
    }

}
}
