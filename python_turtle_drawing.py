import turtle


def square(t,size):
    for i in range(4):
        t.forward(size)
        t.right(90)
        
       
        

def triangle(t,size):
    for i in range(3):
         t.forward(size)
         t.left(120)

def circle(t,size):
    for i in range(360):
        t.speed(1)
        t.forward(1)
        t.left(1)

def pentagon(t,size):
    for i in range(5):
        t.forward(100)
        t.left(72)
    
def star(t,size):
    for i in range(5):
        t.left(72)
        t.forward(size)
        t.right(144)
        t.forward(size)

def polygon(sides, size):
    angle = 360 / sides
    for i in range(sides):
        turtle.forward(size)
        turtle.right(angle)
         
        
        
def main():

    t = turtle.Turtle()
    win = turtle. Screen()
    t.penup()
    t.goto(-200,140)
    t.pendown()
    square(t,100)
    t.penup()
    t.goto(200,100)
    t.pendown()
    triangle(t,100)
    t.penup()
    t.goto(10,10)
    t.pendown()
    pentagon(t,100)
    t.penup()
    t.goto(-100,-100)
    t.pendown()
    circle(t,20)
    t.penup()
    t.goto(-150,-180)
    t.pendown()
    star(t,60)
    t.penup()
    t.goto(-50,50)
    t.pendown()
    polygon(7,60)
if __name__ == "__main__":
    main()
