from .dbConnection import dbConnection


# creating a database if not exist
def createBook():
    with dbConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books (title VARCHAR(50) NOT NULL primary key, author VARCHAR(25), year INTEGER(4))")


# check if database is empty
def checkDbEmpty():
    books = get_all_books()
    if len(books) == 0:
        return "Please add some books first."
    else:
        return "false"


# adding a book into the database
def addBook(title, author, year):
    with dbConnection('data.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO books VALUES(?, ?, ?)', (title, author, year))
            print("===============================================")
            print(f'{title} is added.')
        except:
            print("===============================================")
            print(f'{title} is already available.')


# displaying all the books from the database
def get_all_books():
    with dbConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = [{'title': row[0],
                  'author': row[1],
                  'year': row[2]}
                 for row in cursor.fetchall()]
    return books


# deleting a book from the database
def deleteBook(title):
    books = searchBookByTitle(title)
    if len(books) == 0:
        print("===============================================")
        print("Mentioned book is not present.")
    else:
        with dbConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM books WHERE title =?', (title,))
            print("===============================================")
            print(f"{title} is deleted.")


# searching a book by title
def searchBookByTitle(searchedTitle):
    with dbConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books WHERE title=?', (searchedTitle,))
        books = [{'title': row[0],
                  'author': row[1],
                  'year': row[2]}
                 for row in cursor.fetchall()]
        if len(books) == 0:
            return []
        else:
            return books


# searching a book by author
def searchBookByAuthor(searchedAuthor):
    with dbConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books WHERE author=?', (searchedAuthor,))
        books = [{'title': row[0],
                  'author': row[1],
                  'year': row[2]}
                 for row in cursor.fetchall()]
        if len(books) == 0:
            return []
        else:
            return books


# searching a book by year
def searchBookByYear(searchedYear):
    with dbConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books WHERE year=?', (searchedYear,))
        books = [{'title': row[0],
                  'author': row[1],
                  'year': row[2]}
                 for row in cursor.fetchall()]
        if len(books) == 0:
            return []
        else:
            return books


# updating a book into the database
def updateBook(searchedBook, ch):
    with dbConnection('data.db') as connection:
        cursor = connection.cursor()
        if ch == "title":
            cursor.execute('UPDATE books SET title=? WHERE title=?',
                           (input("Enter the desired title : "), searchedBook,))
            print("===============================================")
            print(f"Book titled {searchedBook} is updated.")
        elif ch == "author":
            cursor.execute('UPDATE books SET author=? WHERE title=?',
                           (input("Enter the desired author : "), searchedBook,))
            print("===============================================")
            print(f"Book titled {searchedBook} is updated.")
        elif ch == "year":
            cursor.execute('UPDATE books SET year=? WHERE title=?',
                           (input("Enter the desired publishing year : "), searchedBook,))
            print("===============================================")
            print(f"Book titled {searchedBook} is updated.")
        else:
            print("===============================================")
            print("Please select from the above choices only.\nReturning back to menu.")
