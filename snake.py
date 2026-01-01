from turtle import Turtle
CORD=[(20,0),(0,0),(-20,0)]

class Snake:
    def __init__(self):
        self.snobj=[]
        self.createsnake()
    def createsnake(self):
        for i in range(3):
            toy = Turtle()
            toy.penup()
            toy.shape("square")
            toy.color("cornsilk1")
            toy.goto(CORD[i])
            self.snobj.append(toy)
        self.head=self.snobj[0]
        self.head.color("moccasin")

    def addseg(self):
        toy=Turtle()
        toy.penup()
        toy.goto(self.snobj[-1].pos())
        toy.shape("square")
        toy.color("cornsilk1")
        self.snobj.append(toy)

    def move(self):
        for i in range(len(self.snobj) - 1, 0, -1):
            self.snobj[i].goto(self.snobj[i - 1].pos())
        self.snobj[0].forward(20)

    def tailcheck(self):
        for i in range(2,len(self.snobj)):
            if self.head.distance(self.snobj[i])<20:
                return False

    def up(self):
        k=self.snobj[0].heading()
        if k!=270:
            self.snobj[0].setheading(90)

    def down(self):
        k = self.snobj[0].heading()
        if k!=90:
            self.snobj[0].setheading(270)

    def left(self):
        k = self.snobj[0].heading()
        if k!=0:
            self.snobj[0].setheading(180)

    def right(self):
        k = self.snobj[0].heading()
        if k!=180:
            self.snobj[0].setheading(0)