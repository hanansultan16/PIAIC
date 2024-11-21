# Initialize empty lists to store books and users
books = []
users = []


# To add a new book
def add_book():
    print("\n--- Add a Book ---")
    while True:
        book_id = input("Enter a unique book ID: ")
        # To check if book ID is already exists
        for book in books:
            if book["id"] == book_id:
                print("This ID already exists! Please enter a unique ID.")
                break
        else:
            # Run the code if book ID is unique
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            genre = input("Enter the book genre: ")
            status = "Available"  # Books will be availabe by default

            # To add book in the list
            book = {"id": book_id, "title": title, "author": author, "genre": genre, "status": status}
            books.append(book)
            print(f"Book '{title}' has been added to the library!")
            break



# To add a new user
def add_user():
    print("\n--- Add a User ---")
    while True:
        user_id = input("Enter a unique user ID: ")
        # To check if user ID is already exists
        for user in users:
            if user["id"] == user_id:
                print("This ID already exists! Please enter a unique ID.")
                break
        else:
            # Run the code if user ID is unique
            name = input("Enter the user's name: ")
            # To add user in the list
            user = {"id": user_id, "name": name, "borrowed_books": []}
            users.append(user)
            print(f"User '{name}' has been added to the library system!")
            break



# To borrow a book
def borrow_book():
    print("\n--- Borrow a Book ---")
    user_id = input("Enter your user ID: ")

    # To find user by their ID
    user = None
    for u in users:
        if u["id"] == user_id:
            user = u
            break

    if user is None:
        print("User not found! Please register first.")
        return

    book_id = input("Enter the book ID you want to borrow: ")

    # to find the book by it's ID
    book = None
    for b in books:
        if b["id"] == book_id:
            book = b
            break

    if book is None:
        print("Book not found!")
        return

    # To check book is available or not
    if book["status"] == "Available":
        book["status"] = "Checked Out"
        user["borrowed_books"].append(book_id)
        print(f"You have successfully borrowed '{book['title']}'!")
    else:
        print(f"Sorry, the book '{book['title']}' is already checked out.")


# To return a book
def return_book():
    print("\n--- Return a Book ---")
    user_id = input("Enter your user ID: ")

    # To find user by their ID
    user = None
    for u in users:
        if u["id"] == user_id:
            user = u
            break

    if user is None:
        print("User not found!")
        return

    book_id = input("Enter the book ID you want to return: ")

    # To check user has borrowed book or not
    if book_id not in user["borrowed_books"]:
        print("You haven't borrowed this book!")
        return

    # To find the book by it's ID
    book = None
    for b in books:
        if b["id"] == book_id:
            book = b
            break

    if book is None:
        print("Book not found!")
        return

    # To return the book
    book["status"] = "Available"
    user["borrowed_books"].remove(book_id)
    print(f"You have successfully returned '{book['title']}'!")


# To search for books
def search_books():
    print("\n--- Search Books ---")
    search_type = input("Search by title, author, or genre: ").lower()
    search_value = input("Enter your search term: ").lower()

    print("\nSearch Results:")
    found = False
    for book in books:
        if search_value in book[search_type].lower():
            print(f"{book['title']} by {book['author']} - {book['genre']} [{book['status']}]")
            found = True

    if not found:
        print("No books match your search criteria.")


# To view all books
def view_all_books():
    print("\n--- All Books ---")
    if not books:
        print("No books in the library.")
    else:
        for book in books:
            print(f"{book['title']} by {book['author']} - {book['genre']} [{book['status']}]")


# To view available books
def view_available_books():
    print("\n--- Available Books ---")
    found = False
    for book in books:
        if book["status"] == "Available":
            print(f"{book['title']} by {book['author']} - {book['genre']} [{book['status']}]")
            found = True

    if not found:
        print("No books are currently available.")


# To view checked-out books
def view_checked_out_books():
    print("\n--- Checked Out Books ---")
    found = False
    for book in books:
        if book["status"] == "Checked Out":
            print(f"{book['title']} by {book['author']} - {book['genre']} [{book['status']}]")
            found = True

    if not found:
        print("No books are currently checked out.")


# To main menu
def main_menu():
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
            add_book()
        elif choice == "2":
            add_user()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            search_books()
        elif choice == "6":
            view_all_books()
        elif choice == "7":
            view_available_books()
        elif choice == "8":
            view_checked_out_books()
        elif choice == "9":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# Start the program
main_menu()
