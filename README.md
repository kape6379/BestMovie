# BestMovie
Applications of Software Architecture
## About
This app fetches movie info from the RottenTomatoes API. Please ensure that you have flask, flyway and postgresql installed. For migrations, please run  this command in your terminal "flyway -user=movie -password=movie -url="jdbc:postgresql://localhost:5432/movie_rating" -locations=filesystem:"databases/movie" migrate clean"
## Fetching Data
In order to ensure that my application is fetching data from an external source, please run "curl -X GET http://127.0.0.1:5000/get_movie?movie_name=Beetlejuice" to get the movie info for "BeetleJuice". Feel free to update this curl command to look for different movies as well.
## Storing Data
In order to add to the movie 'Casablanca' to the database, please run "curl -X POST -H "Content-Type: application/json" -d '{"movie_name": "Casablanca", "rating": 9.9}' http://127.0.0.1:5000/add_movie". If you run "psql -U movie -d movie_rating", and "SELECT * FROM movie_rating;" in your terminal, you should be able to see the added entry, in addition to other entries. Feel free to add mother movies.

