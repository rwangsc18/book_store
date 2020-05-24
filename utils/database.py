"""
Concerning and dealing with books
Use JSON
[
'name': book name,
'author': book author,
'read': False
]
"""
import json
from os import path
FILE_NAME = 'books.json'
CSV_FIELDNAME = ['name', 'author', 'read']


def create_table():  # create an empty JSON file
    if not path.exists(FILE_NAME): # create a new file when file does not exist
        with open(FILE_NAME, mode='w') as file:
            json.dump([], file)


def add_book(name, author):
    # load existing books
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)
    return


def _save_all_books(books):
    with open(FILE_NAME, mode='w') as file:
        json.dump(books, file)
    return


def get_all_books():
    # for book in books:
    #     str_tmp = '' if book['read'] else 'not '
    #     print(f'Book {book["name"]}, Author {book["author"]}, {str_tmp}read')
    # return
    # books = []
    with open(FILE_NAME, mode='r') as file:
        # csv_reader = csv.DictReader(csv_file, fieldnames=CSV_FIELDNAME)
        # books = [book for idx, book in enumerate(csv_reader) if idx > 0]
        books = json.load(file)
    return books


def mark_book(name, author):
    find_book = False
    books = get_all_books()
    for book in books:
        if book['name'] == name and book['author'] == author:
            book['read'] = True
            find_book = True
            break

    if find_book:
        print('Mark the book!')
    else:
        print('Fail to find this book. Please try again!')
    _save_all_books(books)

    return


def del_book(name, author):
    # delete book with (name, author)
    books = get_all_books()
    books = [book for book in books if book['name'] != name or book['author'] != author]
    _save_all_books(books)

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
