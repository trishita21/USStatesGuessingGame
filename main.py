import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape((image))


# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")

turtle_obj = turtle.Turtle()
turtle_obj.penup()
turtle_obj.hideturtle()
turtle_obj.color("black")
state_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct",
                                    prompt="What's another state's name ?").title()

    if answer_state == "Exit":
        break;

    ans_data = data[data.state == answer_state]
    if answer_state in state_list:
        guessed_states.append(answer_state)

        x = int(ans_data.x)
        y = int(ans_data.y)

        turtle_obj.goto(x=x,y=y)
        turtle_obj.write(answer_state, font=("Arial",8,"normal"))


not_guessed = [ state for state in state_list if state not in guessed_states ]

ng = pandas.DataFrame(not_guessed)
ng.to_csv("states_to_learn.csv")