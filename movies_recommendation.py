# movie_recommendation.py

from movies_database import jasman_database  

 
def minutes_to_time_interval(minutes):
    hours = minutes // 60
    minutes %= 60
    return f"{hours} hours {minutes} minutes" if hours > 0 else f"{minutes} minutes"

def recommend_movie(genre, max_duration, IMDB_RATING):
    recommended_movies = []
    for movie, details in jasman_database.items():
        if genre.lower() in [g.lower() for g in details["genres"]] and details["duration"] <= max_duration and details["IMDB_rating"] == IMDB_RATING:
            recommended_movies.append((movie, details["duration"]))
    
    if recommended_movies:
        print("Based on your preference for", genre.capitalize(), "movies and duration up to", minutes_to_time_interval(max_duration) + ", jasman recommends:")
        for i, (movie, duration) in enumerate(recommended_movies, 1):
            print(f"{i}. {movie} ({minutes_to_time_interval(duration)})")
    else:
        print("Sorry, no movies found in the specified genre and duration range.")


print("Genres available:")
genres_list = list(set([genre for genres in jasman_database.values() for genre in genres["genres"]]))
for i, genre in enumerate(genres_list, 1):
    print(f"{i}. {genre.capitalize()}")

user_genre_choice = int(input("Enter the number corresponding to the genre you are in the mood for: "))

if user_genre_choice in range(1, len(genres_list)+1):
    user_genre = genres_list[user_genre_choice-1]
    
    max_duration = int(input("Enter the maximum duration of the movie you prefer (in minutes): "))
    imdb_check = int(input("Enter the imdb rating of the movie you want to see(0-10): "))
    recommend_movie(user_genre, max_duration, imdb_check)
else:
    print("Invalid input. Please enter a number corresponding to the genre.")
