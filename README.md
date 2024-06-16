# Apparel Store CLI Application
Welcome to the Apparel Store CLI! This command-line interface allows you to manage customers, products, suppliers, and orders in the Apparel Store database.

## Prerequisites
Python 3.x installed on your system
SQLite3 database management system
Setup
Clone the repository to your local machine:

```bash
git clone https://github.com/itsivali/apparel-store-cli.git
cd apparel-store-cli
```
## Install dependencies:

```bash
pip install -r requirements.txt
```
## Initialize the database with necessary tables:

```bash
python cli.py
```
This command sets up the SQLite database and creates required tables for customers, products, suppliers, and orders.

## Usage
### Commands
The CLI application supports the following commands:

- **add_customer**: Add a new customer to the database.
- **add_product**: Add a new product to the database, including selection of a supplier.
- **add_supplier**: Add a new supplier to the database.
- **add_order**: Add a new order to the database, linking a product and customer.
- **search_customers**: Search and display all customers in the database.
- **search_products**: Search and display all products in the database.
- **search_suppliers**: Search and display all suppliers in the database.
- **search_orders**: Search and display all orders in the database.

### Examples
#### Adding a Customer
To add a new customer, use the add_customer command:

```bash
python cli.py add_customer --name "John Doe" --email "john.doe@example.com" --phone "1234567890"
```
Follow the prompts to enter customer details interactively if options are not provided.

#### Adding a Product
To add a new product, use the add_product command:

```bash
python cli.py add_product --name "T-Shirt" --price 19.99
```
You will be prompted to select a supplier from the available options. If no suppliers are listed, add a new supplier first using the add_supplier command.

#### Adding an Order
To add a new order, use the add_order command:

```bash
python cli.py add_order --order_date "2024-06-16"
```
You will need to select a product and a customer for the order. Ensure products and customers are available in the database.

# Searching for Customers, Products, Suppliers, or Orders
To search and display existing records:

```bash
python cli.py search_customers
python cli.py search_products
python cli.py search_suppliers
python cli.py search_orders
```
**Note:**
- Ensure proper format for email addresses and phone numbers during data entry.
- Take care to select existing products, customers, and suppliers when adding orders.

