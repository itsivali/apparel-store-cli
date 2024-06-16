import sqlite3
from sqlite3 import Error

# Function to create a database connection
def create_connection(db_file='apparel_store.db'):
    """ Create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

# Function to create customers table if not exists
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

# Function to add a new customer
def add_customer(conn, name, email, phone=None):
    """ Add a new customer to the database """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        conn.commit()
        print("Customer added successfully.")
    except Error as e:
        print(e)

# Function to fetch all customers
def get_customers(conn):
    """ Fetch all customers from the database """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM customers")
        return cursor.fetchall()
    except Error as e:
        print(e)

# Function to search and display all customers
def search_customers(conn):
    """ Search and display all customers """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        if rows:
            print("Customers:")
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Phone: {row[3] if len(row) > 3 else 'N/A'}")
        else:
            print("No customers found.")
    except Error as e:
        print(e)

# Example usage if this script is run directly
if __name__ == '__main__':
    conn = create_connection()
    if conn:
        create_customers_table(conn)
        
        # Example of adding a customer
        add_customer(conn, "John Doe", "john@example.com", "123456789")
        
        # Example of fetching all customers
        customers = get_customers(conn)
        print("All Customers:")
        for customer in customers:
            print(f"ID: {customer[0]}, Name: {customer[1]}")
        
        # Example of searching customers
        search_customers(conn)
        
        conn.close()
    else:
        print("Error! Cannot establish database connection.")
