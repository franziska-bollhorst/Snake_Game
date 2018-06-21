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
    - Schritt für Schritt, d.h:
      - ein Spielfeld erstellen, indem sich eine Schlange bewegt könnte (Größe, über Koordinaten etc.)
      - Punkt im Spielfeld erstellen (später die Schalnge)
      - über eine Tickerfunktion den Punkt bewegen lassen
      - einen weiteren Punkt erstellen
  2. GUI
  3. Kommunikation zwischen Python und Arduino
  
