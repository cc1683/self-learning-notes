int red = 9;
int green = 10;
int blue = 11;

void setup() {
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT); 

  for(int i=0; i<3; i++) {
    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 262, 250);
    delay(250* 1.30);
  
    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 262, 250);
    delay(250* 1.30);
  
    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 392, 250);
    delay(250* 1.30);
  
    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 392, 250);
    delay(250* 1.30); 

    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 440, 250);
    delay(250* 1.30);  

    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 440, 250);
    delay(250* 1.30);  

    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 392, 500);
    delay(500* 1.30); 

    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 349, 250);
    delay(250* 1.30);   

    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 349, 250);
    delay(250* 1.30);
  
    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 330, 250);
    delay(250* 1.30);   

    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 330, 250);
    delay(250* 1.30);  

    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 294, 250);
    delay(250* 1.30);   

    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 294, 250);
    delay(250* 1.30);
     
    analogWrite(red, random(0, 255));
    analogWrite(green, random(0, 255));
    analogWrite(blue, random(0, 255));
    tone(8, 262, 500);
    delay(500* 1.30);    
  }
}

void loop() {
}
