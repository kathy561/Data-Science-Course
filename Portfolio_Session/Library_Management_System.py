'''
Background: In an effort to move away from their physical management system the
library wants a digital solution to manage book checkouts, returns, and reservations
efficiently.
Challenge: You are tasked with creating this new system using lists and dictionaries.
Objective: Once the user has inputted the desired text into the document, the
following features will be offered to the user:
- The program should use lists and dictionaries to keep track of various details
- Handle common library operations like checking out a book, which would
decrease the number of available copies and add the book to the user's
borrowed list.
- Prevent users from borrowing more books than allowed and calculate fines for
late returns.
'''

from datetime import datetime

book_inventory = {"To Kill a Mockingbird" : {"copies" : 5, "current_borrowers" : []}, 
                  "Pride and Prejudice" : {"copies" : 5, "current_borrowers" : []}, 
                  "Animal Farm" : {"copies" : 5, "current_borrowers" : []}, 
                  "	1984" : {"copies" : 5, "current_borrowers" : []}, 
                  "	The Great Gatsby" : {"copies" : 5, "current_borrowers" : []}, 
                  "The Catcher in the Rye" : {"copies" : 5, "current_borrowers" : []}}

user_info = {"John Smith" : {"borrowed_books" : [], "fines" : 0, "checkout_date" : {}},
             "Anna Smith" : {"borrowed_books" : [], "fines" : 0, "checkout_date" : {}}, 
             "Sarah Jones" : {"borrowed_books" : [], "fines" : 0, "checkout_date" : {}}, 
             "Mark Allan" : {"borrowed_books" : [], "fines" : 0, "checkout_date" : {}}}


# Function for checking out books

def checkout_book(book_title, user_name, date):
    if book_inventory[book_title]["copies"] > 0 and len(user_info[user_name]["borrowed_books"]) < 3:
        book_inventory[book_title]["copies"] -= 1
        book_inventory[book_title]["current_borrowers"].append(user_name)
        user_info[user_name]["borrowed_books"].append(book_title)
        date = datetime.strptime(date, '%d-%m-%Y')
        user_info[user_name]["checkout_date"][book_title] = date
        print(f"Book '{book_title}' checked out successfully.")
    else: 
        print("Error: Book not available or user has reach the maximum borrow limit.")

# call the check out book function 

checkout_book("To Kill a Mockingbird", "Anna Smith", "03-05-2023")
checkout_book("Animal Farm", "Anna Smith", "03-03-2024")
checkout_book("Animal Farm", "John Smith", "03-02-2024")
checkout_book("Animal Farm", "Mark Allan", "03-03-2024")

# Function to calculate the number of days
def diff_dates(end_date, start_date):
    return abs(end_date-start_date).days


#Function to return a book 

def return_book(book_title, user_name, date):
    if book_title in user_info[user_name]["borrowed_books"]:
        book_inventory[book_title]["copies"] += 1
        book_inventory[book_title]["current_borrowers"].remove(user_name)
        user_info[user_name]["borrowed_books"].remove(book_title)
        end_date = datetime.strptime(date, '%d-%m-%Y')
        if diff_dates(end_date, user_info[user_name]["checkout_date"][book_title]) > 7:
            user_info[user_name]["fines"] += 1
            print(f"Book '{book_title}' returned successfully but late, fine applied.")
        else: print(f"Book '{book_title}' returned successfully")
    else: print(f"Error: {user_name} has not borrowed {book_title}")


return_book("To Kill a Mockingbird", "Anna Smith", "06-03-2024")
return_book("Animal Farm", "Anna Smith", "03-03-2024")

# Function to output the current books checkout for a user

def user_current_info(user_name):
    print(f'''
          {user_name}'s library account
          Checked out books : {user_info[user_name]["borrowed_books"]}
          Fines : {user_info[user_name]["fines"]}
          ''')

user_current_info("Anna Smith")
user_current_info("Mark Allan")

