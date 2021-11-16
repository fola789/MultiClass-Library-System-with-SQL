from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import tkinter as tk
import bookSearch
import bookWeed
import bookCheckout
import bookReturn

def searchForBook():
    ''' Updates the GUI with the book being searched for by the title.
    '''
    sct_result.config(state='normal')
    sct_result.delete('1.0', END)
    result = bookSearch.bookSearchTitle(txt_input_book_title.get('1.0', 'end-1c'))
    
    sct_result.config(state='normal')
    sct_result.insert(tk.INSERT, result)
    sct_result.config(state='disabled')

def checkoutBook():
    ''' Checks out a book by the mmemberID and bookID and updates the GUI.
    '''
    sct_result.config(state='normal')
    sct_result.delete('1.0', END)
    memberID = txt_input_memberID.get('1.0', 'end-1c')
    if len(memberID) > 4:
        messagebox.showerror("Error!", "The member ID should not be greater than 4 digits")
    else:
        bookID =  txt_input_book_id.get('1.0', 'end-1c')
        result = bookCheckout.checkoutBook(int(memberID), int(bookID))

        sct_result.config(state='normal')
        sct_result.insert(tk.INSERT, result)
    sct_result.config(state='disabled')

def returnBook():
    ''' Returns  a book by the mmemberID and bookID and updates the GUI.
    '''
    sct_result.config(state='normal')
    sct_result.delete('1.0', END)
    result = bookReturn.returnBook(int(txt_input_memberID.get('1.0', 'end-1c')), int(txt_input_book_id.get('1.0', 'end-1c')))
    sct_result.config(state='normal')
    sct_result.insert(tk.INSERT, result)
    sct_result.config(state='disabled') 

def scoutBooks():
    ''' Visualises the book popularity at the library based on times taken out.
    '''
    sct_result.config(state='normal')
    sct_result.delete('1.0', END)
    bookWeed.showBookPopularityGraph()
    sct_result.config(state='disabled') 

def removeBookFromDatabase():
    ''' Removes a book from the library database based on the book title. 
    '''
    sct_result.config(state='normal')
    sct_result.delete('1.0', END)
    bookTitle = txt_input_book_title.get('1.0', 'end-1c')
    response = messagebox.askyesno("Question?", f"This will permanetly remove the book: {bookTitle} the database, are you sure you want to do it?")
    if response == True:
        result = bookWeed.removeBook(str(bookTitle))
        sct_result.config(state='normal')
        sct_result.insert(tk.INSERT, result)
    sct_result.config(state='disabled')

def removeWorstBookFromDatabase():
    ''' Removes the least popular book from the library database based on the timesTakenOut.
    '''
    sct_result.config(state='normal')
    sct_result.delete('1.0', END)
    bookTitle = bookWeed.getWorstBook()
    response = messagebox.askyesno("Question?", f"This will permanetly remove the book: {bookTitle}, which is currently the least popular book from the database, are you sure you want to do it?")
    if response == True:
        result = bookWeed.removeBook(bookTitle)
        sct_result.config(state='normal')
        sct_result.insert(tk.INSERT, result)
    sct_result.config(state='disabled')


def clearLibrary():
    ''' Resets the GUI
    '''
    txt_input_memberID.delete(1.0, END) 
    txt_input_memberID.insert(INSERT, 'Input Member ID here:')
    memberIdClick = 0
    
    txt_input_book_id.delete(1.0, END)
    txt_input_book_id.insert(INSERT, 'Input Book ID here:')
    bookIdClick = 0
    
    txt_input_isbn.delete(1.0, END)
    txt_input_isbn.insert(INSERT, 'Input ISBN here:')
    bookIsbnClick = 0
    
    txt_input_book_title.delete(1.0, END) 
    txt_input_book_title.insert(INSERT, 'Input Book Title here:')
    bookTitleClick = 0
    
    sct_result.config(state='normal')
    sct_result.delete(1.0, END)
    sct_result.config(state='disabled')

