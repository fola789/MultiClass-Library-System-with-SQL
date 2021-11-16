import sqlite3 
import csv
from book import Book

def dropAllTables(): 
    ''' Delete all tables created within the database.
    '''
    connection = sqlite3.connect("Library.db")  
    crsr = connection.cursor() 
    sqlCommand = """ DROP TABLE IF EXISTS Book_Info;"""
    crsr.execute(sqlCommand) # execute the statement 
    sqlCommand = """ DROP TABLE IF EXISTS Loan_History;"""
    crsr.execute(sqlCommand) # execute the statement 
    # To save the changes  within the  database file.
    connection.commit()
    # close the connection
    connection.close()

def createTableBookInfo(): 
    ''' Create BookInfo table
    '''
    connection = sqlite3.connect("Library.db")  
    crsr = connection.cursor() 
    sqlCommand = """CREATE TABLE Book_Info (
		    ID_Num  INTEGER,
		    ISBN    INTEGER,
		    Title   CHAR(10),
            Author  CHAR(10),
            Purchase_Date DATE,
            Member_ID CHAR(10),
		    TimesTakenOut INTEGER);"""
   
    
    crsr.execute(sqlCommand) # execute the statement 

    with open('Book_info.txt','r') as fin: 
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(i['ID'], i['ISBN'], i['Title'], i['Author'], i['PurchaseDate'], i['MemberID'], i['TimesTakenOut']) for i in dr]

    crsr.executemany("INSERT INTO Book_Info (ID_Num, ISBN, Title, Author, Purchase_Date, Member_ID, TimesTakenOut) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
    # To save the changes  within the  database file.
    connection.commit()
    # close the connection
    connection.close()
 
def createTableLoanHistory(): # Create LoanHistory table
    ''' Create Loan History Table 
    '''
    connection = sqlite3.connect("Library.db")  
    crsr = connection.cursor() 
    sqlCommand = """CREATE TABLE Loan_History (
	        Transaction_ID INTEGER PRIMARY KEY AUTOINCREMENT,
		    Book_ID INTEGER,
		    Checkout_Date DATE,
            Return_Date DATE,
            Member_ID CHAR(10));"""
  
    crsr.execute(sqlCommand) # execute the statement 

    with open('Loan_History.txt','r') as fin: 
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(i['Transaction'], i['Book_ID'], i['Checkout_Date'], i['Return_Date'], i['Member_ID'],) for i in dr]

    crsr.executemany("INSERT INTO Loan_History (Transaction_ID, Book_ID, Checkout_Date, Return_Date, Member_ID) VALUES (?, ?, ?, ?, ?);", to_db)
    # To save the changes  within the  database file.
    connection.commit()
    # close the connection
    connection.close()

def readAvailableBookByTitle(title: str):
    ''' Search in book info table for book Title
     based on user input.
    
    Parameters:
    title (str): Name of book in Database.
    Returns:
    availableBooks (Book[]) List of available books by title.
    '''
    connection = sqlite3.connect("Library.db")
    crsr = connection.cursor()
   
    sqlCommand =  f"SELECT * FROM Book_Info WHERE Title LIKE '%{title}%'" # Sting interpolation is an easier way to concatenate a string together without excessive syntax via injection

    # execute the statement 
    crsr.execute(sqlCommand)
    resultSet = crsr.fetchall()
    # To save the changes  within the  database file.
    connection.commit()
    # close the connection
    connection.close()
    availableBooks = []
    for result in resultSet:
        bookSearch = Book(int(result[0]), int(result[1]), result[2], result[3], result[4], int(result[5]), int(result[6])) # creates the book class by getting the results from the book search and setting the array to  = the resulting columns e.g. [0] = ID [1] = ISBN
        availableBooks.append(bookSearch)
    return availableBooks 

