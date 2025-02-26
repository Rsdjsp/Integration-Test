"""
Main script to process candidate, job, and education data, store it in a PostgreSQL database,
and identify unemployed candidates and their locations.
"""

from scripts.data_loader import load_data
from scripts.db_manager import create_tables, insert_data, get_unemployed_candidates
from scripts.notifier import notify

def main():
    """
    execution script
    """
    df_candidates, df_jobs, df_education = load_data()


    conn, cursor = create_tables()
    insert_data(conn,cursor, df_candidates, df_jobs, df_education)
    unemployed_candidates = get_unemployed_candidates(cursor)


    notify(unemployed_candidates)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()