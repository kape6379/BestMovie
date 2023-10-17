-- V1__initial_schema.sql
CREATE TABLE movie_rating (
  id serial PRIMARY KEY,
  datetime timestamp without time zone DEFAULT current_timestamp,
  movie_name varchar(255) NOT NULL,
  rating double precision
);
