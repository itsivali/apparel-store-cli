import sqlite3

def add_supplier(conn, name, phone):
    sql = '''INSERT INTO suppliers(name, phone) VALUES(?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (name, phone))
    conn.commit()

def update_supplier(conn, id, name, phone):
    sql = '''UPDATE suppliers SET name = ?, phone = ? WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (name, phone, id))
    conn.commit()

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
    conn
