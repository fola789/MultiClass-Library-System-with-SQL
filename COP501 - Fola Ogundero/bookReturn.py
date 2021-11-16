from database import updateBookReturn, readBookById
from book import Book

def returnBook(memberID: int, bookID: int): 
    '''Function to return a book based on its ID by a speicifc member
    Parameters:
    memberID(int): Unique identification of member
    bookID(int): Unique identification of book

    Returns:
    result(str) Gives the status of the attempted book return.
    '''
    bookSearch = readBookById(bookID)
    result = ""
    if not bookSearch:
        result = "Sorry, the book ID you searched for does not exist"
    else:   
        book: Book = bookSearch[0]
        if  book.isAvailable():
            result = "Sorry the book is still available so can't be returned"
        elif memberID != book.MemberID : # checks that the current user is the person who has the book 
            result = f"Your memeber ID: {memberID} is not of that enlisted to the book, please try a different member ID for that book or a different bookID"
        else:    
            updateBookReturn(memberID, book.ID)
            result = f"Member ID: {memberID} has returned the book: {book.Title} ID number: {book.ID}"
    return result