# dummy_data.py

# user_ID, name
replicated_users = {
    (1, "Alice"), (2, "Bob"), (3, "Charlie"), (4, "Diana"), (5, "Ethan")
}

fragmented_users_db1 = {    
    (6, "Fay"), (7, "George"), (8, "Hannah"), (9, "Ian"), (10, "Julia")
}

fragmented_users_db2 = {
    (6, "Kara"), (7, "Leo"), (8, "Maya"), (9, "Nate"), (10, "Olivia")
}

fragmented_users_db3 = { 
    (6, "Paul"), (7, "Quinn"), (8, "Rita"), (9, "Sam"), (10, "Tina")
}


# movie_ID, title, genre
replicated_movies = {
    (1, "Inception", "Sci-Fi"),
    (2, "The Matrix", "Sci-Fi"),
    (3, "The Godfather", "Crime"),
    (4, "Titanic", "Romance"),
    (5, "The Dark Knight", "Action")
}

fragmented_movies_db1 = {
    (6, "Forrest Gump", "Drama"),
    (7, "Gladiator", "Action"),
    (8, "Toy Story", "Animation"),
    (9, "Interstellar", "Sci-Fi"),
    (10, "Avatar", "Fantasy")
}

fragmented_movies_db2 = {
    (6, "Joker", "Crime"),
    (7, "Frozen", "Animation"),
    (8, "Avengers", "Action"),
    (9, "La La Land", "Romance"),
    (10, "Mad Max", "Action")
}

fragmented_movies_db3 = {
    (6, "Coco", "Animation"),
    (7, "Parasite", "Thriller"),
    (8, "Up", "Animation"),
    (9, "Shrek", "Comedy"),
    (10, "The Lion King", "Animation")
}

# user_ID, email, password_hash
replicated_logins = {
    (1, "alice@example.com", "hash1"),
    (2, "bob@example.com", "hash2"),
    (3, "charlie@example.com", "hash3"),
    (4, "diana@example.com", "hash4"),
    (5, "ethan@example.com", "hash5")
}

fragmented_logins_db1 = {
    (6, "fay@example.com", "hash6"),
    (7, "george@example.com", "hash7"),
    (8, "hannah@example.com", "hash8"),
    (9, "ian@example.com", "hash9"),
    (10, "julia@example.com", "hash10")
}

fragmented_logins_db2 = {
    (6, "kara@example.com", "hash6"),
    (7, "leo@example.com", "hash7"),
    (8, "maya@example.com", "hash8"),
    (9, "nate@example.com", "hash9"),
    (10, "olivia@example.com", "hash10")
}

fragmented_logins_db3 = {
    (6, "paul@example.com", "hash6"),
    (7, "quinn@example.com", "hash7"),
    (8, "rita@example.com", "hash8"),
    (9, "sam@example.com", "hash9"),
    (10, "tina@example.com", "hash10")
}

#history_id, user_id, movie_id, watch_date
replicated_history = {
    (1, 1, 1, "2025-11-01"),
    (2, 2, 2, "2025-11-02"),
    (3, 3, 3, "2025-11-02"),
    (4, 4, 4, "2025-11-02"),
    (5, 5, 5, "2025-11-02")
}

fragmented_history_db1 = {
    (6, 5, 6, "2025-11-05"),
    (7, 5, 7, "2025-11-12"),
    (8, 1, 8, "2025-12-6"),
    (9, 9, 9, "2025-12-09"),
    (10, 10, 1, "2025-12-10")
}

fragmented_history_db2 = {
    (6, 6, 6, "2025-11-06"),
    (7, 7, 7, "2025-11-07"),
    (8, 8, 8, "2025-11-08"),
    (9, 8, 9, "2025-11-09"),
    (10, 10, 10, "2025-11-10")
}

fragmented_history_db3 = {
    (6, 6, 6, "2025-11-06"),
    (7, 6, 7, "2025-11-07"),
    (8, 8, 8, "2025-11-08"),
    (9, 9, 9, "2025-11-09"),
    (10, 9, 10, "2025-11-10")
}

# rating_id, user_id, movie_id, score
replicated_ratings = {
    (1, 1, 1, 5),
    (2, 2, 2, 4),
    (3, 3, 3, 5),
    (4, 4, 4, 3),
    (5, 5, 5, 4)
}

fragmented_ratings_db1 = {
    (6, 6, 6, 2),
    (7, 1, 7, 3),
    (8, 2, 1, 5),
    (9, 1, 9, 1),
    (10, 1, 3, 4)
}

fragmented_ratings_db2 = {
    (6, 6, 6, 4),
    (7, 7, 7, 2),
    (8, 8, 8, 3),
    (9, 9, 9, 5),
    (10, 10, 10, 1)
}

fragmented_ratings_db3 = {
    (6, 6, 6, 3),
    (7, 7, 7, 5),
    (8, 8, 8, 2),
    (9, 9, 9, 4),
    (10, 10, 10, 1)
}