import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
MTDB_KEY = os.environ['MTDB_KEY']
MTDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MTDB_SELECT_URL = "https://api.themoviedb.org/3/movie"

# ------------------- Flask Form Setup-------------------#

class EditForm(FlaskForm):
    rating = StringField('Your Rating Out of 10', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


# ------------------- DB Setup -------------------#

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=True)
    year = db.Column(db.String(250), nullable=True)
    description = db.Column(db.Integer(), nullable=True)
    rating = db.Column(db.String(250), nullable=True)
    ranking = db.Column(db.String(250), nullable=True)
    review = db.Column(db.Integer(), nullable=True)
    img_url = db.Column(db.String(250), nullable=True)

db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(desc(Movie.rating)).all()
    i = 1
    for movie in all_movies:
        movie.ranking = i
        i += 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route('/edit', methods=["GET", "POST"])
def edit():
    movie_id = request.args.get("id")
    selected_movie = Movie.query.get(movie_id)
    form = EditForm()
    if request.method == "POST":
        if form.validate_on_submit():
            selected_movie.review = request.form["review"]
            selected_movie.rating = request.form["rating"]
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("edit.html", movie=selected_movie, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get("id")
    selected_movie = Movie.query.get(movie_id)
    db.session.delete(selected_movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddForm()
    # ------------------- MTDB Setup-------------------#
    if form.validate_on_submit():
        movie_title = request.form["title"]
        response = requests.get(MTDB_SEARCH_URL, params={"api_key": {MTDB_KEY}, "query": {movie_title}})
        data = response.json()["results"]

        return render_template('select.html', movie_options=data)

    return render_template('add.html', add_form=form)

@app.route('/select')
def select():
    movie_id = request.args.get("id")
    select_movie_url= f"{MTDB_SELECT_URL}/{movie_id}"
    image_url = "https://image.tmdb.org/t/p/w500"
    response = requests.get(select_movie_url, params={"api_key": {MTDB_KEY}})
    data = response.json()
    new_movie = Movie(title=data["title"], img_url=f"{image_url}{data['poster_path']}", year=data["release_date"].split("-")[0], description=data["overview"])
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
