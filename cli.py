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

# Add, update, list, search, and delete customers
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
@click.option('--id', prompt='Customer ID', type=int, help='ID of the customer to update')
@click.option('--name', prompt='New customer name', help='New name of the customer')
@click.option('--email', prompt='New customer email', help='New email of the customer', callback=validate_email)
@click.option('--phone', prompt='New customer phone', help='New phone number of the customer', callback=validate_phone)
def update_customer(id, name, email, phone):
    """ Update an existing customer in the database """
    conn = create_connection()
    if conn:
        customers.update_customer(conn, id, name, email, phone)
        conn.close()

@cli.command()
def list_customers():
    """ List all customers """
    conn = create_connection()
    if conn:
        customers.list_customers(conn)
        conn.close()

@cli.command()
def search_customers():
    """ Search and display all customers """
    conn = create_connection()
    if conn:
        customers.search_customers(conn)
        conn.close()

@cli.command()
def delete_customer():
    """ Delete a customer from the database """
    conn = create_connection()
    if conn:
        customer_options = customers.get_customers(conn)
        if not customer_options:
            click.echo("No customers found.")
            return

        # Display customer options to the user
        click.echo("Select customer to delete:")
        for idx, customer in enumerate(customer_options, start=1):
            click.echo(f"{idx}. ID: {customer[0]}, Name: {customer[1]}")

        customer_choice = click.prompt("Enter customer number", type=int)

        if customer_choice < 1 or customer_choice > len(customer_options):
            click.echo("Invalid customer number.")
            return

        customer_id = customer_options[customer_choice - 1][0]

        customers.delete_customer(conn, customer_id)
        conn.close()

# Add, update, list, search, and delete products
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
@click.option('--id', prompt='Product ID', type=int, help='ID of the product to update')
@click.option('--name', prompt='New product name', help='New name of the product')
@click.option('--price', prompt='New product price', type=float, help='New price of the product')
def update_product(id, name, price):
    """ Update an existing product in the database """
    conn = create_connection()
    if conn:
        products.update_product(conn, id, name, price)
        conn.close()

@cli.command()
def list_products():
    """ List all products """
    conn = create_connection()
    if conn:
        products.list_products(conn)
        conn.close()

@cli.command()
def search_products():
    """ Search and display all products """
    conn = create_connection()
    if conn:
        products.search_products(conn)
        conn.close()

@cli.command()
def delete_product():
    """ Delete a product from the database """
    conn = create_connection()
    if conn:
        product_options = products.get_products(conn)
        if not product_options:
            click.echo("No products found.")
            return

        # Display product options to the user
        click.echo("Select product to delete:")
        for idx, product in enumerate(product_options, start=1):
            click.echo(f"{idx}. ID: {product[0]}, Name: {product[1]}")

        product_choice = click.prompt("Enter product number", type=int)

        if product_choice < 1 or product_choice > len(product_options):
            click.echo("Invalid product number.")
            return

        product_id = product_options[product_choice - 1][0]

        products.delete_product(conn, product_id)
        conn.close()

# Add, update, list, search, and delete suppliers
@cli.command()
@click.option('--name', prompt='Enter the name of a supplier', help='Name of the supplier')
@click.option('--phone', prompt='Supplier phone number', help='Phone number of the supplier', callback=validate_phone)
def add_supplier(name, phone):
    """ Add a new supplier to the database """
    conn = create_connection()
    if conn:
        suppliers.add_supplier(conn, name, phone)
        conn.close()

@cli.command()
@click.option('--id', prompt='Supplier ID', type=int, help='ID of the supplier to update')
@click.option('--name', prompt='New supplier name', help='New name of the supplier')
@click.option('--phone', prompt='New supplier phone', help='New phone number of the supplier', callback=validate_phone)
def update_supplier(id, name, phone):
    """ Update an existing supplier in the database """
    conn = create_connection()
    if conn:
        suppliers.update_supplier(conn, id, name, phone)
        conn.close()

@cli.command()
def list_suppliers():
    """ List all suppliers """
    conn = create_connection()
    if conn:
        suppliers.list_suppliers(conn)
        conn.close()

@cli.command()
def search_suppliers():
    """ Search and display all suppliers """
    conn = create_connection()
    if conn:
        suppliers.search_suppliers(conn)
        conn.close()

@cli.command()
def delete_supplier():
    """ Delete a supplier from the database """
    conn = create_connection()
    if conn:
        supplier_options = suppliers.get_suppliers(conn)
        if not supplier_options:
            click.echo("No suppliers found.")
            return

        # Display supplier options to the user
        click.echo("Select supplier to delete:")
        for idx, supplier in enumerate(supplier_options, start=1):
            click.echo(f"{idx}. ID: {supplier[0]}, Name: {supplier[1]}")

        supplier_choice = click.prompt("Enter supplier number", type=int)

        if supplier_choice < 1 or supplier_choice > len(supplier_options):
            click.echo("Invalid supplier number.")
            return

        supplier_id = supplier_options[supplier_choice - 1][0]

        suppliers.delete_supplier(conn, supplier_id)
        conn.close()

# Add, update, list, search, and delete orders
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
@click.option('--id', prompt='Order ID', type=int, help='ID of the order to update')
@click.option('--order_date', prompt='New order date', help='New date of the order (YYYY-MM-DD)')
def update_order(id, order_date):
    """ Update an existing order in the database """
    conn = create_connection()
    if conn:
        orders.update_order(conn, id, order_date)
        conn.close()

@cli.command()
def list_orders():
    """ List all orders """
    conn = create_connection()
    if conn:
        orders.list_orders(conn)
        conn.close()

@cli.command()
def search_orders():
    """ Search and display all orders """
    conn = create_connection()
    if conn:
        orders.search_orders(conn)
        conn.close()

@cli.command()
def delete_order():
    """ Delete an order from the database """
    conn = create_connection()
    if conn:
        order_options = orders.get_orders(conn)
        if not order_options:
            click.echo("No orders found.")
            return

        # Display order options to the user
        click.echo("Select order to delete:")
        for idx, order in enumerate(order_options, start=1):
            click.echo(f"{idx}. ID: {order[0]}, Order Date: {order[4]}")

        order_choice = click.prompt("Enter order number", type=int)

        if order_choice < 1 or order_choice > len(order_options):
            click.echo("Invalid order number.")
            return

        order_id = order_options[order_choice - 1][0]

        orders.delete_order(conn, order_id)
        conn.close()

if __name__ == '__main__':
    cli()
