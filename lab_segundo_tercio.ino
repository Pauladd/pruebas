int sensorPin = A0; 
int ledPin = 13; 
int brightness = 0; 

void setup() {
  pinMode(ledPin, OUTPUT); // Configurar el pin del LED como salida
  Serial.begin(9600); 
}

void loop() {
  int V_sensor = analogRead(sensorPin); // Leer el valor del sensor
  int V_min = 0; 
  int V_max = 730; 
  int mapeo = map(V_sensor, V_min, V_max, 0, 255); // Mapear el valor del sensor al rango de brillo del LED
  analogWrite(ledPin, mapeo); // Establecer el brillo del LED
  Serial.println(V_sensor); // Enviar el valor del sensor por la comunicación serial
  delay(1000); 
}
