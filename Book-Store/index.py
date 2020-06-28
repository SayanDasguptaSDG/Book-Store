# repository to store books
books = []


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


# add a book
def addBook():
    title = input("Enter book title : ")
    author = input("Enter author name : ")
    year = input("Enter publishing year : ")
    books.append({
        'title': title,
        'author': author,
        'year': year
    })


# delete a book
def deleteBook():
    flag = 0
    if len(books) == 0:
        print("No books are there for deletion. Please try after adding some books.")
    else:
        deletebook = input("Please mention the book name : ")
        for i in books:
            if i['title'] == deletebook:
                books.remove(i)
                flag = 1
                break
            else:
                pass
        if flag != 1:
            print("Mentioned book is not present")


# read a book
def readBook():
    if len(books) == 0:
        print("No books are yet added. Please try again.")
    else:
        for i in books:
            print(f"{i['title']} by {i['author']}, {i['year']}")


# update a book
def updateBook():
    flag = 0
    if len(books) == 0:
        print("No books are there for updating. Please try after adding some books.")
    else:
        updatebook = input("Enter book to be updated : ")
        for i in books:
            if i['title'] == updatebook:
                ch = updateByMenu()
                while ch != "N":
                    if ch == "T":
                        i['title'] = input("Enter the desired title : ")
                    elif ch == 'A':
                        i['author'] = input("Enter the desired author : ")
                    elif ch == 'Y':
                        i['year'] = input("Enter the desired publishing year : ")
                    else:
                        print("Please enter the choice from the set of choices")
                    ch = updateByMenu()
                flag = 1
                break
            else:
                pass
        if flag != 1:
            print("Mentioned book is not present")

def searchMenu():
    ch = input("""How would you like to search?
T for title
A for author
Y for publishing year
N for nothing.
Enter your choice : """).upper()
    return ch


# search a book
def searchBook():
    flag = 0
    if len(books) == 0:
        print("No books are there to be searched. Please try after adding some books.")
    else:
        ch = searchMenu()
        while ch != "N":
            if ch == "T":
                flag = searchByTitle(books, flag)
                break
            elif ch == "A":
                flag = searchByAuthor(books, flag)
                break
            elif ch == "Y":
                flag = searchByYear(books, flag)
                break
            else:
                print("Wrong choice")
            ch = searchMenu()

        if ch == "N":
            flag = 1

        if flag != 1:
            print("Mentioned book is not present")


# search by title
def searchByTitle(books, flag):
    searchbook = input("Search by title : ")
    for i in books:
        if searchbook == i['title']:
            print(f"{i['title']} by {i['author']}, {i['year']}")
            flag = 1
        else:
            pass
    return flag


# search by author
def searchByAuthor(books, flag):
    searchbook = input("Search by author : ")
    for i in books:
        if searchbook == i['author']:
            print(f"{i['title']} by {i['author']}, {i['year']}")
            flag = 1
        else:
            pass
    return flag


# search by publishing year
def searchByYear(books, flag):
    searchbook = input("Search by publishing year : ")
    for i in books:
        if searchbook == i['year']:
            print(f"{i['title']} by {i['author']}, {i['year']}")
            flag = 1
        else:
            pass
    return flag


# accept user choice
choice = userMenu()


# exit condition
while choice != "Q":

    if choice == "A":
        addBook()

    elif choice == "R":
        readBook()

    elif choice == "D":
        deleteBook()

    elif choice == "U":
        updateBook()

    elif choice == "S":
        searchBook()

    else:
        print("Something wrong")

    choice = userMenu()
