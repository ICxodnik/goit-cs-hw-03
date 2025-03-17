from create_tables import create_tables
from seed import fill_db_with_data
from query_example import run_queries


if __name__ == "__main__":
    create_tables()
    fill_db_with_data()
    run_queries()
