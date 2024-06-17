# suppliers.py
import sqlite3

def get_suppliers(conn):
    """Fetch all suppliers from the database."""
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM suppliers")
    return cur.fetchall()

def add_supplier(conn, name, phone):
    sql = '''INSERT INTO suppliers (name, phone)
             VALUES (?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (name, phone))
    conn.commit()
    print(f"Supplier {name} added successfully.")

def update_supplier(conn, id, name, phone):
    sql = '''UPDATE suppliers
             SET name = ?, phone = ?
             WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (name, phone, id))
    conn.commit()
    print(f"Supplier with ID {id} updated successfully.")

def list_suppliers(conn):
    sql = '''SELECT * FROM suppliers'''
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def search_suppliers(conn):
    sql = '''SELECT * FROM suppliers'''
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_supplier(conn, id):
    sql = '''DELETE FROM suppliers WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    print(f"Supplier with ID {id} deleted successfully.")
