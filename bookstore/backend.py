import sqlite3


def create_table():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year DOUBLE, ISBN TEXT)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books VALUES(NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM books WHERE title=? or author=? or year=? or isbn=?", (title, author, year, isbn))
    rows = cursor.fetchall()
    conn.close()
    return rows


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE books SET title=?, author=?, year=?, isbn=? where id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books where id=?", (id,))
    conn.commit()
    conn.close()


create_table()
# insert("Dynamics", "Bhagya", 2020, "13DF15")
# update(1, "Statics", "Bhago", 2019, None)
# delete(1)
# print(search("", "Bhagya"))
# print(view())
