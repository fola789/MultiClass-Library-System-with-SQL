import database
from book import Book
  
def bookSearchTitle(bookTitle: str): 
    ''' Search in book info table for book Title
     based on user input.
    
    Parameters:
    title (str): Name of book in Database.
    Returns:
    result (str) Result of attempted book lookup.
    '''
    books = database.readAvailableBookByTitle(bookTitle)
    result = ""
    if not books:
        result = "Sorry, the book title you searched for does not exist\n" #if there are no results this is printed
    else:
        for book in books:
            f"ID: {book.ID}, ISBN: {book.ISBN}, Title: {book.Title}, Author: {book.Author}"
            book = f"ID: {book.ID}, ISBN: {book.ISBN}, Title: {book.Title}, Author: {book.Author}\n"
            result += book
    return result