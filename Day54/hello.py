from flask import Flask

app = Flask(__name__)

print(__name__)


def make_bold(funtion):
    def wrapper():
        return "<h1>"+funtion()+"</h1>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello world</h1>' \
           '<p>the paraghap</p>' \
           '<img src="https://i.pinimg.com/originals/e7/44/c8/e744c87f7969f1ab305eef56610e4e2b.jpg" width=200px>'


# different routes using the app.route
@app.route("/bye")
@make_bold
def bye():
    return "Bye"


# Create variable paths
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name} you are {number} "


if __name__ == "__main__":
    app.run(debug=True)
