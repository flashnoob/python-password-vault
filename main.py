import sqlite3
from argon2 import PasswordHasher
from pick import pick
from random import choice
import uuid


def random_password_gen():
    return ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789%$@') for i in range(10)])


def option_generator(display_options, title='Please choose: '):
    option, index = pick(display_options, title)
    return index


def get_user_input(message) -> object:
    data = ""
    while len(data) <= 1:
        data = input(message)
    return data





def sign_up():
    first_name = get_user_input("Enter your full name: ")
    email = get_user_input("Enter your email address: ")
    user_name = get_user_input("Enter your full name: ")
    password_option = ['Generate password :)', 'Enter your own password ']
    password=''
    index = option_generator(password_option)
    if index == 0:
        random_password = random_password_gen()
        print(random_password)
        password = random_password
    else:   password = get_user_input("Enter your password: ")




def login():
    print(2)


options = ['Login', 'signup', 'forgot password']
index = option_generator(options)
print(index)
if index == 1:
    sign_up()
elif index == 0:
    login()


# ph = PasswordHasher()
# hash = ph.hash('sachin')
# print(hash)
# print(ph.verify(hash, "1"))

def db_connect(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        con = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return con


cur = db_connect('./db.sqlite3').cursor()

customers_sql = """
CREATE TABLE user (
id integer PRIMARY KEY,
first_name text NOT NULL,
last_name text NOT NULL)"""

# response = cur.execute(customers_sql)
# print(response)
