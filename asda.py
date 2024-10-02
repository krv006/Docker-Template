import psycopg2
import os


db_name = os.getenv("POSTGRES_DB")
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT", "5432")



def get_connection():
    return psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )



def create_books_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        price INTEGER
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()



def add_book(id, name, price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO books (id, name, price) VALUES (%s, %s, %s)
    """, (id, name, price))
    conn.commit()
    cursor.close()
    conn.close()
    print("Kitob qo'shildi!")


def view_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    conn.close()

    if books:
        print("Kitoblar ro'yxati:")
        for book in books:
            print(f"ID: {book[0]}, Nomi: {book[1]}, Narxi: {book[2]}")
    else:
        print("Hozircha kitoblar yo'q.")



def main():
    create_books_table() 
    while True:
        print("Menu:")
        print("1. Kitob qo'shish")
        print("2. Kitoblarni ko'rish")
        print("3. Chiqish")

        a = int(input("Tanlang: "))

        if a == 1:
            id = int(input("ID kiriting: "))
            name = input("Ism kiriting: ")
            price = int(input("Narx kiriting: "))
            add_book(id, name, price)
        elif a == 2:
            view_books()
        elif a == 3:
            print("Xayr!")
            break
        else:
            print("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")


if __name__ == "__main__":
    main()

