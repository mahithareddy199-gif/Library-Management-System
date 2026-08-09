from library import Library
from book import Book
from user import User

library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Add User")
    print("6. Display Users")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        category = input("Enter Category: ")
        quantity = int(input("Enter Quantity: "))

        b = Book(book_id, title, author, category, quantity)
        library.add_book(b)

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        book_id = int(input("Enter Book ID to search: "))
        library.search_book(book_id)

    elif choice == 4:
        book_id = int(input("Enter Book ID to remove: "))
        library.remove_book(book_id)

    elif choice == 5:
        user_id = int(input("Enter User ID: "))
        name = input("Enter Name: ")
        roll_no = input("Enter Roll No: ")
        department = input("Enter Department: ")
        phone = int(input("Enter Phone Number: "))

        u = User(user_id, name, roll_no, department, phone)
        library.add_user(u)

    elif choice == 6:
        library.display_users()

    elif choice == 7:
        book_id = int(input("Enter Book ID to issue: "))
        library.issue_book(book_id)

    elif choice == 8:
        book_id = int(input("Enter Book ID to return: "))
        library.return_book(book_id)

    elif choice == 9:
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")