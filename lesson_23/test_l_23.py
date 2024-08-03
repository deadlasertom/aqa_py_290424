from homework_23 import homework_db
import pytest

@pytest.fixture
def db():
    db_instance = homework_db(':memory:')
    yield db_instance
    db_instance.connection.close()

@pytest.fixture
def test_data():
    return {
        "table_name": "test_table",
        "fields": {'pirate_name': 'TEXT', 'ship_name': 'TEXT', 'gold_chests': 'INTEGER'},
        "columns": ['pirate_name', 'ship_name', 'gold_chests'],
        "data_1": ["John Mamon", "Green Lantern", 23],
        "data_1_result": [(1, 'John Mamon', 'Green Lantern', 23)],
        "update_fields": {'gold_chests': 100},  
        "update_conditions": {'pirate_name': 'John Mamon'},
        "data_2_result": [(1, 'John Mamon', 'Green Lantern', 100)]
    }



def test_create_table(db, test_data):
    db.create_table(test_data['table_name'], test_data['fields'])
    result = db.select_all(test_data['table_name'])
    assert result == [], "Table creation failed or table is not empty."



def test_insert(db, test_data):
    db.create_table(test_data['table_name'], test_data['fields'])
    db.insert(test_data['table_name'], test_data['columns'], test_data['data_1'])
    result = db.select_all(test_data['table_name'])
    
    assert result == test_data["data_1_result"], "Insert failed or data is not correct."

def test_update(db, test_data):
    db.create_table(test_data['table_name'], test_data['fields'])
    db.insert(test_data['table_name'], test_data['columns'], test_data['data_1'])
    db.update(test_data['table_name'], test_data['update_fields'], test_data['update_conditions'])
    result = db.select_all(test_data['table_name'])
    assert result == test_data["data_2_result"], "Insert failed or data is not correct."    
    

def test_delete (db, test_data):
    db.create_table(test_data['table_name'], test_data['fields'])
    db.insert(test_data['table_name'], test_data['columns'], test_data['data_1'])
    db.delete(test_data['table_name'], test_data['update_conditions'])
    result = db.select_all(test_data['table_name'])
    assert result == [], "Table is not empty."




