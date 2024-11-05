import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(740, 500)
background = "blank_states_img.gif"
screen.bgpic(background)

states_content = pd.read_csv("50_states.csv")

state_names = states_content["state"].tolist()
states_x = states_content["x"].tolist()
states_y = states_content["y"].tolist()

states_dict = {
    "states": state_names,
    "x_coor": states_x,
    "y_coor": states_y,
}

printer = turtle.Turtle()
printer.hideturtle()
printer.penup()

right_answers = 0
guesses = []

game_over = False
while not game_over:

    answer_state = screen.textinput(f"{right_answers}/50 Correct Answers", "What's another states name?").title()

    if answer_state == "Exit":
        not_guessed_states = [n for n in state_names if n not in guesses]
        df = pd.DataFrame({
            "States Not Guessed": not_guessed_states
        })
        df.to_csv("game_results.csv")
        game_over = True

    if answer_state in state_names and answer_state not in guesses:
        guesses.append(answer_state)
        index = states_dict["states"].index(answer_state)
        x = int(states_dict["x_coor"][index])
        y = int(states_dict["y_coor"][index])
        printer.goto(x, y)
        printer.write(answer_state, False, "center", ("Courier", 8, "normal"))

        right_answers += 1
    else:
        pass

    if right_answers == 50:
        game_over = True

    if answer_state == "Yes":
        game_over = True

if len(guesses) == 50:
    trophy = "trophy.gif"
    printer.clear()
    screen.bgpic(trophy)
    screen.bgcolor("black")
    printer.goto(0, 140)
    printer.color("white")
    printer.write("YOU GUESSED ALL 50 U.S. STATES", False, "center", ("Courier", 25, "bold"))


turtle.exitonclick()