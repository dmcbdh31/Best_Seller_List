from statistics import mean
from data import data_list
from book import Book


def run_analysis(book_list):
    books = create_book_list(book_list)
    print('')
    print("*******************************************************************")
    print('')
    example_analysis(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_one(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_two(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_three(books)


def create_book_list(data_list):
    book_list = []
    # TODO: Write a function that will loop through data_list, and create a Book object for each list item
    # TODO: Then, add each Book item to book_list
    # TODO: Finally, return book_list for use in analysis questions!
    for item in data_list:
        new_book = Book(item)
        book_list.append(new_book)
    return book_list


def example_analysis(book_list):
    print("Analysis of which book had the highest price in 2016")
    # Find all books from 2016
    # Use a Lambda filter function to find books who have a year of 2016
    # Converting to a list, and saving as variable books_2016
    books_2016 = list(filter(lambda book: book.year == 2016, book_list))
    # Calculating the maximum price, and saving that book as highest_cost_book
    # Using max(), with Lambda function
    highest_cost_book = max(books_2016, key=lambda book: book.price)
    # Print that book's name & price to terminal
    print(
        f"The most expensive book in 2016 was {highest_cost_book.name} with a price of {highest_cost_book.price}")


def analysis_one(book_list):
    print("Analysis of which book had the lowest number of reviews in 2018")
    books_2018 = list(filter(lambda book: book.year == 2018, book_list))
    lowest_number_of_reviews = min(books_2018, key = lambda book: 
    book.number_of_reviews)
    print(f"The book with the lowest number of reviews in 2018 was {lowest_number_of_reviews.name}")

# I am done with this. I give up. I am tired of working on this and I do not think this is a good fit for me.
# It's too much for me mentally. I am missing college basketball because I want to be done and I am getting upset
#  because I am two weeks behind and cannot keep up. I want to just quit and not do this anymore.

def analysis_two(book_list):
    print("Analysis of which genre (fiction or non-fiction) has appeared the most in the top 50's list")
    books_genre = list(filter(lambda genre : genre == genre, book_list))
    genre_appear_the_most = mean(books_genre, key = lambda grenre: book.genre)
    print(f"The genre that has appeared the most is{genre_appear_the_most}.genre")

def analysis_three(book_list):
    print("Analysis of which book has appeared the most in the top 50's list, and how many times it has appeared")
    books_year = list(max(lambda year: year == all, book_list))
    most_years = max(books_year, key = lambda year: book.year)
    print(f"The book that has appeared the most is {most_years}.name")

# BONUS USER STORIES:


def bonus_analysis_one(book_list):
    print("Analysis of which author has shown up on the top 50's list the most (Distinct books only!)")


def bonus_analysis_two(book_list):
    print("Analysis of the top book for each year, based on the book's user ratings and number of reviews")


def bonus_analysis_three(book_list):
    print("Analysis of which book has appeared the most consecutively on top 50's list")


run_analysis(data_list)