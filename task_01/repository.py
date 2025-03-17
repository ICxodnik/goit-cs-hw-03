#SQL-запити 
#Отримати всі завдання певного користувача
get_task_by_user = """
SELECT * FROM tasks
WHERE user_id = %s;
"""

#Вибрати завдання за певним статусом
get_task_by_status = """
SELECT * FROM tasks 
WHERE status_id = (SELECT id FROM status WHERE name = %s);
"""

#Оновити статус конкретного завдання
update_status = """
UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress') 
WHERE id = %s;
"""

#Отримати список користувачів, які не мають жодного завдання
get_users_without_task = """
SELECT * FROM users 
WHERE id NOT IN (SELECT user_id FROM tasks);
"""

#Додати нове завдання для конкретного користувача
add_task = """
INSERT INTO tasks (title, description, status_id, user_id) 
VALUES (%s, %s, %s, %s);
"""

#Отримати всі завдання, які ще не завершено
get_unfinished_tasks = """
SELECT * FROM tasks 
WHERE status_id != (SELECT id FROM status WHERE name = 'completed');
"""

#Видалити конкретне завдання
delete_task = """
DELETE FROM tasks 
WHERE id = %s;
"""

#Знайти користувачів з певною електронною поштою
get_user_by_email = """
SELECT * FROM users 
WHERE email LIKE %s;
"""

#Оновити ім'я користувача
update_user_name = """
UPDATE users 
SET fullname = %s 
WHERE id = %s;
"""

#Отримати кількість завдань для кожного статусу
get_amount_by_status = """
SELECT status_id, COUNT(*) 
FROM tasks 
GROUP BY status_id;
"""

#Отримати завдання, що не мають опису
get_tasks_without_desc = """
SELECT * FROM tasks 
WHERE description IS NULL;
"""

#Вибрати користувачів та їхні завдання у статусі 'in progress'
get_users_with_prog_tasks = """
SELECT u.fullname, t.title 
FROM users u 
INNER JOIN tasks t ON u.id = t.user_id 
WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');
"""

#Отримати користувачів та кількість їхніх завдань
get_amount_of_tasks = """
SELECT u.fullname, COUNT(t.id) 
FROM users u 
LEFT JOIN tasks t ON u.id = t.user_id 
GROUP BY u.id;
"""
    
#SQL-запити для створення таблиць
sql_create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);
"""
sql_create_statuses_table = """
CREATE TABLE IF NOT EXISTS statuses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);
"""
sql_create_tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER REFERENCES statuses(id),
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
"""

#SQL-запити для заповнення даними
sql_users = """
INSERT INTO users (fullname, email) VALUES (%s, %s)
ON CONFLICT (email) DO NOTHING;
"""

sql_statuses = """
INSERT INTO statuses (name) VALUES (%s)
ON CONFLICT (name) DO NOTHING;
"""

sql_tasks = """
INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);
"""