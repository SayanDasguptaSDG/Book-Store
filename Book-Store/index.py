from utils import bookDatabase


######################################## MENUS ########################################


# user menu
def userMenu():
    print("================================================================================")
    menu = input("""Add - adding a book,
List - list all the books,
Delete - deleting a book,
Updating - updating a book,
Searching - searching a book,
Quit - quitting the menu.
Enter your choice : """).lower()
    return menu


# update menu
def updateByMenu():
    print("================================================================================")
    ch = input("""What do you want to update?
Title - update the title,
Author - update the author,
Year - update the publishing year.
Enter your choice: """).lower()
    return ch


# search menu
def searchMenu():
    print("================================================================================")
    ch = input("""How would you like to search?
Title - search by title
Author - search by author
Year - search by publishing year
Enter your choice : """).lower()
    return ch


######################################## MAIN MENU ########################################


def menu():
    bookDatabase.createBook()
    # accept user choice
    choice = userMenu()
    # exit condition
    while choice != "quit":
        if choice == "add":
            addBookPrompt()
        elif choice == "list":
            listAllBooks()
        elif choice == "search":
            searchPrompt()
        elif choice == "delete":
            deleteBookPrompt()
        elif choice == "update":
            updateBookPrompt()
        else:
            print("================================================================================")
            print("Something went wrong.")
        choice = userMenu()


######################################## FEATURES ########################################


# count number of digits in year
def countDigits(year):
    count = 0
    while year != 0:
        count = count + 1
        year = year // 10
    return count


# valid title or not
def isValidTitle(title):
    if any(a.isalpha() for a in title) and \
            all(t.isalpha() or t.isspace() or
                t.isdigit() for t in title) and \
            title.startswith(' ') != True and title.endswith(' ') != True:
        return True
    else:
        return False


# valid author or not
def isValidAuthor(author):
    if any(a.isalpha() for a in author) and \
            all(a.isalpha() or a.isspace() for a in author) \
            and author.startswith(' ') != True and author.endswith(' ') != True:
        return True
    else:
        return False


# display all books
def listAllBooks():
    print("================================================================================")
    if len(bookDatabase.get_all_books()) == 0:
        print("Please add some books first.")
    else:
        for book in bookDatabase.get_all_books():
            print(f"{book['title']} by {book['author']} - {book['year']}")


# prompt for adding a book into the database
def addBookPrompt():
    print("================================================================================")
    try:
        title = input("Enter book title : ")
        author = input("Enter author name : ")
        year = int(input("Enter publishing year : "))
        count = int(countDigits(year))
        titleValidation = isValidTitle(title)
        authorValidation = isValidAuthor(author)
        if count == 4 and titleValidation and authorValidation:
            bookDatabase.addBook(title, author, year)
        else:
            print("================================================================================")
            print("""Incompatible entries.
Title cannot be empty.
Title cannot start or end with a space and cannot end with a space.
Author cannot contain any numeric character
Author cannot start and end with a space.""")
    except ValueError:
        print("================================================================================")
        print("Year must be numeric.")


# prompt for deleting a book from the database
def deleteBookPrompt():
    print("================================================================================")
    check = bookDatabase.checkDbEmpty()
    if check == "false":
        book = input("Which book do you want to delete? : ")
        bookDatabase.deleteBook(book)
    else:
        print(check)


# prompt for searching the book in the database
def searchPrompt():
    check = bookDatabase.checkDbEmpty()
    if check == "false":
        ch = searchMenu()
        print("================================================================================")
        if ch == "title":
            searchedTitle = input("Search by title : ")
            books = bookDatabase.searchBookByTitle(searchedTitle)
            if len(books) == 0:
                print("================================================================================")
                print("Mentioned book is not present.")
            else:
                print("================================================================================")
                for i in books:
                    print(f"{i['title']} by {i['author']} - {i['year']}")
        elif ch == "author":
            searchedAuthor = input("Search by author : ")
            books = bookDatabase.searchBookByAuthor(searchedAuthor)
            if len(books) == 0:
                print("================================================================================")
                print("Books from mentioned author is not present.")
            else:
                print("================================================================================")
                for i in books:
                    print(f"{i['title']} by {i['author']} - {i['year']}")
        elif ch == "year":
            searchedYear = input("Search by publishing year : ")
            books = bookDatabase.searchBookByYear(searchedYear)
            if len(books) == 0:
                print("================================================================================")
                print("Books published in mentioned year is not present.")
            else:
                print("================================================================================")
                for i in books:
                    print(f"{i['title']} by {i['author']} - {i['year']}")
        else:
            print("Please select from the above choices only.\nReturning back to menu.")
    else:
        print("================================================================================")
        print(check)


# prompt for updating the values into the database
def updateBookPrompt():
    print("================================================================================")
    check = bookDatabase.checkDbEmpty()
    if check == "false":
        searchedBook = input("Which book needs to be updated? : ")
        if len(bookDatabase.searchBookByTitle(searchedBook)) == 0:
            print("================================================================================")
            print("Mentioned book is not found.")
        else:
            ch = updateByMenu()
            bookDatabase.updateBook(searchedBook, ch)
    else:
        print(check)


# entry point of the application - calling the main menu function
menu()
