import os

def add_user():
    confirm = "N"
    while confirm != "Y":
        username = input("enter the name to add new user ")
        print("username is '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo useradd " + username)
    
add_user()
print("user has been added")
