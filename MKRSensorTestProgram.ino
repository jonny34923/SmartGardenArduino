// Simple sensor test programme
int moisturePin = A1;
int tempPin = A2;    // select the input pin for the sensor 
int photoPin = A3;
int sensorValue = 0;   // variable to store the value coming from the sensor 
float temperature = 0.0;  
float voltage = 0.0; 
float moisture = 0.0;
float photo = 0.0;
void setup() { 
Serial.begin(9600); 
analogReadResolution(10); 
} 
void loop() { 
// read the value from the sensor: 
sensorValue = analogRead(tempPin); 
Serial.print("sensorValue = "); 
Serial.print(sensorValue); 
voltage = sensorValue * (3300/1024); // in milliVolt 
Serial.print(" voltage = "); 
Serial.print(voltage); 
temperature = (voltage - 500 ) / 10; 
Serial.print(" temperature(C) = "); 
Serial.println(temperature); 
moisture = 1-analogRead(moisturePin)/1023;
Serial.print("moisture% ");
Serial.println(moisture);
photo = analogRead(photoPin);
Serial.print("photo ");
Serial.println(photo);
delay(100);
} 
