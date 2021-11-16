class Book: # Creates a book class where it doesnt matter what column headers are called and allows for operations to be performed
    ''' Definition of a Book
    Parameters: 
    ID (int): Unique identifier for book
    ISBN (int): International Standard Book Number
    TITLE (string): Title of book
    AUTHOR (string): Author of book
    PurchaseDate (string): Day and time of purchase of book
    MemberID (int): Unique identifier for member
    TimesTakenOut (int): Times book has been checked out by a member
    '''
    def __init__(self, ID: int, ISBN: int, Title: str, Author: str, PurchaseDate: str, MemberID: int, TimesTakenOut: int):
        self.ID = ID
        self.ISBN = ISBN
        self.Title = Title
        self.Author = Author
        self.PurchaseDate = PurchaseDate
        self.MemberID = MemberID
        self.TimesTakenOut = TimesTakenOut

    def isAvailable(self):
        '''Checks the availability of book

        Returns:
        True (Bool) If book is availble for checkout.
        False (Bool) If book is not availble for checkout.
        '''
        if self.MemberID == 0:
            return True
        else: 
            return False
