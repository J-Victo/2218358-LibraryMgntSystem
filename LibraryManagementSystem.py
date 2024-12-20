# Great Harland Library Management System
import re

# Initialize book list and user credentials
books = [
    {"id": 1, "title": "Harry Potter Series", "author": "J.K. Rowling", "status": "available"},
    {"id": 2, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "status": "available"},
    {"id": 4, "title": "The Alchemist", "author": "Paulo Coelho", "status": "available"},
    {"id": 4, "title": "The Da Vinci Code", "author": "Dan Brown", "status": "available"},
    {"id": 5, "title": "The Twilight Saga", "author": "Stephenie Meyer", "status": "available"},
    {"id": 6, "title": "Gone with the Wind", "author": "Margaret Mitchell", "status": "available"},
    {"id": 7, "title": "Think and Grow Rich", "author": "Napoleon Hill", "status": "available"},
    {"id": 8, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "status": "available"},
    {"id": 9, "title": "1984", "author": "George Orwell", "status": "available"},
    {"id": 10, "title": "The Diary of a Young Girl", "author": "Anne Frank", "status": "available"},
    {"id": 11, "title": "To Kill a Mockingbird", "author": "Harper Lee", "status": "available"},
    {"id": 12, "title": "The God's Must Be Crazy", "author": "Jamie Uys", "status": "available"},
    {"id": 13, "title": "The Golden Girl", "author": "Anne Frank", "status": "available"},
    {"id": 14, "title": "The Nature and Nature", "author": "James Victor", "status": "available"}

]

users = {
    "Admin": "Admin123",
    "Customer": "Patron123"
}

book_id_counter = max(book["id"] for book in books)  # Initialize book ID counter

# Login function
def login():
    print("Welcome to the Great Hartland Community Library Management!")
    attempts = 3
    while attempts > 0:
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()
        if username in users and users[username] == password:
            print(f"Login successful! Welcome, {username}.")
            return username
        else:
            attempts -= 1
            print(f"Invalid username or password, please try again. {attempts} attempt(s) left.")
    print("Too many failed attempts. Exiting.")
    exit()

# Add new book
def add_book():
    global book_id_counter

    while True:
        title = input("Enter book title: ").strip()
        if not title:
            print("Title cannot be empty. Please try again.")
        else:
            break

    while True:
        author = input("Enter book author: ").strip()
        if not author:
            print("Author name cannot be empty. Please try again.")
        elif re.search(r"[^a-zA-Z\s.]", author):
            print("Author name cannot contain numbers or special characters. Please try again.")
        else:
            break

    book_id_counter += 1
    books.append({"id": book_id_counter, "title": title, "author": author, "status": "available"})
    print(f"Book '{title}' by {author} added successfully with ID {book_id_counter}.")

# Search for books
def search_books():
    search_term = input("Enter book title, author, or keyword to search: ").strip().lower()
    results = [
        book for book in books
        if search_term in book["title"].lower() or search_term in book["author"].lower()
    ]
    if results:
        print("Books found:")
        for book in results:
            print(f"- ID {book['id']}: '{book['title']}' by {book['author']} ({book['status']})")
    else:
        print("No books found matching your search.")

# View available books
def view_books():
    print("All books in the library:")
    for book in books:
        print(f"- ID {book['id']}: '{book['title']}' by {book['author']} ({book['status']})")

# Check out book
def check_out_book():
    identifier = input("Enter the ID or Title of the book to check out: ").strip()
    for book in books:
        if (identifier.isdigit() and book["id"] == int(identifier)) or (identifier.lower() == book["title"].lower()):
            if book["status"] == "available":
                book["status"] = "checked out"
                print(f"'{book['title']}' has been checked out.")
                return
            else:
                print("Book already checked out.")
                return
    print("The title of book entered, or author doesn't match any in our list. Book Not Found.")

# Check in book
def check_in_book():
    identifier = input("Enter the ID or Title of the book to check in: ").strip()
    for book in books:
        if (identifier.isdigit() and book["id"] == int(identifier)) or (identifier.lower() == book["title"].lower()):
            if book["status"] == "checked out":
                book["status"] = "available"
                print(f"'{book['title']}' has been checked in.")
                return
            else:
                print("Book was not checked out.")
                return
    print("The title of book entered, or author doesn't match any in our list. Book Not Found.")

# Remove book
def remove_book():
    identifier = input("Enter the ID or Title of the book to remove: ").strip()
    for book in books:
        if (identifier.isdigit() and book["id"] == int(identifier)) or (identifier.lower() == book["title"].lower()):
            books.remove(book)
            print(f"'{book['title']}' has been removed from the library.")
            return
    print("The Book entered does not exist or not found.")

# Main function
def main():
    user = login()
    while True:
        if user == "Admin":
            print("\nAdmin Menu:")
            print("1. Add New Book")
            print("2. Search for Books")
            print("3. Check Out Book")
            print("4. Check In Book")
            print("5. View Available Books")
            print("6. Remove Book")
            print("7. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                add_book()
            elif choice == "2":
                search_books()
            elif choice == "3":
                check_out_book()
            elif choice == "4":
                check_in_book()
            elif choice == "5":
                view_books()
            elif choice == "6":
                remove_book()
            elif choice == "7":
                print("Exiting the system. See you next time. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        else:
            print("\nPatron Menu:")
            print("1. Search for Books")
            print("2. View Available Books")
            print("3. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                search_books()
            elif choice == "2":
                view_books()
            elif choice == "3":
                print("Thank you for patronising us. See you next time. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
