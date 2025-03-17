from repository import *
from db import execute_query


def create_tables():
    # Підключення до бази даних і створення таблиць
    try:
        print(f"Очищення таблиць...")
        execute_query(clear_db)
        
        print(f"Створення таблиці 'users'...")
        execute_query(sql_create_users_table)

        print(f"Створення таблиці 'status'...")
        execute_query(sql_create_status_table)

        print(f"Створення таблиці 'tasks'...")
        execute_query(sql_create_tasks_table)

        print(f"Всі таблиці створені успішно!")
    except:
        print(f"Не вдалося створити всі таблиці.")

if __name__ == "__main__":
    create_tables()
