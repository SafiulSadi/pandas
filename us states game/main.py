import turtle
import pandas
from tim import Tim
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name? ")
answer_state = answer_state.lower()
print(answer_state)

score = 0
# t = Tim()

# Data part
data = pandas.read_csv("./50_states.csv")
all_states = data["state"].to_list()



if answer_state in all_states:
  t = turtle.Turtle()
  t.hideturtle()
  t.penup()
  state_data = data[data.state == answer_state]
  t.goto(int(state_data.x), int(state_data.y))
  t.write(answer_state)



screen.exitonclick()