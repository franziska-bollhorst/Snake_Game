# Snake_Game
Snake mit Steuerung über Arduino und GUI/Programm über Python
# Idee:
- typisches Snakespiel (übliche Regeln)
- Steuerung und Programm laufen über zwei unterschiedliche Programme
- Steuerung wird mittels des Arduinos durchgeführt und dafür wird ein "Controler" erstellt, der die Schlange steuern lässt
- das Hauptprogramm läuft mit Idle, d.h. das Spiel und die GUI wird über Python erstellt
- die Kommunikation zwischen den beiden Programmen verläuft drahtlos, d.h.es wird ein W-Lanshield für den Arduino benutzt, der über einen Hotspot mit dem Pythonprogramm kommuniziert

# Herangehensweise:
- drei große Herausforderungen:
  1. Grundprogramm
    - Grundkonzept für das Spiel
      a. ein Spielfeld erstellen, indem sich eine Schlange bewegt könnte (Größe, über Koordinaten etc.)
      b. Punkt im Spielfeld erstellen (später die Schalnge)
      c. einen weiteren Punkt erstellen, der sich random im Spielfeld erstellt (später "Apfel")
      d. Funktion erstellen, die die Kollision der Schlange mit sich selber und mit der Boarder abfragt, sodass man das Spiel verliert, wenn die Schlange kollidiert
      e. mittels eines Buttons ("Neustart") kann das Spiel danach beliebig oft ausgeführt werden
      f. das Empfangen der Daten vom Arduino einbauen, damit sich darüber die Richtung der Schlange ändert und sich der Punkt auch in einem bestimmten Zeitintervall weiter bewegt
      g. Verlängerung der Schlange, wenn sie auf einen Apfel trifft, einbauen, sodass die Schalnge wächst
      h. zusätzlich kann ein Score eingebaut werden, der sich immer um z.B. 10 erhöht, wenn die Schlange einen Apfel isst, die Score kann sich nun ggf. auf den Highscore überschreiben lassen, wenn Score > Highscore
  2. GUI (Tkinter)
    - Spielfeld erstellen mit Hilfe von Koordinaten erstellen 
    - Schalnge und Apfel im Koordinatensystem erscheinen lassen
    - Textfelder ("Score", "Highscore", "Du hast verloren!") erstellen
    - Neustartbutton 
  3. Kommunikation zwischen Python und Arduino
    - Grundkonzept für die serielle Kommunikation
      a. Ansätze und Idee aus dem Tutorium 06.WIFI für des erstellen des Codes
      b. auf Basis des Tutoriums haben wir das Grundprogramm für unsere Bedürfnisse angepasst
      c. über einen Server (W-Lan-Router, Handy-Hotspot) die Verbindung erstellen 
   4. Steuerung
    - nachdem die ersten Befehele vom Arduino zum Python gesendet wurden, haben wir unterschiedliche Befehle gesendet
    - Erstellen eines Steuerkreuzes mit den Befehelen oben, unten, rechts und links, damit sich die die Schlange in die jeweilige Richtung bewegen kann
    - die Befehlen werden von dem Pythonprogramm entpfangen und mittels einer if-Funktion verarbeitet
    -  damit sich die Schlange nachdem ein Knopf gedrückt wurde auch weiter in die Richtung bewegt, muss eine millis-Funktion erstellt werden, diese sendet den einmal ausgeführten Befehl innerhalb kurzer Zeit an Python
    - dies wird so lange gemacht bis der Spieler die Richtung ändert, dann sendet der Arduino die neue Richtung an das Pythonprogramm
    - das Steuerkreuz haben wir mit einen Breadboard und vier Knöpfen erstellt 
    - die Könpfe wurde an bestimmte Pins geschaltet und diese Pins sind im Arduinocode für die jeweilige Richtung hinterlegt worden
# Probleme:
# Benutzung:
