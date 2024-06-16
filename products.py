# products.py

import sqlite3
from sqlite3 import Error

# Function to create products table (if not exists)
def create_products_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL,
            supplier_id INTEGER,
            FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
        )
    ''')
    conn.commit()

# Function to add a new product
def add_product(conn, name, price, supplier_id):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, supplier_id) VALUES (?, ?, ?)", (name, price, supplier_id))
    conn.commit()
    print("Product added successfully.")

# Function to fetch all products
def get_products(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM products")
    return cursor.fetchall()

# Function to search and display all products
def search_products(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    if rows:
        print("Products:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Price: ${row[2]}, Supplier ID: {row[3]}")
    else:
        print("No products found.")
