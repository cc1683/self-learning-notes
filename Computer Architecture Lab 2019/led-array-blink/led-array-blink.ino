void setup() {
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  blink(10, 500);
  blink(11, 500);
  blink(12, 500);
  blink(13, 500);                      
}

int blink(int pin, int timer) {
  digitalWrite(pin, HIGH);
  delay(timer);
  digitalWrite(pin, LOW);
  delay(timer);
  return 0;
}
