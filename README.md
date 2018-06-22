# Snake_Game
Snake mit Steuerung über Arduino und GUI/Programm über Python
# Idee:
- typisches Snakespiel (übliche Regeln)
- Steuerung und Spiel laufen über zwei unterschiedliche Programme
- Steuerung wird mittels des Arduinos durchgeführt. Dafür wurde ein "Spiel-Controller" mit Hilfe eines Pappkartons erstellt, mit dem     sich die Schlange steuern lässt
- das Hauptprogramm und somit die GUI läuft in Python
- die Kommunikation zwischen den beiden Programmen verläuft drahtlos, d.h. es wird ein Wifi-Shield für den Arduino benutzt, der über einen Hotspot mit dem Pythonprogramm kommuniziert

# Herangehensweise:
- drei große Herausforderungen:
  1. Grundprogramm
    - Grundkonzept für das Spiel
      a. ein Spielfeld erstellen, indem sich eine Schlange bewegen könnte (Größe, Darstellung über Koordinaten, Design etc.)
      b. Punkte/Quadrate im Spielfeld erstellen (später die Schlange)
      c. einen weiteren Punkt erstellen, der sich random im Spielfeld erstellt (später "Apfel")
      d. Funktion erstellen, die die Kollision der Schlange mit sich selber und mit der Wand/dem Spielfeldrand abfragt, sodass man das Spiel verliert, wenn die Schlange kollidiert
      e. mittels eines Buttons ("Neustart") kann das Spiel danach beliebig oft ausgeführt werden
      f. eine Funktion einbauen, die die gesendeten Daten vom Arduino ausliest, damit sich darüber die Richtung der Schlange ändert und sich der Punkt in einem bestimmten Zeitintervall weiter bewegt
      g. Verlängerung der Schlange, wenn sie auf einen Apfel trifft
      h. zusätzlich kann ein Score eingebaut werden, der sich immer um z.B. 10 Punkte erhöht, wenn die Schlange einen Apfel isst. Dieser kann nun ggf. auch ine einem Highscore gespeichert werden, wenn Score > Highscore
  2. GUI (Tkinter)
    - Spielfeld mit Hilfe von Koordinaten erstellen 
    - Schalnge und Apfel im Koordinatensystem/ auf dem Spielfeld erscheinen lassen
    - Textfelder ("Score", "Highscore", "Du hast verloren!") erstellen
    - Neustart-Button erstellen
    - Startfenster erstellen, bei dem der Name vor Beginn des Spiels abgefragt wird und dieses gestartet werden kann
    - viele Designs wurde individuell geändert, z.B Farbe des Spielfeldes, der Schlange und des Apfels, Größe des Spielfeldes, Hintergrundfarbe des "Neustartbuttons", etc.
  3. Kommunikation zwischen Python und Arduino
    - Grundkonzept für die serielle, drahtlose Kommunikation
      a. Ansätze und Idee aus dem Tutorium 06.
      b. auf Basis des Tutoriums haben wir das Grundprogramm für unsere Bedürfnisse angepasst
      c. über einen Server (W-Lan-Router, Handy-Hotspot) die Verbindung erstellen 
   4. Steuerung
    - nachdem die ersten Befehle vom Arduino an den PC gesendet wurden, haben wir unterschiedliche Befehle gesendet
    - Erstellen eines Steuerkreuzes mit den Befehelen "oben", "unten", "rechts" und "links", damit sich die die Schlange in die jeweilige Richtung bewegen kann
    - die Befehle werden von dem Pythonprogramm entpfangen und mittels einer if-Funktion verarbeitet
    - damit sich die Schlange, nachdem ein Knopf gedrückt wurde auch weiter in die Richtung bewegt, muss eine millis-Funktion erstellt werden. Diese sendet den einmal ausgeführten Befehl solange an Python, bis dieser durch einen neuen ersetzt wird.
    - das Steuerkreuz haben wir mit einen Breadboard und vier Knöpfen erstellt 
    - die Könpfe wurde an bestimmte Pins geschaltet und diese wurden im Arduinocode für die jeweilige Richtung hinterlegt
# Probleme:
# Benutzung:
