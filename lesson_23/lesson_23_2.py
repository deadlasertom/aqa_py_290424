
import sqlite3


class DB_users():

    def __init__(self, filename:str) -> None:
        self.conn_to_db(filename)
        # self.create_table("users")

    def conn_to_db(self, filename:str = ':memory:'):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
    
    def create_table(self, name:str, field_dict:dict):
        fields = ""
        fields = [f"{field} {type_}" for field, type_ in field_dict.items()]
            #fields = fields + ", " + f"{field} {type_}" 
        fields = ", ".join(fields)
        sql = f'''
                CREATE TABLE IF NOT EXISTS {name} (
                id INTEGER PRIMARY KEY,
                {fields}
                )
               '''
        self.cursor.execute(sql)
        self.connection.commit()


    def select(self, colum, table, **kwargs):
        select_string = f'SELECT {colum} FROM {table} WHERE '
        where_args = ""
        for key, value in kwargs.items():
            where_args += f"{key} = '{value}'"
        self.cursor.execute(select_string + where_args)
        return self.cursor.fetchall()


    def insert(self, table, fields_list, data_list):
        fields = ", ".join (fields_list)
        values = ", ".join(f'"{d}"' for d in data_list)
        sql = (f'''
                INSERT INTO {table} ({fields}) VALUES ({values}) ''')
        self.cursor.execute(sql)
        # Збереження змін у базі даних
        self.connection.commit()


if __name__ == "__main__":
    my_db = DB_users("example.db")
    field_dict = {"username": "TEXT",
                  "last_name": "TEXT",
                  "age": "TEXT",
                  "hobbies": "TEXT"}
    my_db.create_table("employe", field_dict)
    # my_db.insert("employe", ["username", "last_name", "age", "hobbies"], 
    #              ["Derek", "Filer", 23, "sport"])
    print(my_db.select("*", "employe", last_name="Joy"))
    print(my_db.select("*", "employe", last_name="Filer"))
