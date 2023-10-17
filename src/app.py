#!/usr/bin/env python3
import urllib
import os
import requests
from flask import Flask, request, jsonify, render_template
from database_support.db import db, MovieRating, get_movie_rating
from urllib.parse import unquote

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")


db.init_app(app)


@app.route("/")
def list_movies():
    movies = MovieRating.query.all()
    return render_template("movies.html", movies=movies)


@app.route("/best_movies")
def best_movies():
    bestmovies = MovieRating.query.filter(MovieRating.rating >= 90).all()
    return render_template("best_movies.html", bestmovies=bestmovies)


@app.route('/add_movie', methods=['POST'])
def add_movie():
    try:
        data = request.get_json()
        title = data.get('movie_name')
        encoded_title = urllib.parse.quote(title)

        rating = get_movie_rating(encoded_title)
        app.logger.info(f"Title: {encoded_title}, Rating: {rating}")
        if title is None:
            return jsonify({'error': 'Title is required'}), 400
        if rating is None:
            return jsonify({'error': 'Movie not found or API failure'}), 404  # Return a 404 status for clarity

        movie = MovieRating(movie_name=title, rating=rating)
        db.session.add(movie)
        db.session.commit()

        return jsonify({'message': 'Movie added successfully'}), 201
    except Exception as e:
        error_message = str(e)
        app.logger.error(str(e))
        return jsonify({'error': error_message}), 500


API_BASE_URL = "https://rotten-tomatoes-api.ue.r.appspot.com"


@app.route('/get_movie', methods=['GET'])
def get_movie():
    movie_name = request.args.get('movie_name')

    if movie_name is None:
        return jsonify({'error': 'Title is required'}), 400

    response = requests.get(f"{API_BASE_URL}/movie/{movie_name}")

    if response.status_code == 200:
        movie_data = response.json()
        return jsonify(movie_data), 200
    elif response.status_code == 404:
        return jsonify({'error': 'Movie not found'}), 404
    else:
        return jsonify({'error': 'API Failure'}), 500
