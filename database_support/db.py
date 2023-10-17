#!/usr/bin/env python3
import urllib.parse

import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://movie:movie@localhost:5432/movie_rating'

db = SQLAlchemy(app)


class MovieRating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=True)


API_BASE_URL = "https://rotten-tomatoes-api.ue.r.appspot.com"


def get_movie_rating(movie_name):
    encoded_movie_name = urllib.parse.quote(movie_name)
    response = requests.get(f"{API_BASE_URL}/movie/{encoded_movie_name}")

    if response.status_code == 200:
        data = response.json()

        tomatometer_rating = data.get("tomatometer", None)

        if tomatometer_rating is not None:
            print(f"Tomatometer rating for {movie_name}: {tomatometer_rating}")
            return float(tomatometer_rating)
        else:
            return None  # Movie not found
    else:
        return None  # API failure


if __name__ == "__main__":
    movie_search = "Pulp%20Fiction"
    movie_rating = get_movie_rating(movie_search)

    new_entry = MovieRating(movie_name=movie_search, rating=movie_rating)
    print(str(new_entry))

    db.session.add(new_entry)
    db.session.commit()
