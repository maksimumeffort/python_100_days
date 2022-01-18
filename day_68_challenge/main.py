from flask import Flask, render_template, session, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = b'38c012ed7f32a415ca53d870985caf99659efad70fb8976bd6e8374ca913994e'

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        password = request.form.get("password")
        hashed_pass = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=8)
        print(hashed_pass)
        new_user = User(
            name=request.form.get("name"),
            password=hashed_pass,
            email=request.form.get("email")
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email_provided = request.form.get("email")
        password_provided = request.form.get("password")
        print(email_provided)
        user = User.query.filter_by(email=email_provided).first()
        if user:
            login_user(user)
            if check_password_hash(user.password, password_provided):
                return redirect(url_for('secrets'))
            else:
                print("password incorrect")
        else:
            return redirect(url_for('register'))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory('static', filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
