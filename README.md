# BestMovie
Applications of Software Architecture
## About
This app fetches movie info from the RottenTomatoes API. Please ensure you are in the project directory for BestMovie. Please ensure that you have flask, flyway, sqlalchemy, and postgresql installed. 
## Features
- This app collects data that users input into the UI.
- This app analyzes this data by categorizing movies with a tomatometer rating of 90+ as a "best movie" on a separate page.
- This app features data persistence using PostgreSQL.
- This app features api collaboration with the RottenTomatoes API to get movie ratings.
- This app features unit tests to ensure functionality. 
## Setting Up
1. Set up environment: source venv/bin/activate
2. Set entry point for my application: export FLASK_APP=src.app
3. Create a PostgreSQL database: createdb 
4. Create _movie_rating_ database: psql -c "create database movie_rating;"
5. Create user _'movie'_ with password _'movie'_: psql -c "create user movie with password 'movie';"
6. Run migrations before running by entering "flyway -user=movie -password=movie -url="jdbc:postgresql://localhost:5432/movie_rating" -locations=filesystem:"databases/movie" migrate". [!WARNING] Running the migrations with "clean" may delete crucial parts of the database. Please refrain from doing so. If this happens, you may need to create a new movie_rating database or configure appropriately.
7. Run the app using "flask run" in your terminal.

## Run the App Locally
Due to issues with heroku deployment, this application is only available locally. After manually setting up the databases and setting the environment, you can get a look into this apps functionality.
- Please ensure you have psycopg2, flask_sqlalchemy, and pip install requests all in your environment. 
- Please triple check that you've set the entry point with export FLASK_APP=src.app and that you've activated the environment using source venv/bin/activate.
- You should be ready to input flask run into your terminal. 

# Unit Tests
I have written a unit test to check if the app starts in addition to if best movie is functioning properly. Please run python -m unittest tests/test_app.py.

## Fetching Data
In order to ensure that my application is fetching data from an external source, please run "curl -X GET http://127.0.0.1:5000/get_movie?movie_name=Beetlejuice" to get the movie info for "BeetleJuice". Feel free to update this curl command to look for different movies as well. In doing so, please ensure that your spelling and formatting are correct, otherwise it might not be able to fetch your specific searches/improper queries from the API. For movies with special characters please replace with the listed guide: 
1. Space: %20
2. Question mark: %3F
3. Ampersand: %26
4. Equals sign: %3D
5. Slash (forward slash): %2F
6. Colon: %3A
7. Comma: %2C
8. Parentheses: %28 for ( and %29 for )
9. Square brackets: %5B for [ and %5D for ]. 

For example: for Pulp Fiction enter: "curl -X GET http://127.0.0.1:5000/get_movie?movie_name=Pulp%20Fiction". 
## Storing Data
In order to add to the movie 'Casablanca' to the database, please run "curl -X POST -H "Content-Type: application/json" -d '{"movie_name": "Casablanca"}' http://127.0.0.1:5000/add_movie". If you run "psql -U movie -d movie_rating", and "SELECT * FROM movie_rating;" in your terminal, you should be able to see the added entry, in addition to other entries. Feel free to add mother movies.
