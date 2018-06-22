#!/usr/bin/env python3

"""
Informatik Projekt 2018
Thema:  Snake
Erstellt von: Adrian Bergen(4228620), Lukas Hansen(4463302), Fanziska Bollhorst (4463145)


"""
import tkinter as tk
from tkinter import *
from random import randint
import socket
"""
Es werden die benötigten librarys importiert. Tkinter für die GUI,
Socket für die Kommunikation, Random für zufällige Zahlen.
"""

s=socket.socket()                                                  
s.connect(('192.168.43.51', 30303))
s.setblocking(True)
"""
Setze die Kommunikation auf.
"""


size=25                                                            
feedcollision=False
length=1
direction=randint(1,4)
xx=8                                                            
yy=8
feedpoint=[randint(1,16),randint(1,16)]                             
xcoordinate=[xx]                                                
ycoordinate=[yy]
lost=False
score=0
highscore=0
"""
Hier werden die für das Spiel benötigten Anfangsvariabeln erstellt.
size: Größe der Quadrate, auf den das Spielfeld gezeichnet wird.
feedcollision: Am Anfang kollidiert die Schlange nicht mit einem Punkt
length: Länge der Schlange, vergrößert sich beim Aufsammeln eines Punktes
direction: Zahlen von 1-4, sie stehen für die jeweilige Richtung.
Dabei wird direction von Arduino gesteuert.
xx und yy: Reine Anfangskoordinaten der Schlange auf dem Feld.
(Das Feld ist 16x16)
x/ycoordinate: xx und yy werden in jeweils einem Array gepackt.
Später zeigt das Array die Punkte aller Schlangenpunkte.
(Also länge des Arrays =Länge der Schlange)
lost: Ist standartmäßig nicht True
score/ Highscore: Ist am Anfang 0
"""

