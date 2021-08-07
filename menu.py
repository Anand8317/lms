#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import book, borrower, admin
def menu():
    flag1 = True
    while (flag1 != False):
        print("\n")
        print("1. Admin")
        print("2. Borrowers")
        print("3. Exit")
        print("\n")
        choice = int(input("Enter your choice: "))

        if (choice == 1):
            username = input("Enter username: ")
            password = input("Enter password: ")
            flag = admin.adminLogin(username, password)
            if flag != True:
                return
            
            flag2 = True
            while (flag2 != False):
                print("\n")
                print("1. Add admin")
                print("2. Add borrower")
                print("3. View book details and borrowing history")
                print("4. Add book")
                print("5. Edit book")
                print("6. Delete book")
                print("7. List all borrowers and view details and borrowing history")
                print("8. Give book to borrower")
                print("9. Accept book return")
                print("10. Go back")
                choice = int(input("Enter your choice: "))
                print("\n")

                if (choice == 1):
                    admin.createAdmin()
                elif (choice == 2):
                    borrower.registerBorrower()
                elif (choice == 3):
                    print("\n")
                    bookId = int(input("Enter book Id: "))
                    book.bookDetailWithHistory(bookId)
                elif (choice == 4):
                    book.addBook()
                elif (choice == 5):
                    print("\n")
                    bookId = int(input("Enter book Id: "))
                    book.editBook(bookId)
                elif (choice == 6):
                    print("\n")
                    bookId = int(input("Enter book Id: "))
                    book.delBook(bookId)
                elif (choice == 7):
                    borrower.allBorrowersAndHistory()
                elif (choice == 8):
                    print("\n")
                    bookId = int(input("Enter book Id: "))
                    emailId = input("Enter email Id: ")
                    book.borrowBook(bookId, emailId)
                elif (choice == 9):
                    print("\n")
                    bookId = int(input("Enter book Id: "))
                    emailId = input("Enter email Id: ")
                    book.bookReturn(bookId, emailId)
                elif (choice == 10):
                    flag2 = False


        elif (choice == 2):
            print("\n")
            print("1. Register")
            print("2. Login")
            choice = int(input("Enter your choice: "))
            print("\n")

            if (choice == 1):
                borrower.registerBorrower()
            elif (choice == 2):
                print("\n")
                emailId = input("Enter Email Id: ")
                password = input("Enter password: ")
                flag = borrower.login(emailId, password)
                if flag != True:
                    return

                flag3 = True
                while (flag3 != False):
                    print("1. List of currently borrowed book with time left")
                    print("2. Book details of each borrowed book")
                    print("3. Borrowing history")
                    print("4. Go Back")
                    choice = int(input("Enter your choice: "))
                    print("\n")

                    if (choice == 1):
                        borrower.currentlyBorrowedBook(emailId)
                    elif (choice == 2):
                        borrower.borrowedBook(emailId)
                    elif (choice == 3):
                        borrower.BorrowedBookHistory(emailId)
                    elif (choice == 4):
                        flag3 = False
                    
        elif (choice == 3):
            flag1 = False

        

