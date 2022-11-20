from data import data_list
from book import Book

# def create_book_list(book_list):
#     books = create_book_list(book_list)

def run_analysis(book_list):

    print(' ')

    analysis_one(book_list)
    print(' ')
    analysis_two(book_list)
    print(' ')

    analysis_three(book_list)

    

# Analysis 1
    # what book has lowest numbers of reviews in 2018
def analysis_one(book_list): 
    books_2018 = list(filter(lambda book: Book.year == 2018, book_list))
    lowest_number_of_reviews = min(books_2018, key = lambda book: 
    Book.number_of_reviews)
    print(f"The book with the lowest number of reviews in 2018 was" 
        "{lowest_number_of_reviews_Book.name}")
    

# Analysis 2
    # Determine which genre has appeared the most in the Top 50s list
def analysis_two(book_list):
    books_genre = list(filter(lambda genre: Book.genre, book_list))
    genres_appear_the_most = max(books_genre, key = lambda book: Book.genre)
    print(f"The genre that has appeared the most is{genres_appear_the_most}")
    

# Analysis 3
    # what book has been in the Top 50s list for the most years
def analysis_three(book_list):
    books_years = list(filter(lambda year: book_list))
    most_years = max(books_years, key = lambda year: Book.year)
    print(f"The book that has")

# def run_report:
# #     pass


#     print(run_report)



