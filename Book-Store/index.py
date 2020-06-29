from utils import bookDatabase


######################################## MENUS ########################################


# user menu
def userMenu():
    menu = input("""A for adding a book,
R for reading a book,
D for deleting a book,
U for updating a book,
S for searching a book,
Q for quitting the menu.
Enter your choice : """).upper()
    return menu


# update menu
def updateByMenu():
    ch = input("""What do you want to update? 
T for title, 
A for author, 
Y for year, 
N for nothing : """).upper()
    return ch


# search menu
def searchMenu():
    ch = input("""How would you like to search?
T for title
A for author
Y for publishing year
N for nothing.
Enter your choice : """).upper()
    return ch


######################################## MAIN MENU ########################################


def menu():
    bookDatabase.createBook()
    # accept user choice
    choice = userMenu()
    # exit condition
    while choice != "Q":
        if choice == "A":
            addBookPrompt()
        elif choice == "R":
            listAllBooks()
        elif choice == "S":
            searchPrompt()
        elif choice == "D":
            deleteBookPrompt()
        elif choice == "U":
            updateBookPrompt()
        else:
            print("Something wrong")
        choice = userMenu()


######################################## FEATURES ########################################


# display all books
def listAllBooks():
    if bookDatabase.get_all_books() == 0:
        print("Please add some books first.")
    else:
        for book in bookDatabase.get_all_books():
            print(f"{book['title']} by {book['author']} - {book['year']}")


# prompt for adding a book into the database
def addBookPrompt():
    title = input("Enter book title : ")
    author = input("Enter author name : ")
    year = input("Enter publishing year : ")
    bookDatabase.addBook(title, author, year)


# prompt for deleting a book from the database
def deleteBookPrompt():
    book = input("Which book do you want to delete? : ")
    bookDatabase.deleteBook(book)


# prompt for searching the book in the database
def searchPrompt():
    if len(bookDatabase.get_all_books()) == 0:
        print("Please add some books first.")
    else:
        ch = searchMenu()
        if ch == "T":
            searchedTitle = input("Search by title : ")
            books = bookDatabase.searchBookByTitle(searchedTitle)
            if len(books) == 0:
                print("Mentioned book is not present")
            else:
                for i in books:
                    print(f"{i['title']} by {i['author']} - {i['year']}")
        elif ch == "A":
            searchedAuthor = input("Search by author : ")
            books = bookDatabase.searchBookByAuthor(searchedAuthor)
            if len(books) == 0:
                print("Books from mentioned author is not present")
            else:
                for i in books:
                    print(f"{i['title']} by {i['author']} - {i['year']}")
        elif ch == "Y":
            searchedYear = input("Search by publishing year : ")
            books = bookDatabase.searchBookByYear(searchedYear)
            if len(books) == 0:
                print("Books published in mentioned year is not present")
            else:
                for i in books:
                    print(f"{i['title']} by {i['author']} - {i['year']}")
        elif ch == "N":
            pass
        else:
            print("Wrong choice")


# prompt for updating the values into the database
def updateBookPrompt():
    searchedBook = input("Which book needs to be updated? : ")
    if len(bookDatabase.searchBookByTitle(searchedBook)) == 0:
        print("Mentioned book is not found")
    else:
        ch = updateByMenu()
        bookDatabase.updateBook(searchedBook, ch)


# entry point of the application - calling the main menu function
menu()
