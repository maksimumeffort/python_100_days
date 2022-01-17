from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
    #
    #     # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
    #     return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    random_cafe = random.choice(Cafe.query.all())
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def show_all():
    all_cafes = Cafe.query.all()
    # cafe_list = {cafe.id: cafe.to_dict() for cafe in all_cafes}
    # return jsonify(cafes=cafe_list)
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def search():
    param_loc = request.args.get('loc')
    error_message = {"Not Found": "Sorry, we don't have a cafe at that location"}
    cafe = Cafe.query.filter_by(location=param_loc).first()
    # for cafe in all_cafes:
    #     cafe_dict = cafe.to_dict()
    #     if cafe_dict["location"] == location:
    #         return jsonify(cafe=cafe_dict)
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error=error_message)

## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    success_message = {"success": "Successfully added the new cafe"}
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(respone=success_message)


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>",  methods=["PATCH"])
def update(cafe_id):
    new_price = request.form.get("new_price")
    success_message = {"success": "Successfully added the new cafe"}
    error_message = {"Not Found": "Sorry, we don't have a cafe at that location"}
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(respone=success_message), 200
    else:
        return jsonify(respone=error_message), 404

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    success_message = {"success": "Successfully deleted cafe"}
    error_message = {"Not Found": "Sorry, we don't have a cafe at that location"}
    auth_error_message = {"error": "Sorry, that's not allowed. Make sure you have the correct api_key"}
    key_provided = request.form.get("api-key")
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        if key_provided == "TopSecretAPIKey":
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(respone=success_message), 200
        else:
            return jsonify(respone=auth_error_message), 403
    else:
        return jsonify(respone=error_message), 404



if __name__ == '__main__':
    app.run(debug=True)
