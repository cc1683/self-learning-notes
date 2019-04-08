#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
#include <LiquidCrystal.h>

#define DHTPIN 2     

#define DHTTYPE    DHT11     

DHT_Unified dht(DHTPIN, DHTTYPE);

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(8, 9, 10, 11, 12, 13);

void setup() {
  lcd.begin(16, 2);
  dht.begin();
}

void loop() {
  delay(2000);
  sensors_event_t event;
  dht.temperature().getEvent(&event);
  if (isnan(event.temperature)) {
    lcd.print(F("Error reading humidity!"));
  }
  else {
    lcd.setCursor(0, 0);
    lcd.print("Temperature:");
    lcd.print(event.temperature);
  }
  // Get humidity event and print its value.
  dht.humidity().getEvent(&event);
  if (isnan(event.relative_humidity)) {
    lcd.print("Error reading humidity!");
  }
  else {
    lcd.setCursor(0, 1);
    lcd.print("Humidity:");
    lcd.print(event.relative_humidity);
  }
}
