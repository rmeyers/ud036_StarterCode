import media
import fresh_tomatoes

# Below creates the three movie instances that we want to display on the site.
toy_story = media.Movie(
    "Toy Story",
    "A story of the boy...",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
)

avatar = media.Movie(
    "Avatar",
    "A marine goes to a new planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)


school_of_rock = media.Movie(
    "School of Rock",
    "Jack Black teaches using rock music",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc"
)

# Add all movie instances to a list so they can easily be passed into the
# HTML-creation function, open_movies_page.
all_movies = [toy_story, avatar, school_of_rock]

fresh_tomatoes.open_movies_page(all_movies)
