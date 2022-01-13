from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():

    year_now = datetime.datetime.now().year
    return render_template("index.html", name="alex_m", year=year_now)


@app.route('/guess/<name>')
def display_name_info(name):
    age = requests.get(f"https://api.agify.io?name={name}").json()
    gender = requests.get(f"https://api.genderize.io?name={name}").json()
    return render_template("index.html", user_age=age, name=name, user_gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/391c35fdc3bed38406fd"
    all_posts = requests.get(blog_url).json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
