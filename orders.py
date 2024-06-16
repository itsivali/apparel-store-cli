import sqlite3

# Function to create orders table
def create_orders_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            product_id INTEGER,
            supplier_id INTEGER,
            order_date TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers (id),
            FOREIGN KEY (product_id) REFERENCES products (id),
            FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
        )
    ''')
    conn.commit()

# Function to add a new order
def add_order(conn, customer_id, product_id, supplier_id, order_date):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO orders (customer_id, product_id, supplier_id, order_date)
        VALUES (?, ?, ?, ?)
    ''', (customer_id, product_id, supplier_id, order_date))
    conn.commit()
    print("Order added successfully.")

# Function to search and display all orders
def search_orders(conn):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT o.id, c.name AS customer_name, p.name AS product_name, s.name AS supplier_name, o.order_date
        FROM orders o
        INNER JOIN customers c ON o.customer_id = c.id
        INNER JOIN products p ON o.product_id = p.id
        INNER JOIN suppliers s ON o.supplier_id = s.id
    ''')
    rows = cursor.fetchall()
    if rows:
        print("Orders:")
        for row in rows:
            print(f"Order ID: {row[0]}, Customer: {row[1]}, Product: {row[2]}, Supplier: {row[3]}, Order Date: {row[4]}")
    else:
        print("No orders found.")
