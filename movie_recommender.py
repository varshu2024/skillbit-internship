# Sample movie database
movies = [
    {"title": "Inception", "genre": ["Action", "Sci-Fi", "Thriller"]},
    {"title": "The Matrix", "genre": ["Action", "Sci-Fi"]},
    {"title": "Titanic", "genre": ["Romance", "Drama"]},
    {"title": "The Notebook", "genre": ["Romance", "Drama"]},
    {"title": "Avengers: Endgame", "genre": ["Action", "Adventure", "Sci-Fi"]},
    {"title": "Interstellar", "genre": ["Adventure", "Drama", "Sci-Fi"]},
    {"title": "The Godfather", "genre": ["Crime", "Drama"]},
    {"title": "The Dark Knight", "genre": ["Action", "Crime", "Drama"]},
    {"title": "Frozen", "genre": ["Animation", "Family", "Adventure"]},
    {"title": "Toy Story", "genre": ["Animation", "Family", "Comedy"]},
]

def find_movie(title):
    for movie in movies:
        if movie["title"].lower() == title.lower():
            return movie
    return None

def recommend_movies(fav_movie):
    print(f"\n🎯 Based on your interest in '{fav_movie['title']}', you might like:")
    fav_genres = set(fav_movie["genre"])
    recommendations = []

    for movie in movies:
        if movie["title"] == fav_movie["title"]:
            continue
        similarity = len(fav_genres.intersection(set(movie["genre"])))
        if similarity > 0:
            recommendations.append((movie["title"], similarity))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    for title, score in recommendations[:5]:
        print(f"• {title}")

def main():
    print("🎥 Welcome to the Movie Recommender!")
    print("Here are some movies you can choose from:")
    for movie in movies:
        print(f"• {movie['title']}")

    choice = input("\nEnter the name of a movie you like: ")
    selected_movie = find_movie(choice)

    if selected_movie:
        recommend_movies(selected_movie)
    else:
        print("❌ Sorry, movie not found in database.")

if __name__ == "__main__":
    main()
