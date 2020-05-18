# This file implements the main menu of the book_store project
from utils import database


def prompt_add_book():
    name, author = input('Input the book name and author, separated by comma:').split(',')
    name = name.strip().title()
    author = author.strip().title()
    database.add_book(name, author)
    return


def list_book():
    database.get_all_books()


def prompt_read_book():
    name, author = input('Input the book name and author to mark as read, separated by comma: ').split(',')
    name = name.strip().title()
    author = author.strip().title()
    database.mark_book(name, author)
    return


def prompt_delete_book():
    name, author = input('Input the book name and author to mark as read, separated by comma: ').split(',')
    database.del_book(name.title(), author.title())
    return



USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """
operations = {
    'a': prompt_add_book,
    'l': list_book,
    'r': prompt_read_book,
    'd': prompt_delete_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in operations:
            operation = operations[user_input]
            operation()
        else:
            print('Unknown command. Please try again.')
        user_input = input(USER_CHOICE)


menu()