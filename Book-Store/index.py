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
    if len(books) == 0:
        print("No books are there for deletion. Please try after adding some books.")
    else:
        delbook = input("Please mention the book name : ")
        for i in range(len(books)):
            if books[i]['title'] == delbook:
                del books[i]
                break
            else:
                print("Mentioned book is not present")


# read a book
def readBook():
    if len(books) == 0:
        print("No books are yet added. Please try again.")
    else:
        for i in range(len(books)):
            print(books[i])


# update a book
def updateBook():
    if len(books) == 0:
        print("No books are there for updation. Please try after adding some books.")
    else:
        updatebook = input("Enter book to be updated : ")
        for i in range(len(books)):
            if books[i]['title'] == updatebook:
                ch = updateByMenu()
                while ch != "N":
                    if ch == "T":
                        books[i]['title'] = input("Enter the desired title : ")
                    elif ch == 'A':
                        books[i]['author'] = input("Enter the desired author : ")
                    elif ch == 'Y':
                        books[i]['year'] = input("Enter the desired year : ")
                    else:
                        print("Wrong choice")
                    ch = updateByMenu()
            else:
                print("Mentioned book is not present")


#search a book
def searchBook():
    if len(books) == 0:
        print("No books are there to be searched. Please try after adding some books.")
    else:
        searchbook = input("Search by title : ")
        for i in range(len(books)):
            if searchbook == books[i]['title']:
                print(books[i])
            else:
                print("Mentioned book is not present")


#accept user choice
choice = userMenu()

#exit condition
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
