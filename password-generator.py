passwords = []

try :
 with open("password.txt", "r") as file:
    for line in file:
       line = line.strip()
       passwords.append(line)
except FileNotFoundError:
 pass


import random
import string

def generate_password():
    try:
        length = int(input("Enter password length : "))
        if length <= 0:
          print("Password length must be greater than 0.")
          return
    except ValueError:
        print("Please enter a valid number.")
        return

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numbers = string.digits
    symbol = string.punctuation

    all_character = upper + lower + numbers + symbol

    password = ""

    for i in range(length):
        password += random.choice(all_character)

    print(password)

    passwords.append(password)
    save_password()
    print("password Added Successfully")


def view_password():
   if len(passwords) == 0:
          print("No password found")
          return

   for password in passwords:
      print(password)

def clear_history():
    passwords.clear()
    save_password()
    print("History Cleared Successfully")

def save_password():
    with open("password.txt", "w") as file:
        for password in passwords:
            file.write(password + "\n")
      
while True:

    print("1. generate password")
    print("2. view password")
    print("3. clear history")
    print("4. exit")

    try :
     choice = int(input("Enter your choice : "))
    except ValueError :
       print("Please enter a valid number.")
       continue

    if choice == 1:
       generate_password()

    elif choice == 2:
       view_password()

    elif choice == 3:
       clear_history()

    elif choice == 4:
        print("Good bye")
        break
       
    else:
        print("Invalid input")
