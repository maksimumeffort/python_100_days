from flask import Flask, render_template, request
from post import Post
import requests
import smtplib

# -------SMTP Setup------- #
EMAIL = "throwawaytestemail2@gmail.com"
PASSWORD = "5Tlny6lL45+tj)Nt"
receiver = "alexmaksimets@gmail.com"

def send_email(name, email, phone, text):
    message = f"Name:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{text}\n"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=email, to_addrs=receiver, msg=message)

# -------FLASK------- #

app = Flask(__name__)

blog_url = "https://api.npoint.io/22232e01fb27fb850951"
all_posts = requests.get(blog_url).json()
post_objects = []
AUTHOR = "alex_m"

for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["author"], post["date"])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", submitted=True)
    return render_template("contact.html")


@app.route('/post/<int:index>')
def get_post(index):
    # print(id)
    requested = None
    for obj in post_objects:
        if obj.id == index:
            requested = obj

    return render_template("post.html", post=requested)


if __name__ == "__main__":
    app.run(debug=True)
