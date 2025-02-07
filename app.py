from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt

# Flask has been included for the potential of extending the project further in the future!
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Table schema
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(40), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    certification = db.Column(db.String(5), nullable=True)
    runtime = db.Column(db.String(10), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    IMDB_rating = db.Column(db.Float, nullable=False)
    overview = db.Column(db.Text, nullable=True)
    director = db.Column(db.String(50), nullable=False)
    star1 = db.Column(db.String(50), nullable=False)
    star2 = db.Column(db.String(50), nullable=False)
    star3 = db.Column(db.String(50), nullable=False)
    star4 = db.Column(db.String(50), nullable=False)
    no_of_votes = db.Column(db.Float, nullable=True)
    gross = db.Column(db.Float, nullable=True)

## Commands kept incase the SQL database needs to be made again
#with app.app_context():
#        db.create_all()





if __name__ == "__main__":
    app.run(debug=True)
