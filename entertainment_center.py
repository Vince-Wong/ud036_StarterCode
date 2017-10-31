import media
import fresh_tomatoes

the_dark_knight = media.Movie("The Dark Knight",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",  # NOQA
                     "https://youtu.be/EXeTwQWrcwY")

inception = media.Movie("Inception",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # NOQA
                        "https://youtu.be/YoHD9XEInc0")

big_hero_6 = media.Movie("Big Hero 6",
                         "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",  # NOQA
                         "https://youtu.be/z3biFxZIJOQ")

baby_driver = media.Movie("Baby Driver",
                          "https://upload.wikimedia.org/wikipedia/en/8/8e/Baby_Driver_poster.jpg",  # NOQA
                          "https://youtu.be/z2z857RSfhk")

wonder_women = media.Movie("Wonder Women",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",  # NOQA
                           "https://youtu.be/VSB4wGIdDwo")

blade_runner_2049 = media.Movie("Blade Runner 2049",
                                "https://upload.wikimedia.org/wikipedia/en/9/9b/Blade_Runner_2049_poster.png",  # NOQA
                                "https://youtu.be/gCcx85zbxz4")


movies = [the_dark_knight, inception, big_hero_6, baby_driver, wonder_women,
          blade_runner_2049]

fresh_tomatoes.open_movies_page(movies)
