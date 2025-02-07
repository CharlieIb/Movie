import pandas as pd
from app import app, db, Movie


# Load CSV file using pandas
movies_df = pd.read_csv('imdb_top_1000.csv')

## Data clean

# Gross column has commas, they need to be cleaned out
movies_df['Gross'] = pd.to_numeric(movies_df['Gross'], errors='coerce')

# Iterate over the DataFrom rows and insert data into the database
with app.app_context():
    for _, row in movies_df.iterrows():
        movie = Movie(
            title=row['Series_Title'],
            release_year=row['Released_Year'],
            certification=row['Certificate'],
            runtime=row['Runtime'],
            genre=row['Genre'], # There are multiple genres for some movies, consider having to split this variable
            IMDB_rating=row['IMDB_Rating'],
            overview=row['Overview'],
            director=row['Director'],
            star1=row['Star1'],
            star2=row['Star2'],
            star3=row['Star3'],
            star4=row['Star4'],
            no_of_votes=row['No_of_Votes'],
            gross=row['Gross']


        )
        db.session.add(movie)

    # Commit the session
    db.session.commit()

print("Data imported succesfully!")

