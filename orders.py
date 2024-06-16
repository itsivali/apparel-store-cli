import sqlite3

def add_order(conn, customer_id, product_id, supplier_id, order_date):
    sql = '''INSERT INTO orders (customer_id, product_id, supplier_id, order_date)
             VALUES (?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (customer_id, product_id, supplier_id, order_date))
    conn.commit()
    print("Order added successfully.")

def update_order(conn, id, order_date):
    sql = '''UPDATE orders
             SET order_date = ?
             WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (order_date, id))
    conn.commit()
    print(f"Order with ID {id} updated successfully.")

def list_orders(conn):
    sql = '''SELECT * FROM orders'''
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def search_orders(conn):
    sql = '''SELECT * FROM orders'''
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_order(conn, id):
    sql = '''DELETE FROM orders WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    print(f"Order with ID {id} deleted successfully.")

def get_orders(conn):
    """ Fetch all orders from the database """
    cur = conn.cursor()
    cur.execute("SELECT id, customer_id, product_id, supplier_id, order_date FROM orders")
    return cur.fetchall()
