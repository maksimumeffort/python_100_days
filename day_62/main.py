from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

coffee_ratings_list = ["☕️" * i for i in range(1, 6)]
wifi_ratings_list = ["💪" * i if i > 0 else "✘" for i in range(0, 6)]
power_ratings_list = ["🔌" * i if i > 0 else "✘" for i in range(0, 6)]

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Cafe Location (URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Open Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=coffee_ratings_list, validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices=wifi_ratings_list, validators=[DataRequired()])
    power_rating = SelectField('Power Outlet Rating', choices=power_ratings_list, validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


fields = ["cafe", "location_url", "open_time", "closing_time", "coffee_rating", "wifi_rating", "power_rating"]


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_cafe_info = ",".join([form[item].data for item in fields])
            with open('cafe-data.csv', newline='', mode='a') as file:
                file.write(f"\n{new_cafe_info}\n")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