class Game(tk.Tk):
    def createbutton(self):
        """
        Hier wird ein Knopf erstellt, nachdem man bei dem Spiel verliert.
        Dieser Knopf dient dazu das Spiel neu zu starten (Aufrufen der Funktion "restart").
        Des Weiteren wird ein Textfeld erstellt. Dieses benachrichtigt dich, dass du verloren hast.
        """
        global knopf
        knopf=tk.Button(w,text="Neustart", fg='Azure', bg='#87ceeb', activebackground='#8470ff', command=self.restart)
        knopf.pack()
        w.create_window(250,10,anchor=tk.N,window=knopf)
        global verlorentext
        verlorentext = w.create_text((250, 475), text="DU HAST VERLOREN")

    def ticker(self):                                                 
        """
        Das Herz des Spiels. Ticker ruft sich alle 0,6 Sekunden rekursiv mithilfe einer after-Funktion wieder auf.
        Mit receivearduino wird die direction von Snake empfangen.
        Die Funktion ruft sich nicht wieder auf, wenn man verloren hat. Stattdessen hört das Spiel auf und der
        Neustartbutton wird erstellt.
        """
        self.receivearduino()
        
        if(lost==False):
            self.drawsnake()
            self.after(600,self.ticker)

        else:
            self.createbutton()
            
    
    def drawsnake(self):
    """
    Zuerst wird geprüft, ob die Schlange mit einem Punkt (Futter) kollidiert.
    Anschließend wird das Array x/ycoordinate um die jeweilige NEUE x/y Koordinate erweitert.
    Bei collisions wird die Kollision mit der Schlange selber, sowie den Wänden geprüft.
    doastep verändert xx und yy, jenachdem welche "direction" die Schlange gerade hat.
    Als nächstes wird der neue Kopf der Schlange gezeichnet, anschließend wird
    hinten wieder die Spielfeldfarbe gezeichnet - Eine Schlange entsteht.
    Da die Länge der Schlange von Punktekollisionen gesteuert wird, muss sich das
    Array darauf anpassen, so wächst die Schlange tatsächlich auch.
    """
        global xx
        global yy
        global xcoordinate
        global ycoordinate
        global feedcollision
        global lost
        global direction
        
        self.feedpoint()

        ycoordinate.append(yy)
        xcoordinate.append(xx)  

        self.collisions()

        self.doastep()
        
        
        if(lost==False):
            w.create_rectangle(25+(xcoordinate[len(xcoordinate)-1])*25, 25+(ycoordinate[len(ycoordinate)-1])*25, 25+(xcoordinate[len(xcoordinate)-1])*25+size, 25+(ycoordinate[len(ycoordinate)-1])*25+size, outline="#556b2f", fill="#556b2f")
        
        if(feedcollision == False)and(lost == False):                                 
            w.create_rectangle(25+xcoordinate[0]*25, 25+ycoordinate[0]*25, 25+xcoordinate[0]*25+size, 25+ycoordinate[0]*25+size, outline="#87ceeb", fill="#87ceeb")
            

        if(len(xcoordinate)>length):
            del xcoordinate[0],ycoordinate[0]
        
        print("x: ", xcoordinate)
        print("y: ", ycoordinate)


    def feedpoint(self):
        """
        Kollidiert der Schlangenkopf mit den x und y Koordinaten des feedpoints?
        Dann verändert sich der Score, die Schlange wächst um 1, ein neuer Punkt wird erstellt.
        """
        global length
        global feedcollision
        global feedpoint
        global score

        if(xcoordinate[len(xcoordinate)-1]==feedpoint[0]):
            if(ycoordinate[len(ycoordinate)-1]==feedpoint[1]):
                print("Kollision")
                length+=1
                feedcollision=True
                score+=10
                w.itemconfig(scorenumber, text=score)
                self.createfeedpoint()
        else:
            feedcollision=False


    def createfeedpoint(self):
        """
        Hier wird der feedpoint generiert. Es passiert zufällig auf dem Spielfeld. Es ist darauf
        zu achten, dass der Punkt nicht auf der Schlange generiert wird, andernfalls wird ein
        neuer Punkt generiert.
        """
        global feedpoint
        feedpoint=[randint(1,16),randint(1,16)]
        for i in range(0,(length-1)):
            if(feedpoint[0] == xcoordinate[i]):
                if(feedpoint[1] == ycoordinate[i]):
                    self.createfeedpoint()                        
        w.create_rectangle(25+feedpoint[0]*25, 25+feedpoint[1]*25, 25+feedpoint[0]*25+size, 25+feedpoint[1]*25+size, outline="#ff4500", fill="#ff4500")


    def collisions(self):
        """
        Diese Funktion checkt die Kollision mit den Spielfeldrändern und der Schlange selber. 
        Passiert dies, wird lost=True gesetzt und der Ticker läuft im nächsten
        Durchgang nicht weiter.
        """
        global lost
        
        if(xcoordinate[len(xcoordinate)-1]==0)or(ycoordinate[len(ycoordinate)-1]==0)or(xcoordinate[len(xcoordinate)-1]==17)or(ycoordinate[len(ycoordinate)-1]==17):
            print("Verloren")
            lost=True
            
        for i in range(0,len(xcoordinate)-2):
            for j in range(0,len(ycoordinate)-2):
                if(xcoordinate[len(xcoordinate)-1]==xcoordinate[i]):
                    if(ycoordinate[len(ycoordinate)-1]==ycoordinate[j]):
                        print("Verloren")
                        lost=True

    def doastep(self):
        """
        Bestimme die neuen Koordinaten von Snake, abhängig von der momentanten Richtung.
        """
        global xx
        global yy
        if(direction==1):
            yy-=1
        elif(direction==2):
            xx+=1
        elif(direction==3):
            yy+=1
        elif(direction==4):
            xx-=1

    def restart(self):
        """
        Wenn man verliert, muss das Spiel neu aufgesetzt werden.
        Das Spielfeld wird neu gezeichnet, ein neuer Highscore wird bestimmt. 
        Es erscheint ein Text, dass man verloren hat und die Variabeln werden
        zurückgesetzt (z.B. die Koordinaten). Der Ticker wird neugestartet.
        """
        global length
        global direction
        global xx
        global yy
        global feedpoint
        global xcoordinate
        global ycoordinate
        global lost
        global score
        global highscore
        
        for x in range(50,450,25):                                          
            for y in range(50,450,25):
                w.create_rectangle(x, y, x+size, y+size, outline="#87ceeb", fill="#87ceeb")

        if(score>highscore):
            highscore=score
            
        score=0
        w.itemconfig(highscorenumber, text=highscore)
        w.itemconfig(scorenumber, text=score)
        knopf.destroy()
        w.itemconfig(verlorentext, text="")
        length=1
        direction=randint(1,4)
        yy=8
        xx=8  
        ycoordinate=[yy]
        xcoordinate=[xx]
        lost=False
        self.createfeedpoint()
        self.ticker()



    def receivearduino(self):
        """
        Empfange vom Arduino die Richtungsdaten (String). Man unterscheidet zwischen
        'u', 're', 'l', 'o' für die jeweiligen Richtungen. Es ist darauf zu achten,
        dass die Schlange keine 180° Wende machen kann.
        """
        global direction
            
        directiondata = s.recv(1024) 
        if ('u' in str(directiondata))and(direction!=1):
            print ("unten")
            direction=3
        elif ('re' in str(directiondata))and(direction!=4):
            print ('rechts')
            direction=2
        elif ('l' in str(directiondata))and(direction!=2):
            print ('links')
            direction=4
        elif ('o' in str(directiondata))and(direction!=3):
            print ('oben')
            direction=1


