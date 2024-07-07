from app.storage.storage import Storage
from app.managers.book import BookManager
from app.managers.user import UserManager
from app.operations.check import CheckoutManager
from app.models.models import Book, User

def main_menu():
    """
    Displays the main menu and gets the user's choice.

    Returns:
        str: The user's menu choice.
    """
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. List Users")
    print("5. Checkout Book")
    print("6. Checkin Book")
    print("7. List Checkouts")
    print("8. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    """
    The main function that runs the Library Management System.
    """
    book_storage = Storage('books.json', Book)
    user_storage = Storage('users.json', User)
    checkout_storage = Storage('checkouts.json', dict)  # Checkout data is stored as a list of dictionaries

    book_manager = BookManager(book_storage)
    user_manager = UserManager(user_storage)
    checkout_manager = CheckoutManager(checkout_storage)

    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_manager.add_book(title, author, isbn)
        elif choice == '2':
            book_manager.list_books()
        elif choice == '3':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)
        elif choice == '4':
            user_manager.list_users()
        elif choice == '5':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout_manager.checkout_book(user_id, isbn)
        elif choice == '6':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkin: ")
            checkout_manager.checkin_book(user_id, isbn)
        elif choice == '7':
            checkout_manager.list_checkouts()
        elif choice == '8':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
