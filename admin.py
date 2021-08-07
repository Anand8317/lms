#!/usr/bin/env python
# coding: utf-8

# In[ ]:
admin = {"admin":"admin"}

def createAdmin():
    newAdmin = dict()
    username = input("Enter username ")
    password = input("Enter password ")
    newAdmin[username] = password
    if username in admin:
        print("\nAdmin already exist\n")
    else:
        admin.update(newAdmin)
        print("\nNew Admin has been created\n")
    
def adminLogin(username, password):
    if not username in admin:
        print("Account doesn't exist")
        return False
    if admin[username] == password:
        print("\n")
        print("Successful login")
        print("\n")
        return True
    else:
        print("\n")
        print("Wrong password")
        print("\n")
        return False
    

