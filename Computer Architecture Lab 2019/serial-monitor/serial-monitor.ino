int a = 45;
int b = 90;
int c = 988;

void setup() {
  Serial.begin(9600);

  Serial.println("Basic Mathematics.");

  Serial.print("Value of A: ");
  Serial.println(a);
  Serial.print("Value of B: ");
  Serial.println(b);
  Serial.print("Value of C: ");
  Serial.println(c);

  Serial.print("a + b = ");
  Serial.println(a+b);
  Serial.print("c - b = ");
  Serial.println(c-b);
  Serial.print("a * c = ");
  Serial.println(a*c);
  Serial.print("c / b = ");
  Serial.println(c/b);
}

void loop() {
}
