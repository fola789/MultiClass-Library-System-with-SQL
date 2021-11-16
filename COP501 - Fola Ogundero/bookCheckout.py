# importing modules
from database import updateBookCheckout, readBookById
from book import Book

def checkoutBook(memberID: int, bookID: int):
    '''Function to checkout a book based on its ID to a speicifc member
    Parameters:
    memberID(int): Unique identification of member
    bookID(int): Unique identification of book

    Returns:
    result(str) Status of the attemped checked out of the book.
    '''
    bookSearch = readBookById(bookID)
    result = ""
    if not bookSearch:
        result =  "Sorry, the book ID you searched for does not exist"
    else:
        book: Book = bookSearch[0]
        if not book.isAvailable():
            result =  "Sorry the book is not available for withdrawal"
        else:
            updateBookCheckout(memberID, book.ID)
            result =  f"Member ID: {memberID} has been assigned the book with title: {book.Title} and ID {book.ID}"
    return result