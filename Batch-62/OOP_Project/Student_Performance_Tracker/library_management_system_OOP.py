# Class to represent a book in the library
class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.status = "Available"  # Books will be availabe by default

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} ({self.genre}) - {self.status}"


# Class to represent a library user
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []  # borrowed books lost store here

    def __str__(self):
        borrowed = ", ".join(self.borrowed_books) if self.borrowed_books else "None"
        return f"{self.user_id}: {self.name} - Borrowed Books: {borrowed}"


# Class to manage the library system
class Library:
    def __init__(self):
        self.books = {}  
        self.users = {}  

    # To add a new book in the library
    def add_book(self, book_id, title, author, genre):
        if book_id in self.books:
            print("Error: Book ID already exists!")
            return
        self.books[book_id] = Book(book_id, title, author, genre)
        print(f"Book '{title}' has been added successfully!")

    # To add a new user in the library
    def add_user(self, user_id, name):
        if user_id in self.users:
            print("Error: User ID already exists!")
            return
        self.users[user_id] = User(user_id, name)
        print(f"User '{name}' has been added successfully!")

    # To borrow a book
    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            print("Error: User ID not found!")
            return
        if book_id not in self.books:
            print("Error: Book ID not found!")
            return

        user = self.users[user_id]
        book = self.books[book_id]

        if book.status == "Available":
            book.status = "Checked Out"
            user.borrowed_books.append(book_id)
            print(f"Book '{book.title}' borrowed by {user.name}.")
        else:
            print(f"Error: Book '{book.title}' is already checked out.")

    # To return a book
    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            print("Error: User ID not found!")
            return
        if book_id not in self.books:
            print("Error: Book ID not found!")
            return

        user = self.users[user_id]
        book = self.books[book_id]

        if book_id in user.borrowed_books:
            book.status = "Available"
            user.borrowed_books.remove(book_id)
            print(f"Book '{book.title}' returned by {user.name}.")
        else:
            print("Error: This user did not borrow this book!")

    # To search for books
    def search_books(self, search_type, search_value):
        print(f"\nSearching for {search_type}: '{search_value}'")
        found_books = [
            book for book in self.books.values()
            if search_value.lower() in getattr(book, search_type).lower()
        ]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No books found.")

    # To view all books
    def view_books(self, status=None):
        print("\nLibrary Books:")
        for book in self.books.values():
            if status is None or book.status == status:
                print(book)


# The main function to interact with the library
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. View All Books")
        print("7. View Available Books")
        print("8. View Checked Out Books")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            genre = input("Enter Book Genre: ")
            library.add_book(book_id, title, author, genre)
        elif choice == "2":
            user_id = input("Enter User ID: ")
            name = input("Enter User Name: ")
            library.add_user(user_id, name)
        elif choice == "3":
            user_id = input("Enter User ID: ")
            book_id = input("Enter Book ID: ")
            library.borrow_book(user_id, book_id)
        elif choice == "4":
            user_id = input("Enter User ID: ")
            book_id = input("Enter Book ID: ")
            library.return_book(user_id, book_id)
        elif choice == "5":
            search_type = input("Search by (title/author/genre): ").lower()
            search_value = input("Enter search value: ")
            library.search_books(search_type, search_value)
        elif choice == "6":
            library.view_books()
        elif choice == "7":
            library.view_books(status="Available")
        elif choice == "8":
            library.view_books(status="Checked Out")
        elif choice == "9":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
