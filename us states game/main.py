import turtle
import pandas
from tim import Tim
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



score = 0
# t = Tim()

# Data part
data = pandas.read_csv("./50_states.csv")
all_states = data["state"].to_list() 

guessed_states = []

while len(guessed_states) < 50:
  answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name? ").title()
  print(answer_state)
  if answer_state == "Exit":
    break
  if answer_state in all_states:
    guessed_states.append(answer_state)
    t = turtle.Turtle()
    t.hideturtle()
    t.color("black")
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)



# states_to_learn.csv
states_to_learn = []

for i in all_states:
  if i not in guessed_states:
    states_to_learn.append(i)

for i in states_to_learn:
  t = turtle.Turtle()
  t.hideturtle()
  t.color("red")
  t.penup()
  state_data = data[data.state == i]
  t.goto(int(state_data.x), int(state_data.y))
  t.write(i)
  new_data = pandas.DataFrame(states_to_learn)
  new_data.to_csv("states_to_learn.csv")

print(states_to_learn)



screen.exitonclick()