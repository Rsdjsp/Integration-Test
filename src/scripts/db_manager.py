"""
This module contains functions to create tables in the PostgreSQL database and insert data into them.
"""
import os
import psycopg2
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def create_tables():
    """
    Create the necessary tables in the PostgreSQL database if they do not exist.
    """
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidates (
        id SERIAL PRIMARY KEY,
        title TEXT,
        location TEXT,
        hire_flag BOOLEAN
    );

    CREATE TABLE IF NOT EXISTS jobs (
        id SERIAL PRIMARY KEY,
        ocupation TEXT,
        dateRange TEXT,
        skills TEXT,
        current_job BOOLEAN,
        occupation_title TEXT,
        start_date TIMESTAMP,
        end_date TIMESTAMP,
        candidate_id INT REFERENCES candidates(id)
    );

    CREATE TABLE IF NOT EXISTS education (
        education_id SERIAL PRIMARY KEY,
        title TEXT,
        description TEXT,
        dateRange TEXT,
        candidate_id INT REFERENCES candidates(id)
    );
    """)
    conn.commit()
    return conn, cursor

def insert_data(conn, cursor, df_candidates, df_jobs, df_education):
    """
    Insert data into the PostgreSQL database tables.
    """

    candidate_id_map = {}

    for _, row in df_candidates.iterrows():
        hire_flag = bool(row['hire_flag'])
        cursor.execute(
            "INSERT INTO candidates (title, location, hire_flag) VALUES (%s, %s, %s) RETURNING id",
            (row['title'], row['location'], hire_flag)
        )
        candidate_id = cursor.fetchone()[0]
        candidate_id_map[row['id']] = candidate_id


    df_jobs = df_jobs[df_jobs['candidate_id'].isin(candidate_id_map.keys())]
    df_education = df_education[df_education['candidate_id'].isin(candidate_id_map.keys())]

    for _, row in df_jobs.iterrows():
        start_date = row['start_date'] if not pd.isna(row['start_date']) else None
        end_date = row['end_date'] if not pd.isna(row['end_date']) else None
        new_candidate_id = candidate_id_map.get(row['candidate_id'])

        if new_candidate_id:
            cursor.execute(
                "INSERT INTO jobs (ocupation, dateRange, skills, current_job, occupation_title, start_date, end_date, candidate_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (row['ocupation'], row['dateRange'], row['skills'], row['current_job'], row['occupation_title'], start_date, end_date, new_candidate_id)
            )

    for _, row in df_education.iterrows():
        new_candidate_id = candidate_id_map.get(row['candidate_id'])

        if new_candidate_id:
            cursor.execute(
                "INSERT INTO education (title, description, dateRange, candidate_id) VALUES (%s, %s, %s, %s)",
                (row['title'], row['description'], row['dateRange'], new_candidate_id)
            )

    conn.commit()


def get_unemployed_candidates(cursor):
    """
    Retrieve the list of unemployed candidates from the PostgreSQL database.
    """
    cursor.execute("""
        SELECT c.title, c.location FROM candidates c
        LEFT JOIN jobs j ON c.id = j.candidate_id
        WHERE j.candidate_id IS NULL;
    """)
    return cursor.fetchall()