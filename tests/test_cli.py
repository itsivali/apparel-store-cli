import pytest
from click.testing import CliRunner
from database import create_connection, initialize_database 
import cli

@pytest.fixture(scope="module")
def connection():
    conn = create_connection()
    initialize_database(conn)
    yield conn
    conn.close()

@pytest.fixture
def runner():
    return CliRunner()

### Customers Tests ###

def test_add_customer(runner, connection):
    result = runner.invoke(cli.cli, ['add-customer'], input='Test Customer\nexample@test.com\n1234567890\n')
    assert result.exit_code == 0
    assert "Customer Test Customer added successfully." in result.output

def test_update_customer(runner, connection):
    # Assuming you have a test customer ID to update
    result = runner.invoke(cli.cli, ['update-customer'], input='1\nUpdated Customer\nupdated@example.com\n9876543210\n')
    assert result.exit_code == 0
    assert "Customer with ID 1 updated successfully." in result.output

def test_list_customers(runner, connection):
    result = runner.invoke(cli.cli, ['list-customers'])
    assert result.exit_code == 0
    assert "Test Customer" in result.output  # Adjust based on your expected output

def test_search_customers(runner, connection):
    result = runner.invoke(cli.cli, ['search-customers'])
    assert result.exit_code == 0
    assert "Test Customer" in result.output  # Adjust based on your expected output

def test_delete_customer(runner, connection):
    # Assuming you have a test customer ID to delete
    result = runner.invoke(cli.cli, ['delete-customer'], input='1\n')
    assert result.exit_code == 0
    assert "Customer with ID 1 deleted successfully." in result.output

### Products Tests ###

def test_add_product(runner, connection):
    result = runner.invoke(cli.cli, ['add-product'], input='Test Product\n99.99\n1\n')
    assert result.exit_code == 0
    assert "Product Test Product added successfully." in result.output

def test_update_product(runner, connection):
    # Assuming you have a test product ID to update
    result = runner.invoke(cli.cli, ['update-product'], input='1\nUpdated Product\n49.99\n')
    assert result.exit_code == 0
    assert "Product with ID 1 updated successfully." in result.output

def test_list_products(runner, connection):
    result = runner.invoke(cli.cli, ['list-products'])
    assert result.exit_code == 0
    assert "Test Product" in result.output  # Adjust based on your expected output

def test_search_products(runner, connection):
    result = runner.invoke(cli.cli, ['search-products'])
    assert result.exit_code == 0
    assert "Test Product" in result.output  # Adjust based on your expected output

def test_delete_product(runner, connection):
    # Assuming you have a test product ID to delete
    result = runner.invoke(cli.cli, ['delete-product'], input='1\n')
    assert result.exit_code == 0
    assert "Product with ID 1 deleted successfully." in result.output

### Suppliers Tests ###

def test_add_supplier(runner, connection):
    result = runner.invoke(cli.cli, ['add-supplier'], input='Test Supplier\n1234567890\n')
    assert result.exit_code == 0
    assert "Supplier Test Supplier added successfully." in result.output

def test_update_supplier(runner, connection):
    # Assuming you have a test supplier ID to update
    result = runner.invoke(cli.cli, ['update-supplier'], input='1\nUpdated Supplier\n9876543210\n')
    assert result.exit_code == 0
    assert "Supplier with ID 1 updated successfully." in result.output

def test_list_suppliers(runner, connection):
    result = runner.invoke(cli.cli, ['list-suppliers'])
    assert result.exit_code == 0
    assert "Test Supplier" in result.output  # Adjust based on your expected output

def test_search_suppliers(runner, connection):
    result = runner.invoke(cli.cli, ['search-suppliers'])
    assert result.exit_code == 0
    assert "Test Supplier" in result.output  # Adjust based on your expected output

def test_delete_supplier(runner, connection):
    # Assuming you have a test supplier ID to delete
    result = runner.invoke(cli.cli, ['delete-supplier'], input='1\n')
    assert result.exit_code == 0
    assert "Supplier with ID 1 deleted successfully." in result.output

### Orders Tests ###

def test_add_order(runner, connection):
    # Assuming you have test product and customer IDs to use
    result = runner.invoke(cli.cli, ['add-order'], input='1\n1\n2024-06-16\n')
    assert result.exit_code == 0
    assert "Order added successfully." in result.output

def test_update_order(runner, connection):
    # Assuming you have a test order ID to update
    result = runner.invoke(cli.cli, ['update-order'], input='1\n2024-06-17\n')
    assert result.exit_code == 0
    assert "Order with ID 1 updated successfully." in result.output

def test_list_orders(runner, connection):
    result = runner.invoke(cli.cli, ['list-orders'])
    assert result.exit_code == 0
    assert "2024-06-16" in result.output  # Adjust based on your expected output

def test_search_orders(runner, connection):
    result = runner.invoke(cli.cli, ['search-orders'])
    assert result.exit_code == 0
    assert "2024-06-16" in result.output  # Adjust based on your expected output

def test_delete_order(runner, connection):
    # Assuming you have a test order ID to delete
    result = runner.invoke(cli.cli, ['delete-order'], input='1\n')
    assert result.exit_code == 0
    assert "Order with ID 1 deleted successfully." in result.output


