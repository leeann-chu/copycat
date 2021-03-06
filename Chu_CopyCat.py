#LeeAnn Chu
#1-11-19
#written in python 3.6.3

from turtle import*
import time
import random

#Setup
setup()
s = Screen()
s.bgcolor("black")
title ("Welcome to the game of Copy Cat")

    #Variables
colors = ["R", "Y", "B", "G"]
seq = []
useq= []

    #Setting up turtles
        #Buttons
tred = Turtle()
tyellow = Turtle()
tblue = Turtle()
tgreen = Turtle()

pplay = Turtle()
ppause = Turtle()
tplay = Turtle()
legend = Turtle()

pred = Turtle()
pred.speed("fastest")
tred.speed("fastest")
gred = Turtle()
gred.speed("fastest")

pyellow = Turtle()
pyellow.speed("fastest")
tyellow.speed("fastest")
gyellow = Turtle()
gyellow.speed("fastest")

pblue = Turtle()
tblue.speed("fastest")
pblue.speed("fastest")
gblue = Turtle()
gblue.speed("fastest")

pgreen = Turtle()
pgreen.speed("fastest")
tgreen.speed("fastest")
ggreen = Turtle()
ggreen.speed("fastest")

tred.up()
tyellow.up()
tblue.up()
tgreen.up()

    #Positions
pgreen.goto(190,-160)
pblue.goto(-190,-160)
pyellow.goto(-185,160)
pred.goto(160,160)

ggreen.goto(160,-160)
gblue.goto(-170,-160)
gyellow.goto(-170,160)
gred.goto(160,160)

#Setup Pictures
    #Setup Background
register_shape("yellow.gif")
pyellow.shape("yellow.gif")

register_shape("red.gif")
pred.shape("red.gif")

register_shape("blue.gif")
pblue.shape("blue.gif")

register_shape("green.gif")
pgreen.shape("green.gif")


    #Setup Foreground
register_shape("redlit.gif")
gred.shape("redlit.gif")

register_shape("yellowlit.gif")
gyellow.shape("yellowlit.gif")

register_shape("greenlit.gif")
ggreen.shape("greenlit.gif")

register_shape("legend.gif")
legend.shape("legend.gif")
legend.up()
legend.ht()
legend.goto(-315,-275)

register_shape("bluelit.gif")
gblue.shape("bluelit.gif")

register_shape("play.gif")
pplay.shape("play.gif")
register_shape("pause.gif")
ppause.shape("pause.gif")
pplay.goto(-5,5)
ppause.goto(-5,5)

text = Turtle(visible=False)
text.speed("fastest")
text.up()

tscore = Turtle(visible=False)
tscore.speed("fastest")
tscore.up()

#Hide Foreground
gred.ht()
gyellow.ht()
gblue.ht()
ggreen.ht()

ppause.ht()

    #Colors
        #Darks
tred.color("#950000")
tyellow.color("#929200")
tblue.color("#005fa1")
tgreen.color("#009200")

tplay.color("#FEFFFE")

text.color("white")
text.goto (-350,180)

tscore.color("white")
tscore.goto(160,-300)

        #Brights
##tred.color("#e60000")
##tyellow.color("#fff200")
##tblue.color("#0096ff")
##tgreen.color("#00e600")

    #Button Setup
tred.goto(160,160)
tred.shape("circle")
tred.shapesize(6,6)

tyellow.goto(-175,170)
tyellow.shape("circle")
tyellow.shapesize(6,6)

tblue.goto(-170,-160)
tblue.shape("circle")
tblue.shapesize(6,6)

tgreen.goto(170,-155)
tgreen.shape("circle")
tgreen.shapesize(6,6)

    #Play/Pause Button
tplay.goto(-5.5,5)
tplay.shape("circle")
tplay.shapesize(3.5,3)

    #Legend
legend.st()

#Function Defining
    #Computer Clicks
def redPressed():
    gred.st()
    tred.color("#e60000")
    time.sleep(.35)
    tred.color("#950000")
    gred.ht()

def yellowPressed():
    gyellow.st()
    tyellow.color("#fff200")
    time.sleep(.35)
    tyellow.color("#929200")
    gyellow.ht()

def bluePressed():
    gblue.st()
    tblue.color("#0096ff")
    time.sleep(.35)
    gblue.hideturtle()
    tblue.color("#005fa1")

def greenPressed():
    ggreen.st()
    tgreen.color("#00e600")
    time.sleep(.35)
    tgreen.color("#009200")
    ggreen.ht()

    #User Clicks
def tredClicked(x,y):
    global wait
    wait = True
    gred.st()
    tred.color("#e60000")
    useq.append("R")
    time.sleep(.35)
    tred.color("#950000")
    gred.ht()

