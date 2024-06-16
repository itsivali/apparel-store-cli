import pytest
from database import create_connection, initialize_database 
import customers

@pytest.fixture(scope="module")
def connection():
    conn = create_connection()
    initialize_database(conn)
    yield conn
    conn.close()

def test_add_customer(connection):
    customers.add_customer(connection, "Test Customer", "example@test.com", "1234567890")
    # Assert based on your expected behavior
    assert len(customers.get_customers(connection)) == 1

def test_update_customer(connection):
    customers.add_customer(connection, "Test Customer", "example@test.com", "1234567890")
    customer_id = customers.get_customers(connection)[0][0]
    customers.update_customer(connection, customer_id, "Updated Customer", "updated@example.com", "9876543210")
    # Assert based on your expected behavior
    updated_customer = customers.get_customers(connection)[0]
    assert updated_customer[1] == "Updated Customer"
    assert updated_customer[2] == "updated@example.com"
    assert updated_customer[3] == "9876543210"

def test_list_customers(connection):
    customers.add_customer(connection, "Test Customer", "example@test.com", "1234567890")
    customers_list = customers.get_customers(connection)
    # Assert based on your expected behavior
    assert len(customers_list) > 0
    assert customers_list[0][1] == "Test Customer"

def test_search_customers(connection):
    customers.add_customer(connection, "Test Customer", "example@test.com", "1234567890")
    found_customers = customers.search_customers(connection)
    # Assert based on your expected behavior
    assert len(found_customers) > 0
    assert found_customers[0][1] == "Test Customer"

def test_delete_customer(connection):
    customers.add_customer(connection, "Test Customer", "example@test.com", "1234567890")
    customer_id = customers.get_customers(connection)[0][0]
    customers.delete_customer(connection, customer_id)
    # Assert based on your expected behavior
    assert len(customers.get_customers(connection)) == 0


