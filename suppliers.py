# suppliers.py

import sqlite3
from sqlite3 import Error

# Function to create suppliers table (if not exists)
def create_suppliers_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT NOT NULL
        )
    ''')
    conn.commit()

# Function to add a new supplier
def add_supplier(conn, name, contact):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO suppliers (name, contact) VALUES (?, ?)", (name, contact))
    conn.commit()
    print("Supplier added successfully.")

# Function to fetch all suppliers
def get_suppliers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM suppliers")
    return cursor.fetchall()

# Function to search and display all suppliers
def search_suppliers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM suppliers")
    rows = cursor.fetchall()
    if rows:
        print("Suppliers:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Contact: {row[2]}")
    else:
        print("No suppliers found.")
