from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/391c35fdc3bed38406fd"
all_posts = requests.get(blog_url).json()
post_objects = []
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:index>')
def get_post(index):
    print(id)
    requested = None
    for obj in post_objects:
        if obj.id == index:
            requested = obj

    return render_template("post.html", post=requested)

if __name__ == "__main__":
    app.run(debug=True)
