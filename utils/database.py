"""
Concerning and dealing with books
"""

books = []


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})
    return


def mark_book(name, author):
    find_book = False
    for book in books:
        if book['name'] == name and book['author'] == author:
            book['read'] = True
            find_book = True
            break

    if find_book:
        print('Mark the book!')
    else:
        print('Fail to find this book. Please try again!')

    return


def del_book(name, author):
    find_book = False
    for book in books:
        if book['name'] == name and book['author'] == author:
            books.remove(book)
            find_book = True
            break

    if find_book:
        print('Delete the book!')
    else:
        print('Fail to find this book. Please try again!')
    return