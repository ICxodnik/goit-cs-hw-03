from repository import *
from db import execute_query

if __name__ == "__main__":
    # Підключення до бази даних і створення таблиць
    try:
        print(f"Створення таблиці 'users'...")
        execute_query(sql_create_users_table)

        print(f"Створення таблиці 'statuses'...")
        execute_query(sql_create_statuses_table)

        print(f"Створення таблиці 'tasks'...")
        execute_query(sql_create_tasks_table)

        print(f"Всі таблиці створені успішно!")
    except:
        print(f"Не вдалося створити всі таблиці.")
