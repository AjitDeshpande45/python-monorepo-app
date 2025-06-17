from shared.db import get_db_connection


def create_user_table():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                );
            """
            )
        conn.commit()


def add_user(name, email):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;",
                (name, email),
            )
            user_id = cur.fetchone()[0]
        conn.commit()
    return user_id


def get_all_users():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, email FROM users ORDER BY id;")
            return cur.fetchall()
