import media
import json
import fresh_tomatoes
import person


# Open the JSON file containing the movie data
with open('movies.json', 'r') as movies_json_file:
    # Parse the JSON file
    movies_json = json.load(movies_json_file)

# JSON data has been loaded, the file is no longer needed so we
# can safely close it.
movies_json_file.close()

# Initialise the movies array so we can refer to it outside
# of the for loop block and pass through to Fresh Tomatoes.
movies = []

for movie_json in movies_json["movies"]:
    # Pass the director JSON data to the Director constructor
    director = person.Director(movie_json["director"]["first_name"],
                               movie_json["director"]["last_name"],
                               movie_json["director"]["gender"],
                               movie_json["director"]["imdb_url"])

    # Pass the movie JSON data and the director object to the Movie
    # constructor
    movie = media.Movie(movie_json["title"], movie_json["duration"],
                        movie_json["storyline"], movie_json["poster_url"],
                        movie_json["youtube_trailer_url"], director)

    # Append the newly created movie to the movies array
    movies.append(movie)

# Send the movies array to the Fresh Tomatoes package and
# open the movies page
fresh_tomatoes.open_movies_page(movies)
