"""
Concerning and dealing with books
Use JSON
[
'name': book name,
'author': book author,
'read': False
]
"""
import sqlite3
import json
from os import path

FILE_NAME = 'books.json'
data_base = 'books.db'
sql_create_data_table = """
CREATE TABLE IF NOT EXISTS books(
                               name text PRIMARY KEY,
                               author text,
                               read integer
                                );
"""
CSV_FIELDNAME = ['name', 'author', 'read']


def create_table():  # create a table in the database
    connection = sqlite3.connect(data_base)  # create a connection
    cursor = connection.cursor()
    cursor.execute(sql_create_data_table)
    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect(data_base)  # create a connection
    cursor = connection.cursor()
    # sql query
    cursor.execute('INSERT INTO books values(?, ?, 0)', (name, author))
    connection.commit()
    connection.close()
    return


def _save_all_books(books):
    with open(FILE_NAME, mode='w') as file:
        json.dump(books, file)
    return


def get_all_books():
    connection = sqlite3.connect(data_base)  # create a connection
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    book_list = cursor.fetchall()  # [(name, author, read), (name, author, read)], list of tuples

    books = [{'name': book[0],
              'author': book[1],
              'read': book[2]
              } for book in book_list ]
    connection.close()
    return books


def mark_book(name, author):
    connection = sqlite3.connect(data_base)  # create a connection
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read = ? WHERE name = ? and author = ?', (1, name, author))
    connection.commit()
    connection.close()

    return


def del_book(name, author):
    # delete book with (name, author)
    connection = sqlite3.connect(data_base)  # create a connection
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name = ? and author = ?', (name, author))
    connection.commit()
    connection.close()

    return
    ### Alternative method (For loop):
    # find_book = False
    # for book in books:
    #     if book['name'] == name and book['author'] == author:
    #         books.remove(book)
    #         find_book = True
    #         break
    #
    # if find_book:
    #     print('Delete the book!')
    # else:
    #     print('Fail to find this book. Please try again!')
