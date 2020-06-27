# repository to store books
books = []

# enter book title, author and year
title = input("Enter book title : ")
author = input("Enter author name : ")
year = input("Enter publishing year : ")

books = [{
    'title': title,
    'author': author,
    'year': year
}]

print(books)
