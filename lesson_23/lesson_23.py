# Structured Query Language = SQL
# СУБД 
import sqlite3

# Підключення до бази даних (створює файл БД, якщо він не існує)
conn = sqlite3.connect('example.db')
# Створення курсора для виконання SQL-запитів
cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                email TEXT
                )
               ''')

# Збереження змін у базі даних
conn.commit()

cursor.execute('''
                INSERT INTO users (username, email) VALUES (?, ?)
                ''', ('JohnDoe', 'john@example.com'))
# Збереження змін у базі даних
conn.commit()

# Вибірка даних
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Оновлення даних
cursor.execute('''
                UPDATE users SET email = ? WHERE id = ?
                ''', ('john.doe@example.com', '1'))
# Збереження змін у базі даних
conn.commit()

# Видалення даних
cursor.execute('DELETE FROM users WHERE email = ?', ('john.doe@example.com',))
# Збереження змін у базі даних
conn.commit()

# Закриття підключення
conn.close()

