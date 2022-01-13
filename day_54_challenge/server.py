from flask import Flask
from random import randint

app = Flask(__name__)

rand_num = randint(1, 9)

def output_selector(function):
    def wrapper(number):
        if int(number) < rand_num:
            return f"<h1 style='color:red'>{function(number)}</h1>" \
                    "<img src='https://media.giphy.com/media/efOj1WU30B9M1LzNFw/giphy.gif'>"
        elif int(number) > rand_num:
            return f"<h1 style='color:purple'>{function(number)}</h1>" \
                    "<img src='https://media.giphy.com/media/VbRY6pfcQpTkk/giphy.gif'>"
        else:
            return f"<h1 style='color:green'>{function(number)}</h1>"\
                    "<img src='https://media.giphy.com/media/PjWCuIvrwBL8s/giphy.gif'>"
    return wrapper

@app.route("/")
def hello():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/AWv3UAFkgz39u/giphy.gif'>"

@app.route("/<number>")
@output_selector
def show_num(number):
    if int(number) == rand_num:
        return f'You got it!'
    elif int(number) < rand_num:
        return f'Too low, try again!'
    else:
        return f'Too high, try again!'

#RUN
if __name__ == "__main__":
    app.run(debug=True)

