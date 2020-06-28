from utils import bookDatabase


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


def listAllBooks():
    if len(bookDatabase.get_all_books()) == 0:
        print("Please add some books first.")
    else:
        for book in bookDatabase.get_all_books():
            print(f"{book['title']} by {book['author']} - {book['year']}")


def addBookPrompt():
    title = input("Enter book title : ")
    author = input("Enter author name : ")
    year = input("Enter publishing year : ")
    bookDatabase.addBook(title, author, year)


def searchMenu():
    ch = input("""How would you like to search?
T for title
A for author
Y for publishing year
N for nothing.
Enter your choice : """).upper()
    return ch


def searchPrompt():
    if len(bookDatabase.get_all_books()) == 0:
        print("Please add some books first.")
    else:
        ch = searchMenu()
        while ch != "N":
            if ch == "T":
                book = input("Search by title : ")
                books = bookDatabase.searchByTitle(book)
                if len(books) == 0:
                    print("Mentioned book is not present")
                else:
                    for i in books:
                        print(f"{i['title']} by {i['author']} - {i['year']}")
                    break
            elif ch == "A":
                book = input("Search by author : ")
                books = bookDatabase.searchByAuthor(book)
                if len(books) == 0:
                    print("Mentioned book is not present")
                else:
                    for i in books:
                        print(f"{i['title']} by {i['author']} - {i['year']}")
                break
            elif ch == "Y":
                book = input("Search by year : ")
                books = bookDatabase.searchByYear(book)
                if len(books) == 0:
                    print("Mentioned book is not present")
                else:
                    for i in books:
                        print(f"{i['title']} by {i['author']} - {i['year']}")
                break
            elif ch == "N":
                pass
            else:
                print("Wrong choice")
            ch = searchMenu()


def deleteBookPrompt():
    book = input("Which book do you want to delete? : ")
    bookDatabase.deleteBook(book)


def updateByMenu():
    ch = input("""What do you want to update? 
T for title, 
A for author, 
Y for year, 
N for nothing : """).upper()
    return ch


def updateBookPrompt():
    flag = 0
    searchedBook = input("Which book needs to be updated? : ")
    books = bookDatabase.get_all_books()
    for book in books:
        if searchedBook == book['title']:
            flag = 1
            ch = updateByMenu()
            bookDatabase.updateBook(searchedBook, ch)
        else:
            pass
    if flag != 1:
        print("Book is not found")




menu()
