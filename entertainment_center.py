from LocalServer.mvoies.fresh_tomatoes import media
from LocalServer.movies.fresh_tomatoes import open_movies_page

# Create instances of media for every movie
life_of_brian = media.Movie("Life of Brian",
                        "Brian Cohen is born in a stable next door to the one in which Jesus is born,"
                        "which initially confuses the who come to praise the future King of the Jews. ",
                        "http://assets.cdn.moviepilot.de/files/48477f5143c8437aff1f276fbabae44fea9860079356a7c7aff5b57a4e44/Das_Leben_des_Brian.jpg",  # NOQA
                        "https://youtu.be/o-wZsE9jlMQ"  # NOQA
                        )

avatar = media.Movie("Avatar",
                     "A man on an alien planet.",
                     "https://resizing.flixster.com/PIhRpOR9nW85stswkSet-W-np_w=/800x1200/v1.bTsxMTE3Njc5MjtqOzE3MDU2OzIwNDg7ODAwOzEyMDA", # NOQA
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8" # NOQA
                     )

snatch = media.Movie("Snatch",
                     "A diamond gets stolen.",
                     "http://assets.cdn.moviepilot.de/files/8b5676c5148cf7fa952a74fcb9e3323be1c6ed98c600f48e994b90999cd1/snatch.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=u8jVN5UAji8"  # NOQA
                     "http://assets.cdn.moviepilot.de/files/8b5676c5148cf7fa952a74fcb9e3323be1c6ed98c600f48e994b90999cd1/snatch.jpg", # NOQA
                     "https://www.youtube.com/watch?v=u8jVN5UAji8" # NOQA
                     )

alien = media.Movie("Alien",
                     "The creature from space.",
                     "http://www.sf-radio.net/filmwelt/images/37,main.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=LjLamj-b0I8"  # NOQA
                     )

thank_you_for_smoking = media.Movie("Thank you for smoking",
                     "A story about a public relations sepcialist in the tobacco industry.",
                     "http://static.rogerebert.com/uploads/movie/movie_poster/thank-you-for-smoking-2006/large_v8PKsbAGIvAhKbbRUjdQ3jgFD2S.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=4GBJOWqlXqE"  # NOQA
                     )

batman_dark_knight = media.Movie("Batman - Dark Knight",
                     "Batman meets the Joker.",
                     "http://vignette3.wikia.nocookie.net/scifi/images/6/65/Joker.jpg/revision/latest?cb=20150606220847&path-prefix=de",  # NOQA
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY"  # NOQA
                     )

# Populate media list for presentation
media_list = [
    life_of_brian,
    avatar,
    snatch,
    alien,
    batman_dark_knight,
    thank_you_for_smoking]

# Create and view movies
open_movies_page(media_list)