def readBookById(bookID: int):
    ''' Search in book info table for book ID
    ID based on user input.
    
    Parameters:
    bookID (int): Book identification to be searched.
    
    Returns:
    availableBooks(Book[]) List of books by ID.
    '''
    connection = sqlite3.connect("Library.db")
    crsr = connection.cursor()
   
    sqlCommand =  f"SELECT * FROM Book_Info WHERE ID_Num LIKE '%{bookID}%'" # Sting interpolation is an easier way to concatenate a string together without excessive syntax via injection

    # execute the statement 
    crsr.execute(sqlCommand)
    resultSet = crsr.fetchall()
    # To save the changes  within the  database file.
    connection.commit()
    # close the connection
    connection.close()
    availableBooks = []

    for result in resultSet:
        bookSearch = Book(int(result[0]), int(result[1]), result[2], result[3], result[4], int(result[5]), int(result[6])) # creates the book class by getting the results from the book search and setting the array to  = the resulting columns e.g. [0] = ID [1] = ISBN
        availableBooks.append(bookSearch)
    return availableBooks      

def deleteBookByTitle(bookTitle: str):
    ''' Delete book from database.
    Parameters:
    bookTitle (str): Name of book.
    '''
    connection = sqlite3.connect("Library.db")  
    crsr = connection.cursor()
                
    sqlCommand = f"DELETE FROM Book_Info WHERE Title = '{bookTitle}';"
    crsr.execute(sqlCommand)
    # To save the changes  within the  database file.
    connection.commit()
    # close the connection
    connection.close()

def readBookPopularityData():
    ''' Read most popular book based on times taken out from database.
    
    Returns:
    bookTitles(str[]) Names of books.
    timesTakenOut(int[]) Number of times the book has been checked out.
    '''
    # connecting to the database  
    connection = sqlite3.connect("Library.db")  
    sqlCommand = connection.cursor() 
    sqlCommand.execute(f"SELECT Title, SUM(TimesTakenOut) FROM Book_Info GROUP BY Title ORDER BY SUM(TimesTakenOut) DESC")
    data = sqlCommand.fetchall()
    # To save the changes  within the  database file.
    connection.commit() 
    # close the connection 
    connection.close()

    bookTitles = []
    timesTakenOut = []
    
    for row in data: 
        bookTitles.append(row[0])
        timesTakenOut.append(row[1])
    return bookTitles, timesTakenOut

def updateBookCheckout(memberID: int, bookID: int):
    ''' Checkout books based on member id and book id.
    
    Parameters:
    memberID (int): Unique identifier for memeber.
    bookID (int): Unique identifier for book.
    '''
    connection = sqlite3.connect("Library.db")
    crsr = connection.cursor()
                
    sqlCommand = f"INSERT INTO Loan_History (Book_ID,Checkout_Date,Return_Date,Member_ID) VALUES ({bookID}, (SELECT strftime('%d/%m/%Y','now')), \"\", \"{memberID}\");"
    crsr.execute(sqlCommand)

    sqlCommand = f"UPDATE Book_Info SET TimesTakenOut = TimesTakenOut + 1 WHERE ID_Num = {bookID};"
    crsr.execute(sqlCommand)

    sqlCommand = f"UPDATE Book_Info SET Member_ID = {memberID} WHERE ID_Num = {bookID};"
    crsr.execute(sqlCommand)
    # To save the changes  within the  database file.
    connection.commit()
    # close the connection
    connection.close()

def updateBookReturn(memberID: int, bookID: int):
    ''' Return books based on member id and book id.
    
    Parameters:
    memberID (int): Unique identifier for memeber.
    bookID (int): Unique identifier for book. 
    '''
    connection = sqlite3.connect("Library.db")
    crsr = connection.cursor()

    sqlCommand = f"SELECT * FROM Book_Info WHERE Member_ID LIKE '%{memberID}%'"
    crsr.execute(sqlCommand)

    sqlCommand = f"UPDATE Book_Info SET Member_ID = 0 WHERE ID_Num = {bookID};" # sets the member id of the book back to 0 so it can be taken out by someone else  
    crsr.execute(sqlCommand)
    # To save the changes  within the  database file.
    connection.commit()
    # close the connection
    connection.close()

