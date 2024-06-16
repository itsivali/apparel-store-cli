 import pytest
from database import create_connection, initialize_database 
import orders

@pytest.fixture(scope="module")
def connection():
    conn = create_connection()
    initialize_database(conn)
    yield conn
    conn.close()

def test_add_order(connection):
    # Assuming you have test product and customer IDs to use
    orders.add_order(connection, 1, 1, 1, "2024-06-16")
    # Assert based on your expected behavior
    assert len(orders.get_orders(connection)) == 1

def test_update_order(connection):
    # Assuming you have a test order ID to update
    orders.add_order(connection, 1, 1, 1, "2024-06-16")
    order_id = orders.get_orders(connection)[0][0]
    orders.update_order(connection, order_id, "2024-06-17")
    # Assert based on your expected behavior
    updated_order = orders.get_orders(connection)[0]
    assert updated_order[4] == "2024-06-17"

def test_list_orders(connection):
    orders.add_order(connection, 1, 1, 1, "2024-06-16")
    orders_list = orders.get_orders(connection)
    # Assert based on your expected behavior
    assert len(orders_list) > 0
    assert orders_list[0][4] == "2024-06-16"

def test_search_orders(connection):
    orders.add_order(connection, 1, 1, 1, "2024-06-16")
    found_orders = orders.search_orders(connection)
    # Assert based on your expected behavior
    assert len(found_orders) > 0
    assert found_orders[0][4] == "2024-06-16"

def test_delete_order(connection):
    orders.add_order(connection, 1, 1, 1, "2024-06-16")
    order_id = orders.get_orders(connection)[0][0]
    orders.delete_order(connection, order_id)
    # Assert based on your expected behavior
    assert len(orders.get_orders(connection)) == 0


