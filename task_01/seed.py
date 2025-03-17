import faker
from random import randint
from config import NUMBER_USERS, NUMBER_TASKS, STATUSES
from repository import sql_users, sql_tasks, sql_statuses
from db import execute_many


def generate_fake_data(NUMBER_USERS, NUMBER_TASKS):
    """Генерація фейкових даних для заповнення таблиць."""
    fake = faker.Faker()
    fake_users = [
        {"fullname": fake.name(), "email": fake.email()} for _ in range(NUMBER_USERS)
    ]
    fake_tasks = [
        {
            "title": fake.sentence(),
            "description": fake.text(),
            "status_id": randint(1, len(STATUSES)),
            "user_id": randint(1, NUMBER_USERS),
        }
        for _ in range(NUMBER_TASKS)
    ]

    return fake_users, fake_tasks


def prepare_data(users, statuses, tasks):
    """Підготовка даних до вставки в таблиці."""
    for_users = [(user["fullname"], user["email"]) for user in users]
    for_statuses = [(status,) for status in statuses]
    for_tasks = [
        (task["title"], task["description"], task["status_id"], task["user_id"])
        for task in tasks
    ]
    return for_users, for_statuses, for_tasks


def insert_data_to_db(users, statuses, tasks):
        try:
            # Вставка користувачів
            execute_many(sql_users, users)
            print(f"Користувачі успішно додані.")

            # Вставка статусів
            execute_many(sql_statuses, statuses)
            print(f"Статуси успішно додані.")

            # Вставка завдань
            execute_many(sql_tasks, tasks)
            print(f"Завдання успішно додані.")
        except Exception as e:
            print(f"Помилка вставки даних: {e}")


if __name__ == "__main__":
    print(f"Генерація даних...")
    users, tasks = generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
    users, statuses, tasks = prepare_data(users, STATUSES, tasks)

    print(f"Заповнення бази даних...")
    insert_data_to_db(users, statuses, tasks)
    print(f"База даних успішно заповнена!")
