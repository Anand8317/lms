#!/usr/bin/env python
# coding: utf-8

# In[65]:

book = {}
from datetime import datetime, timedelta
import borrower
def addBook():
    newBook = dict()
    bookId = id(newBook)
    newBook[bookId] = ["", "", 0, 0, 0, 0,[]]
    print("\n")
    newBook[bookId][0] = input("Enter the title of the book: ")
    newBook[bookId][1] = input("Enter the author of the book: ")
    newBook[bookId][2] = int(input("Enter the no of pages: "))
    newBook[bookId][3] = int(input("Enter the no of copies: "))
    newBook[bookId][4] = int(input("Enter the ISBN number: "))
    newBook[bookId][5] = int(input("Enter the published year: "))
    print("Book has been added to library")
    print("Book Id is",bookId)
    print("\n")
    book.update(newBook)
    
def editBook(bookId):
    if bookId not in book:
        print("\n")
        print("Book Id not found!")
        print("\n")
        return
    print("\n")
    book[bookId][0] = input("Enter the new title of the book: ")
    book[bookId][1] = input("Enter the new author of the book: ")
    book[bookId][2] = int(input("Enter the new no of pages: "))
    book[bookId][3] = int(input("Enter the new no of copies: "))
    book[bookId][4] = int(input("Enter the new ISBN number: "))
    book[bookId][5] = int(input("Enter the new published year: "))
    print("\n")
    
def delBook(bookId):
    if bookId not in book:
        print("\n")
        print("Book Id not found!")
        print("\n")
        return
    del book[bookId]
    print("\n")
    print("Book is deleted")
    print("\n")
    
def borrowBook(bookId, emailId):
    if bookId not in book or emailId not in borrower.borrower:
        print("\n")
        print("Incorrect book Id or email Id!")
        print("\n")
        return
    if book[bookId][3] != 0:
        book[bookId][3] -= 1
        print("\n")
        print(book[bookId][0], "book has been issued")
        issuedDateandTime = datetime.now()
        maxReturnDate = issuedDateandTime + timedelta(days = 14)
        bookIssuedandMax = dict()
        bookIssuedandMax[bookId] = [issuedDateandTime, maxReturnDate]
        borrower.borrower[emailId][5].update(bookIssuedandMax)
        book[bookId][6].append("Book borrowed by " + emailId + " on " + str(issuedDateandTime))
        print("\n")
    else:
        print("\n")
        print(book[bookId][0], " has 0 copies. It cannot be issued")
        
def bookReturn(bookId, emailId):
    if bookId not in book or emailId not in borrower.borrower:
        print("\n")
        print("Incorrect book Id or email Id!")
        print("\n")
        return
    if bookId not in borrower.borrower[emailId][5]:
        print("\n")
        print("This book has not been issued to you")
        print("\n")
    else:
        returnTimeandDate = datetime.now()
        if (returnTimeandDate > borrower.borrower[emailId][5][bookId][1]):
            print("Pay penalty of Rs100 for returning book after 14 days")
        book[bookId][3] += 1
        bookIssuedandreturn = dict()
        bookIssuedandreturn[bookId] = [borrower.borrower[emailId][5][bookId][0], returnTimeandDate]
        borrower.borrower[emailId][6].update(bookIssuedandreturn)
        del borrower.borrower[emailId][5][bookId]
        book[bookId][6].append("Book returned by " + emailId + " on " + str(returnTimeandDate))
        print("\n")
        print("Thank you for returning the book")
        print("\n")
    
def bookDetail(bookId):
    if (bookId not in book):
        print("Book not found")
        return
    print("\n")
    print("Book Id:", bookId)
    print("Title: ", book[bookId][0])
    print("Author name:", book[bookId][1])
    print("Number of pages:", book[bookId][2])
    print("Number of copies:", book[bookId][3])
    print("ISBN:", book[bookId][4])
    print("Published year:", book[bookId][5])
    print("\n")
    
def bookDetailWithHistory(bookId):
    if (bookId not in book):
        print("Book not found")
        return
    print("\n")
    print("Book Id:", bookId)
    print("Title: ", book[bookId][0])
    print("Author name:", book[bookId][1])
    print("Number of pages:", book[bookId][2])
    print("Number of copies:", book[bookId][3])
    print("ISBN:", book[bookId][4])
    print("Published year:", book[bookId][5])
    print("\n")
    print("Issue and Return History")
    for history in book[bookId][6]:
        print(history)
    print("\n")
    


# In[66]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




