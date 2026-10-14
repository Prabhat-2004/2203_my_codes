class Movie:
    title = "Inception"
    director = 'Christopher Nalon'
    def movie_watched(self):
        print(f"{self.title} has been marked as watched.")
    def display_info(self):
        print(f"Title: {self.title}, Director: {self.director}, Status:{self.status}")
m1 = Movie()
m2 = Movie()
m1.status = "Watched"
m2.status = "Not Watched"
m1.display_info()
m1.movie_watched()
m2.display_info()
