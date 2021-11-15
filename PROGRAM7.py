#Create a CSV file by entering user-id and password, read and search the password for given userid.
import csv
user_info = ['Username', 'Password']
user_database = "D:\\Desktop\\Abhijeet\\CS PRACTICAL\\usiptest.csv"

def display_menu():
    print('MENU')
    print("1. Write")
    print("2. Read")
    print("3. Search")
    print("4. Quit")

def add_user():
    print("Add User Information")
    global user_info
    global user_database

    user_data = []
    for i in user_info:
        value = input("Enter " + i + ": ")
        user_data.append(value)

    with open(user_database, "a") as f:
        writer = csv.writer(f)
        writer.writerows([user_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return

def view_user():
    global user_info
    global user_database

    print("--- Records ---")
    with open(user_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i in user_info:
            print(i, end='\t |')
        print("\n----------------------------------")
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
    input("Press any key to continue")

def search_user():
    global user_info
    global user_database

    print("--- Search User ---")
    usrnm = input("Enter username to search: ")
    with open(user_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if usrnm == row[0]:
                    print("----- User Found -----")
                    print("Username: ", row[0])
                    print("Password: ", row[1])
                    break
        else:
            print("Username not found in our database")
    input("Press any key to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_user()
    elif choice == '2':
        view_user()
    elif choice == '3':
        search_user()
    else:
        break




