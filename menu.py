from library import Book, User, Author

books_database = []
users_database = []
authors_database = []

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Author:
    def __init__(self, name):
        self.name = name

def main_menu():
    print("Welcome to the Library Management System!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")

def book_operations_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

def user_operations_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. Display all users")

def author_operations_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. Display all authors")

def add_new_user():
    print("Adding a New User:")
    name = input("Enter the name of the user: ")
    email = input("Enter the email of the user: ")
    new_user = User(name, email)
    users_database.append(new_user)
    print(f"User '{name}' added successfully!")

def display_all_users():
    print("All Users:")
    for index, user in enumerate(users_database, start=1):
        print(f"{index}. Name: {user.name}, Email: {user.email}")

def add_new_author():
    print("Adding a New Author:")
    name = input("Enter the name of the author: ")
    new_author = Author(name)
    authors_database.append(new_author)
    print(f"Author '{name}' added successfully!")

def display_all_authors():
    print("All Authors:")
    for index, author in enumerate(authors_database, start=1):
        print(f"{index}. Name: {author.name}")

def add_new_book():
    print("Adding a New Book:")
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    genre = input("Enter the genre of the book: ")
    publication_date = input("Enter the publication date of the book: ")
    new_book = Book(title, author, genre, publication_date)
    books_database.append(new_book)
    print(f"Book '{title}' added successfully!")

def borrow_book():
    print("Borrow a Book:")
    title = input("Enter the title of the book you want to borrow: ")
    found = False

    for book in books_database:
        if book.title.lower() == title.lower() and not book.borrowed:
            book.borrowed = True
            found = True
            print(f"Book '{title}' borrowed successfully!")
            break
    
    if not found:
        print(f"Book '{title}' is either not available or already borrowed.")

def return_book():
    print("Return a Book:")
    title = input("Enter the title of the book you want to return: ")
    found = False

    for book in books_database:
        if book.title.lower() == title.lower() and book.borrowed:
            book.borrowed = False
            found = True
            print(f"Book '{title}' returned successfully!")
            break
    
    if not found:
        print(f"Book '{title}' was not found or it is not borrowed.")

def search_for_book():
    print("Search for a Book:")
    title = input("Enter the title of the book you want to search for: ")
    found = False

    for book in books_database:
        if book.title.lower() == title.lower():
            found = True
            print(f"Book Found:")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Genre: {book.genre}")
            print(f"Publication Date: {book.publication_date}")
            if book.borrowed:
                print("Status: Borrowed")
            else:
                print("Status: Available")
            break
    
    if not found:
        print(f"Book '{title}' was not found in the library.")

def display_all_books():
    print("All Books in the Library:")
    for index, book in enumerate(books_database, start=1):
        print(f"{index}. Title: {book.title}")
        print(f"   Author: {book.author}")
        print(f"   Genre: {book.genre}")
        print(f"   Publication Date: {book.publication_date}")
        if book.borrowed:
            print("   Status: Borrowed")
        else:
            print("   Status: Available")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            book_operations_menu()
            book_choice = input("Enter your choice: ")
            if book_choice == '1':
                add_new_book()
            elif book_choice == '2':
                borrow_book()
            elif book_choice == '3':
                return_book()
            elif book_choice == '4':
                search_for_book()
            elif book_choice == '5':
                display_all_books()
            else:
                print("Invalid choice. Please enter a valid option.")
        
        elif choice == '2':
            user_operations_menu()
            user_choice = input("Enter your choice: ")
            if user_choice == '1':
                add_new_user()
            elif user_choice == '2':
                display_all_users()
            else:
                print("Invalid choice. Please enter a valid option.")

        elif choice == '3':
            author_operations_menu()
            author_choice = input("Enter your choice: ")
            if author_choice == '1':
                add_new_author()
            elif author_choice == '2':
                display_all_authors()
            else:
                print("Invalid choice. Please enter a valid option.")
        
        elif choice == '4':
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()