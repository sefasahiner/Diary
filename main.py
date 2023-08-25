import hashlib
from datetime import datetime
import os

current_date = datetime.now().date()
date_string = current_date.strftime("%Y-%m-%d")
text_name = date_string + ".txt"
users = {}


def register(username, password):
    username = input("Username: ")
    password = input("Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    print("User registered.")
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")


def login(username, password):
    with open("users.txt", "r")as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if stored_username == username and stored_password == password:
                print("Login successful!")
                gunluk_giris()
                return True
        print("User could not found or the password is incorrect.")
        return False


def save_to_text_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


def read_from_text_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        return content


def list_previous_journals():
    journal_files = [file for file in os.listdir() if file.endswith(".txt") and file != "users.txt"]
    return journal_files


previous_journals = list_previous_journals()


def gunluk_giris():
    girdi = input("To write Diary type writediary, to see the old records type oldrecords.")
    if girdi == "writediary":
        gunluk = input("$ ")
        save_to_text_file(text_name, gunluk)
    elif girdi == "oldrecords":
        if previous_journals:
            print("Old Records:")
            for journal in previous_journals:
                print(journal)
        else:
            print("Not found any record.")


istek = input("Do you want to Register or Login? L/R: ")
if istek == "L":
    username = input("Username: ")
    password = input("Password: ")
    login(username, password)
elif istek == "R":
    username = input("Username: ")
    password = input("Password: ")
    register(username, password)
    print("Please login.")
    username = input("Username: ")
    password = input("Password: ")
    login(username, password)
else:
    print("Invalid input")
