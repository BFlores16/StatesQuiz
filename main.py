import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Quiz")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="State Name", prompt="Enter a state's name.")
