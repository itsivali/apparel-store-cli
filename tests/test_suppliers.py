import pytest
from database import create_connection, initialize_database 
import suppliers

@pytest.fixture(scope="module")
def connection():
    conn = create_connection()
    initialize_database(conn)
    yield conn
    conn.close()

def test_add_supplier(connection):
    suppliers.add_supplier(connection, "Test Supplier", "1234567890")
    # Assert based on your expected behavior
    assert len(suppliers.get_suppliers(connection)) == 1

def test_update_supplier(connection):
    suppliers.add_supplier(connection, "Test Supplier", "1234567890")
    supplier_id = suppliers.get_suppliers(connection)[0][0]
    suppliers.update_supplier(connection, supplier_id, "Updated Supplier", "9876543210")
    # Assert based on your expected behavior
    updated_supplier = suppliers.get_suppliers(connection)[0]
    assert updated_supplier[1] == "Updated Supplier"
    assert updated_supplier[2] == "9876543210"

def test_list_suppliers(connection):
    suppliers.add_supplier(connection, "Test Supplier", "1234567890")
    suppliers_list = suppliers.get_suppliers(connection)
    # Assert based on your expected behavior
    assert len(suppliers_list) > 0
    assert suppliers_list[0][1] == "Test Supplier"

def test_search_suppliers(connection):
    suppliers.add_supplier(connection, "Test Supplier", "1234567890")
    found_suppliers = suppliers.search_suppliers(connection)
    # Assert based on your expected behavior
    assert len(found_suppliers) > 0
    assert found_suppliers[0][1] == "Test Supplier"

def test_delete_supplier(connection):
    suppliers.add_supplier(connection, "Test Supplier", "1234567890")
    supplier_id = suppliers.get_suppliers(connection)[0][0]
    suppliers.delete_supplier(connection, supplier_id)
    # Assert based on your expected behavior
    assert len(suppliers.get_suppliers(connection)) == 0

 
