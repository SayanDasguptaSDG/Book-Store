import os

books_file = "books.txt"


def createBook():
    if os.path.isfile(books_file):
        pass
    else:
        with open(books_file, 'w') as file:
            pass


def addBook(title, author, year):
    with open(books_file, 'a') as file:
        file.write(f'{title},{author},{year}\n')
    print(f"Book titled {title} by {author} is added")


def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'title': line[0], 'author': line[1], 'year': line[2]}
        for line in lines
    ]


def saveAllBooks(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['title']},{book['author']},{book['year']}\n")


def searchByTitle(title):
    books = get_all_books()
    books = [book for book in books if title in book['title']]
    return books


def searchByAuthor(author):
    books = get_all_books()
    books = [book for book in books if author in book['author']]
    return books


def searchByYear(year):
    books = get_all_books()
    books = [book for book in books if year in book['year']]
    return books


def deleteBook(title):
    books = get_all_books()
    books = [book for book in books if book['title'] != title]
    saveAllBooks(books)
    print(f"Book titled {title} is deleted")


def updateBook(searchedBook, ch):
    books = get_all_books()
    for book in books:
        if searchedBook == book['title']:
            if ch == "T":
                book['title'] = input("Enter the desired title : ")
            elif ch == "A":
                book['author'] = input("Enter the desired author : ")
            elif ch == "Y":
                book['year'] = input("Enter the desired year : ")
            else:
                print("Wrong choice")
            print(f"Book(s) titled {searchedBook} is/are updated")
        else:
            pass
    saveAllBooks(books)