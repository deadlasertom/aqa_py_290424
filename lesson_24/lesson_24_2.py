from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("sqlite://", echo=True)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()
# Додавання нового користувача
new_user = User(name='John', age=30)
session.add(new_user)
session.commit()

all_users = session.query(User).all()
print(all_users)
