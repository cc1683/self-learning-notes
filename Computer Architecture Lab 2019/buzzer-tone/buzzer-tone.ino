void setup() {
  // put your setup code here, to run once:
  for(int counter=0; counter<3; counter++){
    play();
  }
}

void loop() {
  // put your main code here, to run repeatedly:
}

int play() {
  
  tone(8, 262, 250);
  delay(250* 1.30);

  tone(8, 262, 250);
  delay(250* 1.30);

  tone(8, 392, 250);
  delay(250* 1.30);
  
  tone(8, 392, 250);
  delay(250* 1.30);

  tone(8, 440, 250);
  delay(250* 1.30);

  tone(8, 440, 250);
  delay(250* 1.30);

  tone(8, 392, 500);
  delay(500* 1.30);

  tone(8, 349, 250);
  delay(250* 1.30);
  
  tone(8, 349, 250);
  delay(250* 1.30);

  tone(8, 330, 250);
  delay(250* 1.30);
  
  tone(8, 330, 250);
  delay(250* 1.30);
  
  tone(8, 294, 250);
  delay(250* 1.30);
  
  tone(8, 294, 250);
  delay(250* 1.30);
  
  tone(8, 262, 500);
  delay(500* 1.30);  

  return 0;
  
}
