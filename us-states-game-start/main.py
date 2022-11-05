# Create a program that marks the location of each USA State base on players input
import turtle
import pandas

"""Creating Screen layout"""
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

"""Accessing Database"""
data = pandas.read_csv("50_states.csv")

"""Creating Variable for Map location"""
state_location = turtle.Turtle()
state_location.color("black")
state_location.hideturtle()
state_location.penup()

"""Creating Game's Logic"""
guessed_states = []
correct_answers = 0
while correct_answers < 50:
    answer_state = screen.textinput(title=f"{correct_answers}/50 correct\nGuess the State",
                                    prompt="What's the State's name?").title()
    if answer_state == "Exit":
        break
    elif answer_state in guessed_states:
        continue
    for state in data["state"]:
        if state == answer_state:
            guessed_states.append(state)
            correct_answers += 1
            new_state = data[data.state == state]
            state_location.goto(int(new_state.x), int(new_state.y))
            state_location.write(f"{state}")
        else:
            continue

"""Creating a database of States that were not answer by the player"""
all_states = data.state.to_list()

missing_states = [state for state in all_states if state not in guessed_states]
states_to_learn = pandas.DataFrame(missing_states)
states_to_learn.to_csv("states_to_learn.csv")

turtle.mainloop()
"""The function below prints the x and y coordinates when clicking on screen"""
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinates)
