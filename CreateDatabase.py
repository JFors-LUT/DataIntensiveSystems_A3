import os
import sqlite3
from dummy_data import replicated_users, fragmented_users_db1, fragmented_users_db2, fragmented_users_db3
from dummy_data import replicated_movies, fragmented_movies_db1, fragmented_movies_db2, fragmented_movies_db3   
from dummy_data import replicated_logins, fragmented_logins_db1, fragmented_logins_db2, fragmented_logins_db3
from dummy_data import replicated_history, fragmented_history_db1, fragmented_history_db2, fragmented_history_db3
from dummy_data import replicated_ratings, fragmented_ratings_db1, fragmented_ratings_db2, fragmented_ratings_db3   



#Config
database_directory = "databases"
db_names = ["db1", "db2", "db3"]
    
tables = {
        "users": """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                name TEXT   
            );
        """,
        "login_details": """
            CREATE TABLE IF NOT EXISTS login_details (
                user_id INTEGER,
                email TEXT,
                password TEXT,
                PRIMARY KEY (user_id),
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            );
        """,
        "movies": """
            CREATE TABLE IF NOT EXISTS movies (
                movie_id INTEGER PRIMARY KEY,
                title TEXT,
                genre TEXT
            );
        """,
        "watch_history": """
            CREATE TABLE IF NOT EXISTS watch_history (
                history_id INTEGER PRIMARY KEY,
                user_id integer,
                movie_id integer,
                watch_date TEXT,
                FOREIGN KEY(user_id) REFERENCES users(user_id),
                FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
            );
        """,
        "ratings": """
            CREATE TABLE IF NOT EXISTS ratings (
                rating_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                movie_id INTEGER,
                score INTEGER
            );
        """
        }

def insert_dummy_data(cursor, db_name):

    fragmented_users_map = {
        "db1": fragmented_users_db1,
        "db2": fragmented_users_db2,
        "db3": fragmented_users_db3
    }
    fragmented_movies_map = {
        "db1": fragmented_movies_db1,
        "db2": fragmented_movies_db2,
        "db3": fragmented_movies_db3
    }
    fragmented_logins_map = {
        "db1": fragmented_logins_db1,
        "db2": fragmented_logins_db2,
        "db3": fragmented_logins_db3
    }
    fragmented_history_map = {
        "db1": fragmented_history_db1,
        "db2": fragmented_history_db2,
        "db3": fragmented_history_db3
    }
    fragmented_ratings_map = {
        "db1": fragmented_ratings_db1,
        "db2": fragmented_ratings_db2,
        "db3": fragmented_ratings_db3
    }

    for user in list(replicated_users) + list(fragmented_users_map[db_name]):
        cursor.execute("INSERT OR IGNORE INTO users (user_id, name) VALUES (?, ?)", user)

    for movie in list(replicated_movies) + list(fragmented_movies_map[db_name]):
        cursor.execute("INSERT OR IGNORE INTO movies (movie_id, title, genre) VALUES (?, ?, ?)", movie)

    for login in list(replicated_logins) + list(fragmented_logins_map[db_name]):
        cursor.execute("INSERT OR IGNORE INTO login_details (user_id, email, password) VALUES (?, ?, ?)", login)

    for history in list(replicated_history) + list(fragmented_history_map[db_name]):
        cursor.execute("INSERT OR IGNORE INTO watch_history (history_id, user_id, movie_id, watch_date) VALUES (?, ?, ?, ?)", history)

    for rating in list(replicated_ratings) + list(fragmented_ratings_map[db_name]):
        cursor.execute("INSERT OR IGNORE INTO ratings (rating_id, user_id, movie_id, score) VALUES (?, ?, ?, ?)", rating)

def initialize():
    os.makedirs(database_directory, exist_ok=True)
    for db in db_names:
        folder_path = os.path.join(database_directory, db)
        os.makedirs(folder_path, exist_ok=True)

        db_path = os.path.join(folder_path, f"{db}.sqlite")

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        for tname, tddl in tables.items():
            cur.execute(tddl)

        insert_dummy_data(cur, db)

        conn.commit()
        conn.close()
        check_db_creation(db_path)

def check_db_creation(db_path):
    new_con = sqlite3.connect(db_path)
    new_cur = new_con.cursor()
    res = new_cur.execute("SELECT user_id, name FROM users ORDER BY user_id DESC")
    id, name = res.fetchone()
    print(f'Last user id {id}, with name {name}')
    new_con.close()

if __name__ == "__main__":   
    initialize()
    print("All databases created successfully.")