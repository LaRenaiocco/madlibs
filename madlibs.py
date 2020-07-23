"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Get response from user ."""
    answer = request.args.get("play_game")

    if answer == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():
    person = request.args.get("person")
    person_2 = request.args.get("person_2")
    color = request.args.get("color")
    color_2 = request.args.get("color_2")
    noun = request.args.get("noun")
    noun_2 = request.args.get("noun_2")
    noun_3 = request.args.get("noun_3")
    noun_4 = request.args.get("noun_4")
    adjective = request.args.get("adjective")
    adjective_2 = request.args.get("adjective_2")
    time = request.args.get("time")

    return render_template("madlib.html", person=person, person_2=person_2, color=color, color_2=color_2, noun=noun, noun_2=noun_2, noun_3=noun_3, noun_4=noun_4, adjective=adjective, adjective_2=adjective_2, time=time)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
