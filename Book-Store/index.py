# repository to store books
books = []

choice = input("""A for adding a book,
    R for reading a book,
    D for deleting a book,
    U for updating a book,
    Q for quitting the menu.
    Enter your choice : """).upper()

while choice != "Q":

    if choice == "A":
        title = input("Enter book title : ")
        author = input("Enter author name : ")
        year = input("Enter publishing year : ")
        books.append({
            'title': title,
            'author': author,
            'year': year
        })

    elif choice == "R":
        if len(books) == 0:
            print("No books are yet added. Please try again.")
        else:
            for i in range(len(books)):
                print(books[i])

    elif choice == "D":
        if len(books) == 0:
            print("No books are there for deletion. Please try after adding some books.")
        else:
            delBook = input("Please mention the book name : ")
            for i in range(len(books)):
                if books[i]['title'] == delBook:
                    del books[i]
                    break
            print(books)


    elif choice == "U":
        if len(books) == 0:
            print("No books are there for deletion. Please try after adding some books.")
        else:
            updateBook = input("Enter book to be updated : ")
            for i in range(len(books)):
                if books[i]['title'] == updateBook:
                    ch = input("What do you want to update? T for title, A for author, Y for year, N for nothing : ").upper()
                    while ch != "N":
                        if ch == "T":
                            books[i]['title'] = input("Enter the desired title : ")
                        elif ch == 'A':
                            books[i]['author'] = input("Enter the desired author : ")
                        elif ch == 'Y':
                            books[i]['year'] = input("Enter the desired year : ")
                        else:
                            print("Wrong choice")
                        ch = input(
                            "What do you want to update? T for title, A for author, Y for year, N for nothing : ").upper()
                else:
                    pass

    else:
        print("Something wrong")

    choice = input("""\nA for adding a book,
    R for reading a book,
    D for deleting a book,
    U for updating a book,
    Q for quitting the menu.
    Enter your choice : """).upper()
