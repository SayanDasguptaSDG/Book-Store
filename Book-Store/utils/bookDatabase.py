from .dbConnection import dbConnection


# creating a database if not exist
def createBook():
    with dbConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books (title text primary key, author text, year integer)")


# adding a book into the database
def addBook(title, author, year):
    with dbConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?, ?, ?)', (title, author, year))


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
    with dbConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE title =?', (title,))
    print(f"{title} is deleted....")


# searching a book by title
def searchBookByTitle(searchedTitle):
    with dbConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books WHERE title=?', (searchedTitle,))
        books = [{'title': row[0],
                  'author': row[1],
                  'year': row[2]}
                 for row in cursor.fetchall()]
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
    return books


# updating a book into the database
def updateBook(searchedBook, ch):
    with dbConnection('data.db') as connection:
        cursor = connection.cursor()
        if ch == "T":
            cursor.execute('UPDATE books SET title=? WHERE title=?', (input("Enter the desired title : "), searchedBook,))
        elif ch == "A":
            cursor.execute('UPDATE books SET author=? WHERE title=?', (input("Enter the desired author : "), searchedBook,))
        elif ch == "Y":
            cursor.execute('UPDATE books SET year=? WHERE title=?',
                         (input("Enter the desired publishing year : "), searchedBook,))
        else:
            print("Wrong choice")
        print(f"Book titled {searchedBook} is updated....")
