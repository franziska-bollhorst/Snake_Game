/**
Programm zur Steuerug und Übermittlung der Daten an Python.
Die Verbindung basiert auf dem Code "03_ServerExample.ino" aus Tutorium 6 unseres Informatikkurses. Die beiden zusätzlichen 
Dateien "DumbServer.cpp" und "DumbServer.h" müssen dazu zwingend im selben Ordner sein, wie der Hauptcode.
*/

#include <SoftwareSerial.h> /** importiert die für die Serverkommunikation benötigte Bibliothek mit unterschiedlichsten seriellen Schnittstellen */
#include "DumbServer.h" /** importiert die beiden in "Übung 6" verwendeten Serverdateien für die Servererstellung */ 


SoftwareSerial esp_serial(3, 2);  /** die Pins 2 und 3 werden für die Verbindung vom ESP-Shield zum Arduino verwendet*/
EspServer esp_server;


String snake_direction = "u"; /** Ein String, in dem die Richtung der Schlange gespeichert wird*/
float temp = millis(); /** speichert die aktuelle Zeit*/


void setup()
{
  Serial.begin(9600); /** die Baudrate für den seriellen Monitor wird auf 9600 festgesetzt */
  esp_serial.begin(9600); /** die Baudrate für die Serverausgabe wird auf 9600 festgesetzt */

  Serial.println("Starting server..."); /** Server wird gestartet */
  esp_server.begin(&esp_serial, "Lukas-Server", "0987654321", 30303); /** SSID und Passwort wird festgelegt */
  Serial.println("...server is running"); /** Meldung, dass der Server gestartet wurde */

  char ip[16];  /** Char-Array, in dem die IP-Adresse gespeichert wird */
  esp_server.my_ip(ip, 16); /** die IP-Adresse wird abgespeichert */

  Serial.print("My ip: "); 
  Serial.println(ip); /** Falls der Arduino mit dem PC verbunden ist, wird die IP im seriellen Monitor ausgegeben */
  pinMode(9, INPUT_PULLUP); /** Hier werden die Pins für die vier Knöpfe initialisiert und alle Input-Pins zusätzlich zur Sicherheit mit der Pullup-Funktion versehen */
  pinMode(10, INPUT_PULLUP);
  pinMode(11, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(13, INPUT_PULLUP);
  pinMode(4, OUTPUT); /** Pin 4 ist der Output-Pin für die Status-LED */
  digitalWrite(4, HIGH);  /** sofern der Server gestartet wurde und alle Pins korrekt initialisiert wurden, blinkt die Status-LED dreimal */
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

void loop() { /** Hier beginnt die Abfrage der Knöpfe, die wiederum an Python die entsprechenden Richtungsangaben sendet */
  if (digitalRead(10) == HIGH)  { /** mit Hilfe von If-Funktionen wird der Status des jeweiligen Knopfs überprüft */
    snake_direction = "o";  /** wenn der jeweilige Knopf aktiviert wird, wird hier die jeweilige Richtung in der String-Variable gespeichert */
    Serial.println("o"); /** im seriellen Monitor wird ebenfalls die Richtung ausgegeben; "o" steht für "oben", "re" für "rechts", "u" für "unten" und "l" für "links" */
  }
  
  if (digitalRead(11) == HIGH)  {
    snake_direction = "re"; /** hier mussten wir an Stelle von "r" "re" verwenden, da bei der drahtlosen Übertragung durch den Servercode immer noch ein "/r" an die jeweiligen Datenpakete gehängt wird. Dies würde in Python in der Auslese der Daten zu einem Fehler führen, weshalb wir "re" verwenden */
    Serial.println("re");
  }
  
  if (digitalRead(12) == HIGH)  {
    snake_direction = "u";
    Serial.println("u");
  }
  
  if (digitalRead(13) == HIGH)  {
    snake_direction = "l";
    Serial.println("l");
  }
  
  if ((millis() - temp) > 10)   { /** hier wird alle 0,01 Sekunden die jeweilige Richtung an Python übermittelt, um dort eine kontinuierliche Vorwärtsbewegung der Schlange zu erreichen, da Pythen bei einem Nicht-Erhalten der Nachricht den Code nicht weiter ausführt */
    temp = millis();
    esp_server.println(snake_direction);
  }
}



