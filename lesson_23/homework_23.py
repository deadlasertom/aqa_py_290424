import sqlite3

class homework_db():

    def __init__(self, file_name: str) -> None:
        self.conn_to_db(file_name)

    def conn_to_db(self, filename:str = ':memory:'):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()

    def create_table(self, name:str, field_dict:dict):
        fields = ""
        fields = [f"{field} {type_}" for field, type_ in field_dict.items()]
        fields = ", " .join(fields)
        sql = f'''
                CREATE TABLE IF NOT EXISTS {name} (
                id INTEGER PRIMARY KEY,
                {fields}
                )
               '''
        self.cursor.execute(sql)
        self.connection.commit()


    def select(self, column, table, **kwargs):
        select_string = f'SELECT {column} FROM {table} WHERE '
        where_args = ""
        for key, value in kwargs.items():
            where_args += f"{key} = '{value}'"
        self.cursor.execute(select_string + where_args)
        return self.cursor.fetchall()
    
    def select_all(self, table):
        select_str = f"SELECT * from {table}"
        self.cursor.execute(select_str)
        return self.cursor.fetchall()
    
    
    def insert(self, table, fields_list, data_list):
        fields = ", ".join (fields_list)
        values = ", ".join("?" for _ in data_list)
        sql = f"INSERT INTO {table} ({fields}) VALUES ({values})"
        self.cursor.execute(sql, data_list)
        self.connection.commit()


    def update(self, table: str, fields: dict, conditions: dict):
        fields_var = ", ".join([f"{key} = ?" for key in fields.keys()])
        condition_var = " AND ".join([f"{key} = ?" for key in conditions.keys()])
        sql = f'UPDATE {table} SET {fields_var} WHERE {condition_var}'
        values = list(fields.values()) + list(conditions.values())
        self.cursor.execute(sql, values)
        self.connection.commit()

    def delete(self, table:str, conditions: dict):
        conditions_var = " AND ".join([f"{key} = ?" for key in conditions.keys()])
        sql = f"DELETE FROM {table} WHERE {conditions_var}"
        self.cursor.execute(sql, list(conditions.values()))  
        self.connection.commit()


    
    
        
