//int LDR_Pin = A0;
//
//void setup() {
//  Serial.begin(9600);
//}
//
//void loop() {
//  float LDR_Reading = analogRead(LDR_Pin);
//  LDR_Reading  = (LDR_Reading*0.00488);
//
//  Serial.println(LDR_Reading);
//  delay(1000);
//}

int LDR_Pin = A0;

void setup() {
  pinMode(11, OUTPUT); // RGB
  pinMode(2, OUTPUT); // LED ARRAY
}

void loop() {
  float LDR_Reading = analogRead(LDR_Pin);
//  LDR_Reading  = (LDR_Reading*0.00488);
  LDR_Reading = map(LDR_Reading, 0, 1023, 0, 255);
  analogWrite(11, LDR_Reading);

  if(LDR_Reading > 1.0) {
    digitalWrite(2, LOW);  
  } else {
    digitalWrite(2, HIGH);  
  }
}