def clearTextField(event, txt_input_field, click): 
    ''' Delete the placeholder_text when user clicks in input box for the first time.
    '''
    if click == 0: ##Checking if its first click
        txt_input_field.delete(1.0, END)
        click+=1

########## GUI ##########
if __name__ == '__main__': # Entry point for application
    window = tk.Tk() #Creates tkinter object

    window.title("Library Managment System") # Settting up window and name
    window.geometry('750x500')
    window.configure(background = 'Grey')
    window.resizable(width=TRUE, height=TRUE)

    background_image = PhotoImage(file="image.png")
    background_label = Label(window, image=background_image)
    background_label.place(x=0,y=0, relwidth=1, relheight=1)

    memberIdClick = 0
    bookIdClick = 0
    bookIsbnClick = 0
    bookTitleClick = 0

    txt_input_memberID = Text(window) #Creates and places input field for Member ID
    txt_input_memberID.grid(column=0, row=4, padx=20, pady=20, sticky="W")
    txt_input_memberID.config(width=40, height = 2.5)
    txt_input_memberID.insert(INSERT, 'Input Your 4 digit Member ID here:')
    txt_input_memberID.bind("<Button-1>", lambda event: clearTextField(event, txt_input_memberID, memberIdClick))

    txt_input_book_id = Text(window) #Creates and places input field for book ID
    txt_input_book_id.grid(column=1, row=4, padx=20, pady=20, sticky="W")
    txt_input_book_id.config(width=40, height = 2.5)
    txt_input_book_id.insert(INSERT, 'Input the Book ID here:')
    txt_input_book_id.bind("<Button-1>", lambda event: clearTextField(event, txt_input_book_id, bookIdClick))

    txt_input_isbn = Text(window) #Creates and places input field for book ISBN
    txt_input_isbn.grid(column=1, row=6, padx=20, pady=20, sticky="W")
    txt_input_isbn.config(width=40, height = 2.5)
    txt_input_isbn.insert(INSERT, 'Input the book ISBN here:')
    txt_input_isbn.bind("<Button-1>", lambda event: clearTextField(event, txt_input_isbn, bookIsbnClick))

    txt_input_book_title = Text(window) #Creates and places input field for book title
    txt_input_book_title.grid(column=0, row=6, padx=20, pady=20, sticky="W")
    txt_input_book_title.config(width=40, height = 2.5)
    txt_input_book_title.insert(INSERT, 'Input the book title here:')
    txt_input_book_title.bind("<Button-1>", lambda event: clearTextField(event, txt_input_book_title, bookTitleClick))

    sct_result = scrolledtext.ScrolledText(window) #Creates and plces result field
    sct_result.place(x=95, y=200)
    sct_result.config(width=65, height=7, state='disabled')

    search_btn_run = Button(window, width=20, height=3, text="Book Search", command=lambda: searchForBook()).place(x=230, y=350) #Creates and places button and binds it to inspect arrangment method

    return_btn2_run  = Button(window, width=20, height=3, text="Book Return",command=lambda: returnBook()).place(x=70, y=350) #Creates and places button and binds it to inspect arrangment method
   
    checkout_btn3_run = Button(window, width=20, height=3, text="Book Checkout",command=lambda: checkoutBook()).place(x=390, y=350) #Creates and places button and binds it to inspect arrangment method

    popularity_btn4_run = Button(window, width=20, height=3, text="Book Popularity",command=lambda: scoutBooks()).place(x=550, y=350) #Creates and places button and binds it to inspect arrangment method

    reset_btn_run = Button(window, width=20, height=3, text="Reset Library Machine", command=lambda: clearLibrary()).place(x=390, y=420) #Creates and places button and binds it to inspect arrangment method

    remove_book_btn_run = Button(window, width=20, height=3, text="Remove Book", command=lambda: removeBookFromDatabase()).place(x=230, y=420) #Creates and places button and binds it to inspect arrangment method

    remove_worst_book_btn_run = Button(window, width=20, height=3, text="Remove Worst Book", command=lambda: removeWorstBookFromDatabase()).place(x=70, y=420) #Creates and places button and binds it to inspect arrangment method

    window.mainloop() #Stops the window from closing