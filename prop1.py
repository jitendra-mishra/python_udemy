class Movie:
    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        print("Calling the getter")
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, float) and 1.0 < new_rating <= 5.0:
            print("Calling setter")
            self._rating = new_rating
        else:
            print("Invalid rating")


fav_novie = Movie("Titanic", 4.5)
print(fav_novie.rating)
fav_novie.rating = 4.3
print(fav_novie.rating)