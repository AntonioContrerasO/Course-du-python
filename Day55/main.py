import random
from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


@app.route('/')
def start():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<name>/<int:number>")
@make_bold
def greet(name, number):
    return f'Hello {name}, you are {number} years old'


# correct_answer = random.randint(0, 9)
# print(correct_answer)
#
#
# @app.route("/<int:number>")
# def guess(number):
#     if number < correct_answer:
#         return "<h1 style='color:red'>Too low</h1>"\
#                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=200px>"
#     if number > correct_answer:
#         return "<h1 style='color:blue'>Too high</h1>" \
#                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=200px>"
#     if number == correct_answer:
#         return "<h1 style='color:green'>You guessed it</h1>" \
#                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=200px>"
#
#
# @app.route("/bye")
# def bye():
#     return "Bye"


if __name__ == "__main__":
    app.run(debug=True)
