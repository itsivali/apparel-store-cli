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
    suppliers_list = suppliers.get_suppliers(connection)
    assert len(suppliers_list) == 1
    assert suppliers_list[0][1] == "Test Supplier"

def test_update_supplier(connection):
    suppliers.add_supplier(connection, "Another Supplier", "0987654321")
    supplier_id = suppliers.get_suppliers(connection)[1][0]
    suppliers.update_supplier(connection, supplier_id, "Updated Supplier", "9876543210")
    updated_supplier = suppliers.get_suppliers(connection)[1]
    assert updated_supplier[1] == "Updated Supplier"
    assert updated_supplier[2] == "9876543210"

def test_list_suppliers(connection):
    suppliers_list = suppliers.get_suppliers(connection)
    assert len(suppliers_list) > 0

def test_search_suppliers(connection):
    found_suppliers = suppliers.get_suppliers(connection)
    assert len(found_suppliers) > 0

def test_delete_supplier(connection):
    suppliers.add_supplier(connection, "Supplier to Delete", "1112223333")
    supplier_id = suppliers.get_suppliers(connection)[-1][0]
    suppliers.delete_supplier(connection, supplier_id)
    suppliers_list = suppliers.get_suppliers(connection)
    assert all(supplier[0] != supplier_id for supplier in suppliers_list)