def tyellowClicked(x,y):
    global wait
    wait = True
    gyellow.st()
    tyellow.color("#fff200")
    useq.append("Y")
    time.sleep(.35)
    tyellow.color("#929200")
    gyellow.ht()

def tblueClicked(x,y):
    global wait
    wait = True
    gblue.st()
    tblue.color("#0096ff")
    useq.append("B")
    time.sleep(.35)
    gblue.hideturtle()
    tblue.color("#005fa1")

def tgreenClicked(x,y):
    global wait
    wait = True
    ggreen.st()
    tgreen.color("#00e600")
    useq.append("G")
    time.sleep(.35)
    tgreen.color("#009200")
    ggreen.ht()

    #User Key Presses
def tredPressed():
    global wait
    wait = True
    gred.st()
    tred.color("#e60000")
    useq.append("R")
    time.sleep(.25)
    tred.color("#950000")
    gred.ht()

def tyellowPressed():
    global wait
    wait = True
    gyellow.st()
    tyellow.color("#fff200")
    useq.append("Y")
    time.sleep(.25)
    tyellow.color("#929200")
    gyellow.ht()

def tbluePressed():
    global wait
    wait = True
    gblue.st()
    tblue.color("#0096ff")
    useq.append("B")
    time.sleep(.25)
    gblue.hideturtle()
    tblue.color("#005fa1")

def tgreenPressed():
    global wait
    wait = True
    ggreen.st()
    tgreen.color("#00e600")
    useq.append("G")
    time.sleep(.25)
    tgreen.color("#009200")
    ggreen.ht()

    ###################
def playClicked(x,y):
    global start
    start = True
    pplay.ht()
    ppause.st()
    text.clear()

def playPressed():
    global start
    start = True
    pplay.ht()
    ppause.st()
    text.clear()

def playunPressed(x,y):
    global seq
    ppause.ht()
    pplay.st()
    seq = []
    text.clear()

    ###############
def randColor():
    global color
    color = random.choice(colors)

def sequence():
    print("Sequence:",seq,"\nUser Input:",useq)
def clear():
    global useq
    useq = []
    print("User Input:",useq)

def fail():
    global end
    ppause.ht()
    pplay.st()
    text.clear()
    tscore.clear()
    end = "y"

def stop(x,y):
    global end
    ppause.ht()
    pplay.st()
    text.clear()
    tscore.clear()
    end = "y"


#MainProcessing
listen()
pause = False
go = True
start = False
write = True
play = False
wait = False
end = 0
score = 0
n = 0

while go == True:
    tscore.write("Score: %s" % str(score), font=("Impact",35))
    if write == True:
        write = False
        text.write("Welcome to the game of Copy Cat! \nHit the play button to begin.", font=("Impact", 35))
    while start==False:
        tplay.onclick(playClicked)
        onkey(playPressed, "p")

    while start==True:
        if write == False:
            text.write("Copy the order of the flashing \ncolors.", font=("Impact", 35))
        while pause == False:
            randColor()
            seq.append(color)
            useq = []
            length = len(seq)
            tplay.onclick(stop)
            time.sleep(0.25)

        #Show the Sequence
            for n in range (0,length):
                if seq[n] == "R":
                    redPressed()
                       
                if seq[n] == "Y":
                   yellowPressed()
                   
                if seq[n] == "B":
                    bluePressed()
                   
                if seq[n] == "G":
                   greenPressed()
                write = True
                pause = True
                text.clear()
                    
                #Copy the Sequence
            while pause == True:
                tred.onclick(tredClicked)
                tyellow.onclick(tyellowClicked)
                tblue.onclick(tblueClicked)
                tgreen.onclick(tgreenClicked)
                onkey(tredPressed, "r")
                onkey(tyellowPressed, "y")
                onkey(tbluePressed, "b")
                onkey(tgreenPressed, "g")
                onkey(sequence, "s")
                onkey(fail, "q")
                onkey(clear, "c")
                
                if end == "y":
                    while (end != "y" and end != "n"):
                        end = str(input("Would you like to end the program (y/n): "))
                    if end == "y":
                        print("We're sorry to see you go, have a nice day!")
                        fin = input("Please hit enter to end:")
                        quit()
                    else:
                        sequence()
                else:                     
                    while wait == True:
                        tscore.clear()
                        if useq == seq:
                            tscore.write("Score: %s" % str(score), font=("Impact",35))
                            score += 1
                            wait = False
                            pause = False
                            wrong = 0
                            useq = []
                        else:
                            wait = False
                            pause = True
                            wrong += 1
                                
                            if wrong >= 10:
                                useq = seq
                                                     
               
                while n <= length:
                    n+=1 


