from repository import *
from db import execute_query

def run_queries():
    # 
    try:
        execute_query(get_task_by_user, (1,))
        execute_query(get_task_by_status, ('new',))
        execute_query(update_status, ('in progress', 1))
        execute_query(get_users_without_task)
        execute_query(add_task, ('New Task', 'Description', 1, 2))
        execute_query(get_unfinished_tasks)
        execute_query(delete_task, (1,))
        execute_query(get_user_by_email, ("%n@example.net",))
        execute_query(update_user_name, ('Updated Name', 1))
        
        execute_query(get_amount_by_status)
        execute_query(get_tasks_without_desc)
        execute_query(get_users_with_prog_tasks)
        execute_query(get_amount_of_tasks)

        print(f"Всі запроси успішно протестовані!")
    except:
        print(f"Не вдалося протестувати всі запроси.")


if __name__ == "__main__":
    run_queries()
