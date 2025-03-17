from pymongo import MongoClient
from data import cats

# Підключення до MongoDB
try:
    client = MongoClient(
        f"mongodb://mongo/?retryWrites=true&appName=task_02"
    )
    db = client["cats_db"]
    cats_collection = db["cats"]
    # Створюємо індекс для поля name так як часто по ньому звертаємось
    cats_collection.create_index("name")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    raise


# Функція для додавання котів до бази даних
def add_sample_cats():
    """Функція для додавання згенерованих котів до бази даних"""
    try:
        cats_collection.insert_many(cats)
        print("Коти успішно додані.")
    except Exception as e:
        print(f"Помилка при додаванні котів: {e}")


# Операції CRUD
def get_all_cats():
    """Функція для виведення всіх котів з колекції."""
    try:
        cats = list(cats_collection.find())
        if not cats:
            print("Колекція пуста.")
        else:
            for cat in cats:
                print(str(cat))
    except Exception as e:
        print(f"Помилка при отриманні котів: {e}")


def get_cat_by_name(name):
    """Функція для виведення кота за ім'ям."""
    try:
        cat = cats_collection.find_one({"name": name})
        if cat:
            print(str(cat))
        else:
            print(f"Кота з ім'ям {name} не знайдено.")
    except Exception as e:
        print(f"Помилка при отриманні кота: {e}")


def update_cat_age(name, new_age):
    """Функція для оновлення віку кота."""
    try:
        result = cats_collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print(f"Вік кота {name} оновлено на {new_age}.")
        else:
            print(f"Не знайдено кота з ім'ям {name}.")
    except Exception as e:
        print(f"Помилка при оновленні віку кота: {e}")


def add_feature_to_cat(name, new_feature):
    """Функція для додавання нової характеристики до кота."""
    try:
        result = cats_collection.update_one(
            {"name": name},
            {"$addToSet": {"features": new_feature}},  # Додає елемент, якщо його немає
        )
        if result.modified_count > 0:
            print(f"Характеристика '{new_feature}' додана до кота {name}.")
        else:
            print(f"Не знайдено кота з ім'ям {name}.")
    except Exception as e:
        print(f"Помилка при додаванні характеристики: {e}")


def delete_cat_by_name(name):
    """Функція для видалення кота за ім'ям."""
    try:
        result = cats_collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кота з ім'ям {name} видалено.")
        else:
            print(f"Не знайдено кота з ім'ям {name}.")
    except Exception as e:
        print(f"Помилка при видаленні кота: {e}")


def delete_all_cats():
    """Функція для видалення всіх котів з колекції."""
    try:
        result = cats_collection.delete_many({})
        print(f"{result.deleted_count} котів було видалено.")
    except Exception as e:
        print(f"Помилка при видаленні котів: {e}")


if __name__ == "__main__":
    # Додати котів до бази даних перед тестуванням інших операцій
    add_sample_cats()

    # Тестування операцій
    print("Отримання всіх котів:")
    get_all_cats()

    print("\nОтримання кота за ім'ям 'Барсік':")
    get_cat_by_name("Барсік")

    print("\nОновлення віку кота 'Барсік' на 4 роки:")
    update_cat_age("Барсік", 4)

    print("\nДодавання характеристики до кота 'Барсік':")
    add_feature_to_cat("Барсік", "любить лазити по деревах")

    print("\nОтримання оновлених даних кота 'Барсік':")
    get_cat_by_name("Барсік")

    print("\nВидалення кота 'Барсік':")
    delete_cat_by_name("Барсік")

    print("\nВидалення всіх котів:")
    delete_all_cats()
