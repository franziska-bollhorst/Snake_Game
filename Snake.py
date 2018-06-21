"""
Informatik Projekt 2018
Thema:  Snake
Erstellt von: Adrian Bergen(), Lukas Hansen(4463302), Fanziska Bollhorst (4463145)


"""
import tkinter as tk
from tkinter import *
from random import randint
import socket

s=socket.socket()                                                  
s.connect(('192.168.43.51', 30303))
s.setblocking(True)

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

class Game(tk.Tk):
    def createbutton(self):
        """Hier wird ein Knopf erstellt, nachdem man bei dem Snakespiel verliert.
        Dieser Knopf dient dazu das Spiel neu zu starten. Des Weiteren
        wird ein Textfeld erstellt. Dieses benachrichtigt dich, dass du verloren hast.
        """
        global knopf
        knopf=tk.Button(w,text="Neustart", fg='Azure', bg='#87ceeb', activebackground='#8470ff', command=self.restart)
        knopf.pack()
        w.create_window(250,10,anchor=tk.N,window=knopf)
        global verlorentext
        verlorentext = w.create_text((250, 475), text="DU HAST VERLOREN")

    def ticker(self):                                                 
        """Alle 0,6 Sekunden erhält er vom Arduino die Richtung für die Schlange und führt die Definition drawnsnake aus, falls das Spiel verloren wird (lost=True),
        dann springt er in die Definition creatbutton.
        """
        self.receivearduino()
        
        if(lost==False):
            self.drawsnake()
            self.after(600,self.ticker)

        else:
            self.createbutton()
            
    
    def drawsnake(self):
        """Hier wird die Schlange
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

        self.changedirection()
        
        if(feedcollision == False)and(lost == False):                                 
            w.create_rectangle(25+xcoordinate[0]*25, 25+ycoordinate[0]*25, 25+xcoordinate[0]*25+size, 25+ycoordinate[0]*25+size, outline="#87ceeb", fill="#87ceeb")
            
        if(lost==False):
            w.create_rectangle(25+(xcoordinate[len(xcoordinate)-1])*25, 25+(ycoordinate[len(ycoordinate)-1])*25, 25+(xcoordinate[len(xcoordinate)-1])*25+size, 25+(ycoordinate[len(ycoordinate)-1])*25+size, outline="#556b2f", fill="#556b2f")

        if(len(xcoordinate)>length):
            del xcoordinate[0],ycoordinate[0]
        
        print("x: ", xcoordinate)
        print("y: ", ycoordinate)


    def feedpoint(self):
        """TEST1
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
        """TEST 2
        """
        global feedpoint
        feedpoint=[randint(1,16),randint(1,16)]
        for i in range(0,(length-1)):
            if(feedpoint[0] == xcoordinate[i]):
                if(feedpoint[1] == ycoordinate[i]):
                    self.createfeedpoint()                        
        w.create_rectangle(25+feedpoint[0]*25, 25+feedpoint[1]*25, 25+feedpoint[0]*25+size, 25+feedpoint[1]*25+size, outline="#ff4500", fill="#ff4500")


    def collisions(self):
        """TEST 3
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

    def changedirection(self):
        """TEST 4
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
        """TEST 5
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
        """TEST 6
        """
        global direction
            
        z = s.recv(1024) 
        if ('u' in str(z))and(direction!=1):
            print ("unten")
            direction=3
        elif ('re' in str(z))and(direction!=4):
            print ('rechts')
            direction=2
        elif ('l' in str(z))and(direction!=2):
            print ('links')
            direction=4
        elif ('o' in str(z))and(direction!=3):
            print ('oben')
            direction=1


def createfield():
    """TEST 7
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
game = Game()