def createfield():
    """
    Hier wird das erste mal das richtige Spielfeld erstellt. Es wird der Spielername übernommen
    und nach oben links gesetzt, Score und Highscore nach oben rechts. Das Startfenster wird gelöscht.
    Der Ticker wird zum ersten mal gestartet. Der Feedpoint wird gesetzt.
    """
    global w
    
    w = tk.Canvas(tk.Tk(), width=500, height=500, bg = 'Azure')
    w.pack()
    textname = w.create_text(50, 25, text=eingabefeld.get())
    scoretext = w.create_text(350, 15, text='Score: ')
    highscoretext = w.create_text(350, 35, text='Highscore: ') # font="Arial")
    global scorenumber
    scorenumber = w.create_text((400, 15), text=score)
    global highscorenumber
    highscorenumber = w.create_text((400, 35), text=highscore)
    fenster.destroy()
    for x in range(50,450,25):
        for y in range(50,450,25):
            w.create_rectangle(x, y, x+size, y+size, outline="#87ceeb", fill="#87ceeb")
    game.ticker()
    w.create_rectangle(25+feedpoint[0]*25, 25+feedpoint[1]*25, 25+feedpoint[0]*25+size, 25+feedpoint[1]*25+size, outline="#ff4500", fill="#ff4500")

def firststart():
    """
    Wird das Spiel gestartet, erscheint ein Fenster mit Namenseingabe und einem Startknopf.
    Durch diesen Startknopf startet sich das Spiel.
    """
    
    fenster = Tk()
    fenster.geometry("600x600")
    fenster.title("SNAKE-GAME")
    startknopf=Button(fenster,text="Starten", bg = '#87ceeb', command=createfield)
    startknopf.pack()
    startknopf.place(x = 200, y = 300, width=200, height=100)
    name = Label(fenster, text="Gib deinen Namen ein")
    name.pack()
    name.place(x = 200, y = 100, width = 200, height = 100)
    global eingabefeld
    eingabefeld = Entry(fenster, bd=10, width=50)
    eingabefeld.pack()
    eingabefeld.place(x = 140, y = 180)
    
firststart()
game = Game()
