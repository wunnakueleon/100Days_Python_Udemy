import turtle
import pandas

screen = turtle.Screen()
screen.title("Unitest Taste of Amerikca")
image = "day-25-us-states-game-start/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# Data analysis part with pandas
data = pandas.read_csv("day-25-us-states-game-start/50_states.csv")
state_list = data['state'].to_list()

screen.tracer(0)
state_guessed = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title="Guess the staes", prompt="What's another state's name?").title()
    if answer_state in state_list and answer_state not in state_guessed:
        state_match = data['state'] == f'{answer_state}'
        states = data[state_match]['state'].item()
        x_cor = data[state_match]['x'].item()
        y_cor = data[state_match]['y'].item()

        # State's name showing on screen
        letter = turtle.Turtle()
        letter.hideturtle()
        letter.penup()
        letter.goto(x_cor, y_cor)
        letter.write(f"{states}")

        state_guessed.append(answer_state)

    elif answer_state in state_guessed:
        print("You have already guessed the state, guess again!")

    if len(state_guessed) == 50:
        print("You have guessed all the states! Congrats!")
        game_is_on = False
        
    elif answer_state not in state_list:
        print("Try again!")
    screen.update()

screen.mainloop()




