from contextlib import contextmanager
import psycopg2
from psycopg2 import OperationalError
from config import DB_CONFIG
from repository import *

@contextmanager
def create_connection():
    # print(f"Створення з'єднання з PostgreSQL.")
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        yield conn
        conn.commit()
    except OperationalError as e:
        print(f"Помилка підключення: {e}")
        if conn:
            conn.rollback()
    except Exception as e:
        print(f"Невідома помилка: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()


def execute_query(sql: str, params: tuple = ()) -> None:
    try:
        with create_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                #print(f"Выполненный SQL запрос: {cur.query.decode()}")
                # Отримуємо кількість змінених рядків
                affected_rows = cur.rowcount
                # Якщо це SELECT запит, можемо отримати результати
                if sql.strip().upper().startswith('SELECT'):
                    results = cur.fetchall()
                    print(f"Запит виконано успішно. Отримано {len(results)} записів:")
                    #print(results)
                    return results
                elif affected_rows >= 0:
                    print(f"Запит виконано успішно. Змінено {affected_rows} записів.")
    except psycopg2.Error as e:
        print(f"Помилка виконання запиту: {e}")
        raise


def execute_many(sql: str, params_list: list) -> None:
    try:
        with create_connection() as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, params_list)
                print(f"Масовий запит виконано успішно. Змінено {cur.rowcount} записів.")
    except psycopg2.Error as e:
        print(f"Помилка виконання масового запиту: {e}")
        raise