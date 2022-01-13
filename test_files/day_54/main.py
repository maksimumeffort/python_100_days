from flask import Flask

app = Flask(__name__)

#FUNCTIONS

def make_bold(function):
    def wrapper():
        content = function()
        return f"<b>{content}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        content = function()
        return f"<em>{content}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        content = function()
        return f"<u>{content}</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)