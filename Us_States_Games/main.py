import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
correct_guesses = []

game_on = True
while game_on:
    if len(correct_guesses) < 50:
        answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Guess the state's name").title()
        if answer_state == "Exit":
            missing_states = []
            for state in states:
                if state not in correct_guesses:
                    missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break
        if answer_state in states:
            # Jalar las coordenadas de cada estado.
            x_cor = int(data[data["state"] == answer_state]['x'].values[0])
            y_cor = int(data[data["state"] == answer_state]['y'].values[0])

            # Escribir el estado en el mapa
            turtle.penup()
            turtle.tracer(0.5)
            turtle.goto(x_cor, y_cor)
            turtle.write(answer_state)

            # Guardar Respuestas Adivinadas
            correct_guesses.append(answer_state)
    else:
        game_on = False
        turtle.exitonclick()
        print("Thanks for playing")



# states_to_learn.csv





















































