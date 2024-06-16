import sqlite3

def add_product(conn, name, price, supplier_id):
    sql = '''INSERT INTO products(name, price, supplier_id) VALUES(?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (name, price, supplier_id))
    conn.commit()

def update_product(conn, id, name, price):
    sql = '''UPDATE products SET name = ?, price = ? WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (name, price, id))
    conn.commit()

def list_products(conn):
    sql = '''SELECT * FROM products'''
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def search_products(conn):
    sql = '''SELECT * FROM products'''
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_product(conn, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def get_products(conn):
    """ Fetch all products from the database """
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM products")
    return cur.fetchall()
