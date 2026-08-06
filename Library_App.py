import sqlite3

def create_connection():

    return sqlite3.connect(
        "Library.db"
    )

def create_table():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def add_book():

    title = input("Title : ")
    author = input("Author : ")
    quantity = int(input("Quantity : "))

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO books(
        title,
        author,
        quantity
    )
    VALUES(?,?,?)
    """,
    (title, author, quantity))

    conn.commit()
    conn.close()

    print("Book Added")

def view_books():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM books"
    )

    rows = cursor.fetchall()

    conn.close()

    print("\nBOOKS")

    for row in rows:

        print(row)

def search_book():

    keyword = input(
        "Enter Title : "
    )

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM books
    WHERE title LIKE ?
    """,
    ('%' + keyword + '%',))

    rows = cursor.fetchall()

    conn.close()

    for row in rows:

        print(row)

def update_book():

    book_id = int(
        input("ID : ")
    )

    quantity = int(
        input("Quantity : ")
    )

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE books
    SET quantity=?
    WHERE id=?
    """,
    (quantity, book_id))

    conn.commit()
    conn.close()

    print("Updated")

def delete_book():

    book_id = int(
        input("ID : ")
    )

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM books
    WHERE id=?
    """,
    (book_id,))

    conn.commit()
    conn.close()

    print("Deleted")


def menu():

    create_table()

    while True:

        print("\n1.Add Book")
        print("2.View Books")
        print("3.Search Book")
        print("4.Update Book")
        print("5.Delete Book")
        print("6.Exit")

        choice = input(
            "Enter Choice : "
        )

        if choice == "1":

            add_book()

        elif choice == "2":

            view_books()

        elif choice == "3":

            search_book()

        elif choice == "4":

            update_book()

        elif choice == "5":

            delete_book()

        elif choice == "6":

            break

        else:

            print(
                "Invalid Choice"
            )


if __name__ == "__main__":

    menu()