from data import data_list

class Book:
    def __init__(self, data_dictionary) -> None:
        self.name = data_dictionary["name"]
        self.author = data_dictionary["author"]
        self.user_rating = data_dictionary["user_rating"]
        self.number_of_reviews = data_dictionary["number_of_reviews"]
        self.price = data_dictionary["price"]
        self.year = data_dictionary["year"]
        self.genre = data_dictionary["genre"]

# def book_name(self):
#     self.name = input('Enter Book Name:     ')

# def book_author(self):
#     self.author = input('Enter Author:      ')

# def book_user_rating(self):
#     self.user_rating = input('Enter User Rating:    ')

# def book_number_of_reviews(self):
#     self.number_of_reviews = input('Enter Reviews:  ')

# def book_price(self):
#     self.price = input('Enter Price:    ')

# def book_year(self):
#     self.year = input('Enter Year:  ')

# def book_genre(self):
#     self.genre = input('Enter Genre:    ')
