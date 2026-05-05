import random
import sqlite3

from poetry_demo.models.int_module_1_sql import Order, OrderItem, User

conn = sqlite3.connect(":memory:")

name = input("Give me a name:\n")
user_number = int(input("Give me a number:\n"))
user_order = random.choice(["small", "medium", "large"])
order_number = int(input("Give me an id:\n"))
quantity = random.randint(1, 1000)
total = random.randint(1, 1000)
discount = random.choice([True, False])


cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    user_order TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

cursor.execute("""
CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    total REAL NOT NULL,
    discount INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id)
)
""")


nuevo_usuario = User(name=name)

order = Order(user_id=user_number, user_order=user_order)

order_item = OrderItem(
    order_id=order_number, name=name, quantity=quantity, total=total, discount=discount
)


cursor.execute("INSERT INTO users (name) VALUES (?)", [nuevo_usuario.name])
conn.commit()

user_id: int | None = cursor.lastrowid


cursor.execute(
    "INSERT INTO orders (user_id, user_order) VALUES (?, ?)",
    [user_id, order.user_order],
)
conn.commit()

order_id: int | None = cursor.lastrowid

cursor.execute(
    "INSERT INTO order_items (order_id, name, quantity, total, discount) VALUES (?, ?, ?, ?, ?)",
    [
        order_id,
        order_item.name,
        order_item.quantity,
        order_item.total,
        order_item.discount,
    ],
)
conn.commit()


cursor.execute("SELECT * FROM users")
for fila in cursor.fetchall():
    print(fila)

cursor.execute("SELECT * FROM orders")
for fila in cursor.fetchall():
    print(fila)

cursor.execute("SELECT * FROM order_items")
for fila in cursor.fetchall():
    print(fila)


conn.close()
