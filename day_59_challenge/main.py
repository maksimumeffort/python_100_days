from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/22232e01fb27fb850951"
all_posts = requests.get(blog_url).json()
post_objects = []
AUTHOR = "alex_m"

for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["author"], post["date"])
    post_objects.append(post_obj)

@app.route('/index')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
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
