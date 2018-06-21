#include <SoftwareSerial.h> // importiert die für die Serverommunikation benötigte Bibliothek mit unterschiedlichsten seriellen Schnittstellen
#include "DumbServer.h" // importiert die beiden in "Übung 6" verwendeten Serverdateien für die Servererstellung


SoftwareSerial esp_serial(3, 2);  // die Pins 2 und 3 werden für die Verbindung vom ESP-Shield zum Arduino verwendet
EspServer esp_server;


String snake_direction = "u"; // Ein String in dem die Richtung der Schlange eingegeben wird
float temp = millis(); // speichert die aktuelle Zeit


void setup()
{
  Serial.begin(9600); // die Baudrate für den seriellen Monitor wird auf 9600 festgesetzt
  esp_serial.begin(9600); // die Baudrate für die Serverausgabe wird auf 9600 festgesetzt

  Serial.println("Starting server..."); // Server wird gestartet
  esp_server.begin(&esp_serial, "Lukas-Server", "0987654321", 30303); // SSID und Passwort wird festgelegt
  Serial.println("...server is running"); // Meldung, dass der Server gestartet wurde

  char ip[16];  // Char-Array, in dem die IP-Adresse gespeichert wird
  esp_server.my_ip(ip, 16);

  Serial.print("My ip: ");
  Serial.println(ip);
  pinMode(9, INPUT_PULLUP);
  pinMode(10, INPUT_PULLUP);
  pinMode(11, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(13, INPUT_PULLUP);
  pinMode(4, OUTPUT);
  digitalWrite(4, HIGH);
  delay(500);
  digitalWrite(4, LOW);
  delay(500);
  digitalWrite(4, HIGH);
  delay(500);
  digitalWrite(4, LOW);
  delay(500);
  digitalWrite(4, HIGH);
  delay(500);
  digitalWrite(4, LOW);
  delay(500);
}

void loop() {
  if (digitalRead(10) == HIGH)  {
    digitalWrite(4, HIGH);
    snake_direction = "o";
    //esp_server.println(snake_direction);
    Serial.println("o");
    //delay(500);
  }
  if (digitalRead(11) == HIGH)  {
    digitalWrite(4, HIGH);
    snake_direction = "re";
    //esp_server.println(snake_direction);
    Serial.println("re");
    //delay(500);
  }
  if (digitalRead(12) == HIGH)  {
    digitalWrite(4, HIGH);
    snake_direction = "u";
    //esp_server.println(snake_direction);
    Serial.println("u");
    //delay(500);
  }
  if (digitalRead(13) == HIGH)  {
    digitalWrite(4, HIGH);
    snake_direction = "l";
    //esp_server.println(snake_direction);
    Serial.println("l");
    //delay(500);
  }
  
  else   {
    digitalWrite(4, LOW);
  }




  if ((millis() - temp) > 10)
  {
    temp = millis();
    esp_server.println(snake_direction);
  }

}




// esp_server.println("Test");

/*else
  {
    Serial.println("Geht nicht");
  } */


