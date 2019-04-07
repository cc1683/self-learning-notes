//void setup() {
//  Serial.begin(9600);
//}
//
//void loop() {
//  int Dout = analogRead(A0);
//  float Vin = (Dout * 0.00488);
//  Serial.print("Voltage: ");
//  Serial.println(Vin);
//  delay(1000);                                              
//}

void setup() {
  pinMode(8, OUTPUT);
}

void loop() {
  int pot = analogRead(A0);
  pot = map(pot, 0, 1023, 0, 255);
  analogWrite(8, pot); 
  delay(1000);

  analogWrite(10, pot);
  delay(1000);

  analogWrite(11, pot);
  delay(1000);
}
