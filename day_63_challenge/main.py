from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ------------------- DB Setup -------------------#

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()
# ------------------- Flask App Setup -------------------#


@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template("index.html", books=all_books)


@app.route('/edit',  methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        update_book = Book.query.get(request.form["id"])
        update_book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get('id')
    selected_book = Book.query.get(book_id)
    return render_template("edit.html", book=selected_book)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["book_name"],
            author=request.form["book_author"],
            rating=request.form["book_rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

