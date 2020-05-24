"""
Concerning and dealing with books
"""
import csv
FILE_NAME = 'books.txt'
CSV_FIELDNAME = ['name', 'author', 'read']


def create_table():  # create an empty txt file
    with open(FILE_NAME, mode='a'):
        pass


def add_book(name, author):
    # load existing books
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)
    return


def _save_all_books(books):
    with open(FILE_NAME, mode='w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDNAME)
        csv_writer.writeheader()
        for book in books:
            csv_writer.writerow(book)
    return


def get_all_books():
    # for book in books:
    #     str_tmp = '' if book['read'] else 'not '
    #     print(f'Book {book["name"]}, Author {book["author"]}, {str_tmp}read')
    # return
    books = []
    with open(FILE_NAME, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=CSV_FIELDNAME)
        books = [book for idx, book in enumerate(csv_reader) if idx > 0]
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
