#include "DataUploader.h"

char host[] = "smartgarden-5d081.firebaseio.com";
char ssid[] = "BlueStamp@GHS";
char pass[] = "Scr@nt0n";

DataUploader uploader(host, ssid, pass, true);

float temp;
float light;
float moist;

int moisturePin = A1;
int tempPin = A2;    // select the input pin for the sensor 
int photoPin = A3;

void setup() {
  uploader.init();
}

void loop() {
  temp = getTemp();
  light = getLight();
  moist = getMoisture();
  uploader.uploadDataPoint(temp, light, moist);
  delay(2000);
}

float getMoisture() {
  return 1000-(1000*analogRead(moisturePin))/1023;
}

float getTemp() {
  int sensorValue = analogRead(tempPin); 
  float voltage = sensorValue * (3300/1024); // in milliVolt 
  float temperature = (voltage - 500 ) / 10; 
  return temperature;
}

float getLight() {
  return analogRead(photoPin);
}
