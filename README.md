
# Movie Recommendation system


## Description
A brief overview of the project:
- What does it do?
  - This application will allow you to pull from the imdb database and find recommendations to new films to watch. 
  - You can filter the desired content
  - you can stipulate those movies that you have liked or watched before and the system will recommend to you movies that you should like
  - Then the system will recommend movies
- Why was it built?
- What problem does it solve?
  - On those nights where you and perhaps those you love are looking for a movie and trawling through the endless lists of movies
  - Even if they are catagorised by genre, they are never quite what you are looking for.
  - They are:
    - limited by the platform that you are streaming from
    - they are sometimes pushing those movies that they produced internally
    - They offer choice, and recommendations, but not always surprise

## Features
System:
This project creates a simple movie recommendation system through the use of the packages scikit-learn and pandas
- Movie recommendations
  - Using content markers (Overview, Director, Genre) and an input movie this program produces another film that is likely to be similar in content/style.
  - e.g. if you Enter Pulp Fiction the recommendation will be Django Unchained.
  - The database used for this sytem is IMDB top 1000 movies
  - Extension to the system:
    - I could also include:
      - region the movie was made

- Alternatives/Improvements:
  - I would like to test out user preference systems and if possible incorporate them into these functions to see how these two methods differ.
  

## Installation
Software requirements:
- This has been run and tested on Python 3.12
- Additional requirements can be found in requirements.txt

Please note:
- Flask web framework and SqlAlchemy are not necessarily needed

Flask has been included for the potential of expanding this project to a web based service
SQL is my preference for database storage for this project. However, for testing this could be omitted.

### Steps to Install
- Flask web framework
- SQLAlchemy for database management
- 

## Usage

### write in the command line:

flask run movie.py