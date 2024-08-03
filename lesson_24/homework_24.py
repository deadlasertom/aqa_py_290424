from pony.orm import *


mysql = dict(
            provider='mysql',
            host="localhost",
            user="root",
            passwd="root",
            db="uakino"
            )

sqlite = dict(
            provider='sqlite',
            filename='uakino.db',
            create_db=True
            )

db = Database()

class Items(db.Entity):
    id = PrimaryKey(int, auto=True)
    title_ua = Optional(str)
    title_or = Optional(str)
    type_src = Optional(str)
    year = Optional(str)
    director = Optional(str)
    poster = Optional(str)
    json = Optional(str)
    imdb = Optional(str)
    links = Set("Links")  

class Seasons(db.Entity):
    id = PrimaryKey(int, auto=True)
    source_id = Optional(str)
    name = Optional(str)
    season = Optional(str)
    title = Optional(str)
    links = Set("Links")  

class Links(db.Entity):
    id = PrimaryKey(int, auto=True)
    source_id = Optional(str)
    series_id = Optional(str)
    quality = Optional(str)
    its_work = Optional(str)
    type_src = Optional(str)
    m3u_links = Optional(str)
    subs = Optional(str)
    item = Optional(Items)   
    season = Optional(Seasons) 


db.bind(sqlite)
db.generate_mapping(create_tables=True)
set_sql_debug(True)

tables = {
    'Items': Items,
    'Seasons': Seasons,
    'Links': Links }

@db_session
def check_in_base(table_name, **kwargs):
     table = tables.get(table_name)
     if not table:
        raise ValueError(f"Table {table_name} not found.")
     item = table.get(**kwargs)
     return item is not None

@db_session 
def add_to_db(table_name, data_to_add):
    table = tables.get(table_name)
    if not table:
        raise ValueError(f"Table {table_name} not found.")
    added_data = table(**data_to_add)
    return added_data

@db_session 
def add_m3u(m3u_data):
    added_m3u = Links(**m3u_data)
    return added_m3u

@db_session 
def add_m3u(link_id, new_m3u_link):
    link = Links.get(id=link_id)
    if link is None:
        raise ValueError(f"Link with ID {link_id} not found.")
    link.m3u_links = new_m3u_link
    return link

@db_session
def save():
    db.commit()




