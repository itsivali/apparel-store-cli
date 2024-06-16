# cli.py

#!/usr/bin/env python

import click
from database import create_connection, initialize_database 
import customers
import products
import suppliers
import orders
import re

@click.group()
def cli():
    """
    Welcome to the Apparel Store CLI! 🛍️👗👚
    """
    pass

# Function to initialize database
def initialize_database_on_startup():
    """ Initialize the database with necessary tables """
    conn = create_connection()
    if conn:
        initialize_database(conn)
        conn.close()
    else:
        click.echo("Error! Cannot establish database connection.")
        raise click.Abort()

# Call initialize_database_on_startup() when the script runs
initialize_database_on_startup()

# Validate email format using regex
def validate_email(ctx, param, value):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
        raise click.BadParameter('Invalid email format. Please provide a valid email address.')
    return value

# Validate phone number as integer
def validate_phone(ctx, param, value):
    try:
        return int(value)
    except ValueError:
        raise click.BadParameter('Phone number must be numeric.')

@cli.command()
@click.option('--name', prompt='Customer name', help='Name of the customer')
@click.option('--email', prompt='Customer email', help='Email of the customer', callback=validate_email)
@click.option('--phone', prompt='Customer phone', help='Phone number of the customer', callback=validate_phone)
def add_customer(name, email, phone):
    """ Add a new customer to the database """
    conn = create_connection()
    if conn:
        customers.add_customer(conn, name, email, phone)
        conn.close()

@cli.command()
@click.option('--name', prompt='Product name', help='Name of the product')
@click.option('--price', prompt='Product price', type=float, help='Price of the product')
def add_product(name, price):
    """ Add a new product to the database """
    conn = create_connection()
    if conn:
        suppliers_options = suppliers.get_suppliers(conn)  # Fetch suppliers

        if not suppliers_options:
            click.echo("No suppliers found. Please add suppliers first.")
            return

        # Display supplier options to the user
        click.echo("Select supplier:")
        for idx, supplier in enumerate(suppliers_options, start=1):
            click.echo(f"{idx}. {supplier[1]}")

        supplier_choice = click.prompt("Enter supplier number", type=int)

        if supplier_choice < 1 or supplier_choice > len(suppliers_options):
            click.echo("Invalid supplier number.")
            return

        supplier_id = suppliers_options[supplier_choice - 1][0]

        products.add_product(conn, name, price, supplier_id)  # Pass supplier_id as the fourth argument
        conn.close()

@cli.command()
@click.option('--name', prompt='Supplier name', help='Name of the supplier')
@click.option('--phone', prompt='Supplier phone number', help='Phone number of the supplier', callback=validate_phone)
def add_supplier(name, phone):
    """ Add a new supplier to the database """
    conn = create_connection()
    if conn:
        suppliers.add_supplier(conn, name, phone)
        conn.close()

@cli.command()
@click.option('--order_date', prompt='Order date', help='Date of the order (YYYY-MM-DD)')
def add_order(order_date):
    """ Add a new order to the database """
    conn = create_connection()
    if conn:
        products_options = products.get_products(conn)  # Fetch products
        customers_options = customers.get_customers(conn)  # Fetch customers

        if not products_options:
            click.echo("No products found. Please add products first.")
            return

        if not customers_options:
            click.echo("No customers found. Please add customers first.")
            return

        # Display options to the user
        click.echo("Select product:")
        for idx, product in enumerate(products_options, start=1):
            click.echo(f"{idx}. {product[1]}")

        product_choice = click.prompt("Enter product number", type=int)

        click.echo("Select customer:")
        for idx, customer in enumerate(customers_options, start=1):
            click.echo(f"{idx}. {customer[1]}")

        customer_choice = click.prompt("Enter customer number", type=int)

        # Example: Hardcoded supplier_id for demonstration
        supplier_id = 1

        # Add order to the database
        orders.add_order(conn, customers_options[customer_choice - 1][0], products_options[product_choice - 1][0], supplier_id, order_date)
        
        conn.close()

@cli.command()
def search_customers():
    """ Search and display all customers """
    conn = create_connection()
    if conn:
        customers.search_customers(conn)
        conn.close()

@cli.command()
def search_products():
    """ Search and display all products """
    conn = create_connection()
    if conn:
        products.search_products(conn)
        conn.close()

@cli.command()
def search_suppliers():
    """ Search and display all suppliers """
    conn = create_connection()
    if conn:
        suppliers.search_suppliers(conn)
        conn.close()

@cli.command()
def search_orders():
    """ Search and display all orders """
    conn = create_connection()
    if conn:
        orders.search_orders(conn)
        conn.close()

if __name__ == '__main__':
    cli()
