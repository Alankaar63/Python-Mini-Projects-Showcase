#library management system 2
class Library:
    def __init__(self , list_books , name_lib):
        self.list_books = list_books
        self.name_lib = name_lib
        self.lent_books = {}

    def add_books(self , book):
        self.list_books.append(book)
        print(f"{book} has been added successfully!")

    def display_books(self):
        print(f"The books available in {self.name_lib}:")
        for book in self.list_books:
            print(book)
        for book , borrower in self.lent_books.items():
            print(f'{book} issued by:{borrower}')

    def lend_books(self , book , borrower):
        if book in self.list_books:
            print(f"you can issue the book here:")
            self.lent_books[book] = borrower
            self.list_books.remove(book)
            print(f"{book} issued by: {borrower}")

        else:
            if book in self.lent_books:
                print(f"the {book} has been lent to {self.lent_books[books]}")
            else:
                print(f"Book '{book}' is not available in the library.")

    def return_books(self , book,borrower):
        if book in self.lent_books:
            self.lent_books.pop(book)
            self.list_books.append(book)
            print(f'{book} has ben returned by {borrower}')
        else:
            print(f'{book} is not available in {self.name_lib}')


list_books = ["Lolita" , "Pride and Prejudice" , "Harry Potter" , "1984"]
alankarLibrary = Library(list_books , "Phulera Library")

if __name__ == '__main__':
    while True:
        choice = input("Welcome to our Phulera Library\n Press D to display\n A to add books\n L to issue a boo"
                       "k\n R to return the books\n Q to exit the Program").capitalize()
        if choice == "D":
            alankarLibrary.display_books()

        elif choice == "A":
            book_tobe_added = input("Please enter the books to be added:")
            alankarLibrary.add_books(book_tobe_added)

        elif choice == "L":
            books_tobe_lend = input("Please enter the books to be issued:")
            book_borrower = input("Borrower's Name:")
            alankarLibrary.lend_books(books_tobe_lend , book_borrower)

        elif choice == "R":
            book_return = input("Please enter the book to be returned:")
            book_borrower = input("Borrower's Name:")
            alankarLibrary.return_books(book_return,book_borrower)

        elif choice == "Q":
            print("Exiting Phulera Library")
            break

        else:
            print("Invalid input.Try again!")
