import turtle

def head(t,size):
    for i in range(36):
        t.forward(20)
        t.left(10)

def eye1(t,size):
    for i in range(90):
        t.forward(1.5)
        t.left(4)

def eye2(t,size):
    for i in range(90):
        t.forward(1.5)
        t.left(4)

def nose(t,size):
    for i in range(8):
        t.forward(20)
        t.left(45)

def h(t,size):
    for i in range(13):
        t.forward(5)
        t.left(30)

def h2(t,size):
    for i in range(13):
        t.forward(5)
        t.left(30)

def eyebrow(t,size):
    for i in range(1):
        t.right(50)
        t.forward(30)

def eyebrow2(t,size):
    for i in range(1):
        t.forward(30)
        t.left(50)
        

def star(t,size):
    for i in range(5):
        t.left(72)
        t.forward(20)
        t.right(144)
        t.forward(20)

def hat(t,size):
    for i in range(3):
         t.forward(90)
         t.right(120)

def ear1(t,size):
    for i in range(90):
        t.forward(3)
        t.left(4)

def ear2(t,size):
    for i in range(90):
        t.forward(3)
        t.left(4)

def mouth(t,size):
    for i in range(2):
        t.right(56)
        t.forward(20)
        t.left(48)
       
        
        
        
        
def main():

    t = turtle.Turtle()
    win = turtle. Screen()
    t.penup()
    t.goto(0,0)
    t.pendown()
    head(t,100)
    t.penup()
    t.goto(50,120)
    t.pendown()
    t.begin_fill()
    eye1(t,30)
    t.end_fill()
    t.penup()
    t.goto(-50,120)
    t.pendown()
    t.begin_fill()
    eye2(t,30)
    t.end_fill()
    t.penup()
    t.goto(-1,50)
    t.pendown()
    t.begin_fill()
    nose(t,50)
    t.end_fill()
    t.penup()
    t.goto(58,130)
    t.color("white")
    t.pendown()
    t.begin_fill()
    h(t,5)
    t.end_fill()
    t.penup()
    t.goto(-40,130)
    t.pendown()
    t.begin_fill()
    h2(t,5)
    t.end_fill()
    t.penup()
    t.goto(-46,180)
    t.color("black")
    t.pendown()
    eyebrow(t,3)
    t.penup()
    t.goto(40,180)
    t.pendown()
    eyebrow2(t,5)
    t.penup()
    t.goto(90,150)
    t.color("yellow")
    t.pendown()
    t.begin_fill()
    star(t,3)
    t.end_fill()
    t.penup()
    t.goto(-45,200)
    t.color("orange")
    t.pendown()
    t.begin_fill()
    hat(t,10)
    t.end_fill()
    t.penup()
    t.goto(-70,200)
    t.color("black")
    t.pendown()
    t.begin_fill()
    ear1(t,10)
    t.end_fill()
    t.penup()
    t.goto(150,210)
    t.color("black")
    t.pendown()
    t.begin_fill()
    ear2(t,10)
    t.end_fill()
    t.penup()
    t.goto(-4,30)
    t.pendown()
    mouth(t,3)
    t.penup()
    t.goto(180,180)
    
    

   
if __name__ == "__main__":
    main()
