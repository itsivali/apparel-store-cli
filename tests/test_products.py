import pytest
from database import create_connection, initialize_database 
import products

@pytest.fixture(scope="module")
def connection():
    conn = create_connection()
    initialize_database(conn)
    yield conn
    conn.close()

def test_add_product(connection):
    products.add_product(connection, "Test Product", 99.99, 1)
    # Assert based on your expected behavior
    assert len(products.get_products(connection)) == 1

def test_update_product(connection):
    products.add_product(connection, "Test Product", 99.99, 1)
    product_id = products.get_products(connection)[0][0]
    products.update_product(connection, product_id, "Updated Product", 49.99)
    # Assert based on your expected behavior
    updated_product = products.get_products(connection)[0]
    assert updated_product[1] == "Updated Product"
    assert updated_product[2] == 49.99

def test_list_products(connection):
    products.add_product(connection, "Test Product", 99.99, 1)
    products_list = products.get_products(connection)
    # Assert based on your expected behavior
    assert len(products_list) > 0
   

