#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import book
from datetime import datetime, timedelta

borrower = {}

def registerBorrower():
    newBorrower = dict()
    name = input("Enter your full name: ")
    dob = input("Enter your date of birth: ")
    contactNo = int(input("Enter contact No: "))
    emailId = input("Enter email Id: ")
    password = input("Enter password: ")
    if emailId in borrower:
        print("\nAccount already exist\n")
        return
    newBorrower[emailId] = [name, dob, contactNo, emailId, password, {}, {}]
    borrower.update(newBorrower)
    
def login(emailId, password):
    if emailId not in borrower:
        print("\n")
        print("Account doesn't exist")
        print("\n")
        return False

    if borrower[emailId][4] == password:
        print("\n")
        print("Successful login")
        print("\n")
        return True
    else:
        print("\n")
        print("Wrong password")
        print("\n")
        return False
    
def borrowedBook(emailId):
    if emailId not in borrower:
        print("\n")
        print("Account doesn't exist")
        print("\n")
        return
    print("\n")
    print("Currently borrowed books")
    for bookId in borrower[emailId][5]:
        book.bookDetail(bookId)
    print("\n")
        
def borrowHistory(emailId):
    if emailId not in borrower:
        print("\n")
        print("Account doesn't exist")
        print("\n")
        return
    print("\n")
    print("Your borrow history")
    for bookId in borrower[emailId][6]:
        book.bookDetail(bookId)
    print("\n")
    
def allBorrowersAndHistory():
    print("\n")
    i = 1
    for emailId in borrower:
        print("User ",i)
        print("Full name", borrower[emailId][0])
        print("DOB", borrower[emailId][1])
        print("Contact no", borrower[emailId][2])
        print("Email Id", borrower[emailId][3])
        print("Password", borrower[emailId][4])
        currentlyBorrowedBook(emailId)  
        BorrowedBookHistory(emailId)
        print("\n")
        i+=1
        
def currentlyBorrowedBook(emailId):
    print("\n")
    print("Currently borrowed books")
    for bookId in borrower[emailId][5]:
        print("Book Id",bookId)
        print("Title",book.book[bookId][0])
        currentDateandTime = datetime.now()
        print("Time remaining",(borrower[emailId][5][bookId][1] - currentDateandTime))
        print("\n")
        
def BorrowedBookHistory(emailId):
    print("\n")
    print("Your borrow history")
    for bookId in borrower[emailId][6]:
        print("Book Id",bookId)
        print("Title",book.book[bookId][0])
        print("Book borrowed on",(borrower[emailId][6][bookId][0]))
        print("Book returned on",(borrower[emailId][6][bookId][1]))
        print("\n")

