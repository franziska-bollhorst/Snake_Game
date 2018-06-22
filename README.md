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
      c. über eine Tickerfunktion den Punkt bewegen lassen
      d. einen weiteren Punkt erstellen der sich random im Spielfeld erstellt (später "Apfel") 
  2. GUI
  3. Kommunikation zwischen Python und Arduino
    - Grundkonzept für die serielle Kommunikation
      a. Ansätze und Idee aus dem Tutorium 06.WIFI für des erstellen des Codes
      b. auf Basis des Tutoriums haben wir das Grundprogramm für unsere Bedürfnisse angepasst
      c. über einen Server (W-Lan-Router, Handy-Hotspot) die Verbindung erstellen 
   4. Steuerung
    - nachdem die ersten Befehele vom Arduino zum Python gesendet wurden, haben wir unterschiedliche Befehle gesendet
    - Erstellen eines Steuerkreuzes mit den Befehelen oben, unten, rechts und links, damit sich die die Schlange in die jeweilige Richtung bewegen kann
    - die Befehlen werden von dem Pythonprogramm entpfangen und mittels einer if-Funktion verarbeitet
    - 
# Probleme:
# Benutzung:
