import sqlite3
from sqlite3 import Error

# Function to create a database connection
def create_connection(db_file='apparel_store.db'):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

# Function to create all necessary tables
def initialize_database(conn):
    """ Initialize the database with necessary tables """
    create_customers_table(conn)
    create_products_table(conn)
    create_suppliers_table(conn)
    create_orders_table(conn)
    print("Database initialized successfully!")

# Function to create customers table
def create_customers_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS customers
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     email TEXT NOT NULL,
                     phone INTEGER)''')
    except Error as e:
        print(e)

# Function to create products table
def create_products_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS products
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     price REAL NOT NULL,
                     supplier_id INTEGER,
                     FOREIGN KEY (supplier_id) REFERENCES suppliers (id))''')
    except Error as e:
        print(e)

# Function to create suppliers table
def create_suppliers_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS suppliers
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     contact TEXT NOT NULL)''')
    except Error as e:
        print(e)

# Function to create orders table
def create_orders_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS orders
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     customer_id INTEGER,
                     product_id INTEGER,
                     supplier_id INTEGER,
                     order_date TEXT NOT NULL,
                     FOREIGN KEY (customer_id) REFERENCES customers (id),
                     FOREIGN KEY (product_id) REFERENCES products (id),
                     FOREIGN KEY (supplier_id) REFERENCES suppliers (id))''')
    except Error as e:
        print(e)
