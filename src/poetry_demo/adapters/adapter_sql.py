import sqlite3

from poetry_demo.domain.ports import CreateOrder


class RetrieveResponseSql(CreateOrder):
    def __init__(self, base_url: str):
        self.conn = sqlite3.connect(base_url)
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            user_order TEXT NOT NULL
        )
        """)

    def get_order(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE id=?", (1,))
        return cursor.fetchone()

    def insert(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO orders (user_id, user_order) VALUES (?, ?)",
            [1, 12],
        )
        self.conn.commit()
