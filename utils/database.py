"""
Concerning and dealing with books
Use sqlite3 database
"""
from typing import List, Dict, Union
from utils.database_connection import DatabaseConnection

FILE_NAME = 'books.json'
data_base = 'books.db'
sql_create_data_table = """
CREATE TABLE IF NOT EXISTS books(
                               name text PRIMARY KEY,
                               author text,
                               read integer
                                );
"""



def create_table() -> None:  # create a table in the database
    with DatabaseConnection(data_base) as connection:
        cursor = connection.cursor()
        cursor.execute(sql_create_data_table)


def add_book(name, author):
    with DatabaseConnection(data_base) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books values(?, ?, 0)', (name, author))
    return


def get_all_books() -> List[Book]:
    with DatabaseConnection(data_base) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        book_list = cursor.fetchall()  # [(name, author, read), (name, author, read)], list of tuples

        books = [{'name': book[0],
                  'author': book[1],
                  'read': book[2]
                  } for book in book_list ]
    return books


def mark_book(name, author):
    with DatabaseConnection(data_base) as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read = ? WHERE name = ? and author = ?', (1, name, author))
    return


def del_book(name, author):
    # delete book with (name, author)
    with DatabaseConnection(data_base) as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name = ? and author = ?', (name, author))

    return
