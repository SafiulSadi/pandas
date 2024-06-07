from turtle import Turtle
class Tim:
  def __init__(self, x, y, state):
    super().__init__()    
    self.score = 0
    self.x=100
    self.y =100
    self.penup()
    self.hideturtle()
    self.goto(x, y)
    self.write(f"{state}",False,"left",("Arial", 24, "normal"))