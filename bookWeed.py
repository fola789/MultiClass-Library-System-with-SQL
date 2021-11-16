# importing modules 
import numpy as np
import matplotlib.pyplot as plt
from bookSearch import bookSearchTitle
from book import Book
from database import deleteBookByTitle, readBookPopularityData, readAvailableBookByTitle

def showBookPopularityGraph(): 
    '''Function to list the book titles (not book copies) in the popularity order
    '''
    # visualise the list using Matplotlib module
    bookTitles, timesTakenOut = readBookPopularityData()
    plt.bar(bookTitles,timesTakenOut)
    plt.yticks(np.arange(min(timesTakenOut), max(timesTakenOut)+1, 1.0)) # used to increase Y axis by whole integers rather than by decimals
    plt.title("Book Popularity")
    plt.ylabel("Times Taken Out")
    plt.xlabel("Book Title")
    plt.show()
    
def getWorstBook(): 
    '''Pulls the least popular book from the database, based on times taken out.
    
    Returns:
    return(str) Recalls the book that has the least amount of times taken out.
    '''
    bookTitles, timesTakenOut = readBookPopularityData()
    np.arange(min(timesTakenOut), max(timesTakenOut)+1, 1.0) # used to increase Y axis by whole integers rather than by decimals
    return min(bookTitles)

def removeBook(bookTitle: str):
    '''Attempts to emoves a book from the library database
    Parameters:
    bookTitle (str) The title of the book that is attempting to be removed.
    
    Returns:
    result(str) Recalls the name of the book that has been attempted to be removed.
    '''
    bookSearch = readAvailableBookByTitle(bookTitle)
    result = ""
    if not bookSearch:
        result = "Sorry, the book title you searched for does not exist"
    else:
        book: Book = bookSearch[0]
        deleteBookByTitle(book.Title)
        result = f"Book Title: {book.Title} has been removed from the database"
    return result

