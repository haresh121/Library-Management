# Library Management System

This Library Management System is a console-based application that allows users to manage books and users, perform checkouts and check-ins of books, and track book availability. The application is designed using Object-Oriented Programming principles and is modular and scalable.

## Features

1. Manage Books
    - Add, update, delete, list, and search books by title, author, or ISBN.
2. Manage Users
    - Add, update, delete, list, and search users by name or user ID.
3. Book Checkout and Check-in
    - Check out books to users and check them back in.
4. Track Book Availability
    - Maintain the availability status of books.
5. Simple Logging of Operations
    - Log operations for adding, updating, deleting, and checking in/out books.

## Project Structure
```
app/
├── models/
│ ├── __init__.py
│ ├── models.py
├── storage/
│ ├── __init__.py
│ ├── storage.py
├── managers/
│ ├── __init__.py
│ ├── book.py
│ ├── user.py
├── operations/
| ├── __init__.py
| ├── check.py
tests/
├── __init__.py
├── test_models.py
├── test_storage.py
├── test_book_manager.py
├── test_user_manager.py
├── test_checkout_manager.py
main.py
```

To run the application, run the following snippet
```sh
python main.py
```

To run the tests, use the following command:
```sh
python -m unittest discover tests
```
