import turtle
import pyttsx3


engine = pyttsx3.init()
def square():
    t = turtle.Turtle()
    engine.say("I am drawing a square")
    t.forward(100) #Forward turtle by 100 units
    t.left(90) #Turn turtle by 90 degree
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    turtle.exitonclick()

user_input = input("what would you like me to draw? ")
if user_input == "square":
    square()

# testing
engine.runAndWait()