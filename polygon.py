import turtle
import time
print("Hello friends, This is a simple program .This program will help you to Understand The Polygons!\nSO let's get started!!")
ch=1
print("Use this shortcuts:\n\t\tRectangle(1)\n\t\tSquare(2)\n\t\tCircle(3)")
wn=turtle.Screen()
t=turtle.Turtle()
while ch==1:
    a=int(input("Which polygon you want to draw: "))
    if a==1:
        a=int(input("Length : "))
        b=int(input("Breadth : "))
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)
        t.forward(a)
        print("This is a rectangle.Every rectangle have 4 angles and 4 sides.\nThe measure of each angle of rectangle is 90 degrees")
        print("The opposite sides of rectangle are equal.")
        print("Area:"+str(a*b))
        print("Perimeter:" +str(2*(a+b)))
        time.sleep(10)
        t.clear()
        t.reset()
    elif a==2:
        c=int(input("Length: "))
        t.forward(c)
        t.left(90)
        t.forward(c)
        t.left(90)
        t.forward(c)
        t.left(90)
        t.forward(c)
        print("This is a Square.Every square have 4 angles and 4 sides.\nThe measure of each angle of square in 90 degrees ")
        print("All sides of Square are equal.")
        print("Area:"+str(c**2))
        print("Perimeter:"+str(c*4))
        time.sleep(10)
        t.clear()
        t.reset()
    elif a==3:    
        d=int(input("Radius: "))
        t.circle(d)
        print("This is a circle.The circle have infinite radius and diameters.\nThe diameter is the twice of the radius")
        print("Area:"+str(22/7*d**2))
        time.sleep(10)
        t.clear()
        t.reset()
    ch=int(input("Thanks for using this program.\n Do you want to use it again?? (Yes(1),No(0)) : "))