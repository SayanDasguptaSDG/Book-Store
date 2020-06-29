from utils import bookDatabase


######################################## MENUS ########################################


# user menu
def userMenu():
    print("===============================================")
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
    print("===============================================")
    ch = input("""What do you want to update? 
T for title, 
A for author, 
Y for year, 
N for nothing : """).upper()
    return ch


# search menu
def searchMenu():
    print("===============================================")
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


# count number of digits in year
def countDigits(year):
    count = 0
    while year != 0:
        count = count + 1
        year = year // 10
    return count


# display all books
def listAllBooks():
    print("===============================================")
    if len(bookDatabase.get_all_books()) == 0:
        print("Please add some books first.")
    else:
        for book in bookDatabase.get_all_books():
            print(f"{book['title']} by {book['author']} - {book['year']}")


# prompt for adding a book into the database
def addBookPrompt():
    print("===============================================")
    try:
        title = input("Enter book title : ")
        author = input("Enter author name : ")
        year = int(input("Enter publishing year : "))
        count = int(countDigits(year))
        if count == 4:
            bookDatabase.addBook(title, author, year)
        else:
            print("Year must be a four digit number")
    except ValueError:
        print("Year must be numeric")


# prompt for deleting a book from the database
def deleteBookPrompt():
    print("===============================================")
    check = bookDatabase.checkDbEmpty()
    if check == "false":
        book = input("Which book do you want to delete? : ")
        bookDatabase.deleteBook(book)
    else:
        print(check)


# prompt for searching the book in the database
def searchPrompt():
    print("===============================================")
    check = bookDatabase.checkDbEmpty()
    if check == "false":
        if len(bookDatabase.get_all_books()) == 0:
            print("===============================================")
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
                        print(f"\{i['title']} by {i['author']} - {i['year']}")
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
    else:
        print(check)


# prompt for updating the values into the database
def updateBookPrompt():
    print("===============================================")
    check = bookDatabase.checkDbEmpty()
    if check == "false":
        searchedBook = input("Which book needs to be updated? : ")
        if len(bookDatabase.searchBookByTitle(searchedBook)) == 0:
            print("Mentioned book is not found")
        else:
            ch = updateByMenu()
            bookDatabase.updateBook(searchedBook, ch)
    else:
        print(check)


# entry point of the application - calling the main menu function
menu()
