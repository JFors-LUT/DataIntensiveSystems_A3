import os
import sys
import sqlite3
from CreateDatabase import initialize

def menu():
    print("\nSelect an operation:")
    print("1: Show all users")
    print("2: Show all movies")
    print("3: Update user name")
    print("4: Add a new movie")
    print("5: Change user email")
    print("6: Switch database")
    print("7: Exit")
    return input("Enter choice: ")

def choose_database():
    print("Select a database:")
    print("1: db1")
    print("2: db2")
    print("3: db3")
    print("0: Exit")
    print("INIT to initialize databases, DEL to delete and re-initialize databases")
    choice = input("Enter 1, 2 or 3 (or 0): ")

    if choice == "DEL":
        delete_db()
        return choice
                        
    elif choice == "INIT":
        initialize()
        return choice
    
    elif choice == "0":
        sys.exit()
    else:
        db_path = (f"databases/db{choice}/db{choice}.sqlite")
        return db_path

def show_users(cur):
    cur.execute("""
        SELECT users.user_id, users.name, login_details.email
        FROM users
        LEFT JOIN login_details ON users.user_id = login_details.user_id
        ORDER BY users.user_id
    """)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def show_movies(cur):
    cur.execute("""
        SELECT 
            movies.title, 
            movies.genre, 
            COALESCE(watch_history.count_watched, 0) AS times_watched,
            COALESCE(ratings.avg_score, 0) AS avg_score
        FROM movies
        LEFT JOIN (
            SELECT movie_id, COUNT(*) AS count_watched
            FROM watch_history
            GROUP BY movie_id
        ) watch_history ON movies.movie_id = watch_history.movie_id
        LEFT JOIN (
            SELECT movie_id, AVG(score) AS avg_score
            FROM ratings
            GROUP BY movie_id
        ) ratings ON movies.movie_id = ratings.movie_id
        ORDER BY times_watched DESC, avg_score DESC

    """)

    rows = cur.fetchall()
    for title, genre, times_watched, avg_score in rows:
        if avg_score == 0:
            avg_score = "N/A"
        print(f"{title} | {genre} | Watched: {times_watched} times | Average rating: {avg_score}")

def update_user_name(con, cur):
    user_id = input("Enter user_id to update (0 to cancel): ")

    if user_id == "0":
        return
    
    cur.execute("SELECT email FROM login_details WHERE user_id=?", (user_id,))
    row = cur.fetchone()

    if row is None:
        print(f"No user found with ID: {user_id}.")
        return
    
    new_name = input("Enter new name: ")
    cur.execute("UPDATE users SET name=? WHERE user_id=?", (new_name, user_id))
    con.commit()
    print("User updated.")

def update_user_email(con, cur):
    user_id = input("Enter user_id to update email (0 to cancel) : ")
    if user_id == "0":
        return
    
    cur.execute("SELECT email FROM login_details WHERE user_id=?", (user_id,))
    row = cur.fetchone()

    if row is None:
        print(f"No user found with ID: {user_id}.")
        return

    print(f"Current email: {row[0]}")
    new_email = input("Enter new email: ")
    cur.execute("UPDATE login_details SET email=? WHERE user_id=?",(new_email, user_id))
    con.commit()
    print("Email updated")

def add_movie(cur, title, genre):
    cur.execute(
        "INSERT INTO movies (title, genre) VALUES (?, ?)", (title, genre))

def switch_database(con, cur):
    
    
    print("Select a database to switch to:")
    print("1: db1")
    print("2: db2")
    print("3: db3")
    choice = input("Enter 1, 2, or 3: ")
    db_path = f"databases/db{choice}/db{choice}.sqlite"
    if os.path.exists(db_path):
        con.close()
        con = sqlite3.connect(db_path)
        cur = con.cursor()
    else:
        print(f"Database {db_path} does not exist. Staying on current database.")
        return con, cur
        
    print (f"Switched to db{choice}")
    return con, cur

def delete_db():
    db_root = "databases/db"

    for i in range(1, 4):
        db_path = f"{db_root}{i}/db{i}.sqlite"
        if os.path.exists(db_path):
            os.remove(db_path)
            print(f"{db_path} deleted!")
        else:
            print(f"{db_path} does not exist.")
            return
    initialize()


def main():
    no_database = True
    db_path = choose_database()

    while no_database:
        if os.path.exists(db_path):
            con = sqlite3.connect(db_path)
            cur = con.cursor()
            print(f"Connected to {db_path}")
            no_database = False
        else:
            if db_path == "INIT" or db_path == "DEL":
                print(f"{db_path}: Database initialized.")
            else:
                print(f"Database {db_path} does not exist.")
            db_path = choose_database()


    while True:
        choice = menu()
        
        if choice == "1":
            show_users(cur)
        elif choice == "2":
            show_movies(cur)
        elif choice == "3":
            update_user_name(con, cur)
        elif choice == "4":
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            add_movie(cur, title, genre)
            con.commit()
            print("Movie added.")
        elif choice == "5":
            update_user_email(con, cur)
        elif choice == "6":
            con, cur = switch_database(con, cur)
        elif choice == "7":
            break



if __name__ == "__main__":
    main()  