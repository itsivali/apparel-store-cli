import sqlite3

def add_customer(conn, name, email, phone):
    sql = '''INSERT INTO customers (name, email, phone)
             VALUES (?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (name, email, phone))
    conn.commit()
    print(f"Customer {name} added successfully.")

def update_customer(conn, id, name, email, phone):
    sql = '''UPDATE customers
             SET name = ?, email = ?, phone = ?
             WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (name, email, phone, id))
    conn.commit()
    print(f"Customer with ID {id} updated successfully.")

def list_customers(conn):
    sql = '''SELECT * FROM customers'''
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def search_customers(conn):
    sql = '''SELECT * FROM customers'''
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_customer(conn, id):
    sql = '''DELETE FROM customers WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    print(f"Customer with ID {id} deleted successfully.")

def get_customers(conn):
    """ Fetch all customers from the database """
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM customers")
    return cur.fetchall()
