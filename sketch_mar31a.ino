const int PIN_BOMBILLA = 12; // Tu Pin del MOC/TRIAC
const int PIN_BOTON = 10;    // Tu Pin del Botón

void setup() {
  Serial.begin(115200);
  pinMode(PIN_BOMBILLA, OUTPUT);
  pinMode(PIN_BOTON, INPUT); // Usamos la resistencia interna
}

void loop() {
  // 1. Escuchar a ROS 2
  if (Serial.available() > 0) {
    char comando = Serial.read();
    if (comando == '1') digitalWrite(PIN_BOMBILLA, HIGH);
    if (comando == '0') digitalWrite(PIN_BOMBILLA, LOW);
  }

  // 2. Avisar a ROS 2 sobre el botón
  if (digitalRead(PIN_BOTON) == HIGH) { // Si se presiona (GND)
    Serial.println("BOTON_ON");
    delay(200); // Debounce simple
  }
}
