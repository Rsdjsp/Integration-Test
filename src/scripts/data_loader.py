"""
This module is used to load the data from the csv files.
"""
import os

import pandas as pd


def load_data():
    """ Load data from the csv files"""
    base_path = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_path, 'data')

    candidates_file = os.path.join(data_path, 'Copy of CANDIDATES.csv')
    jobs_file = os.path.join(data_path, 'Copy of JOBS.csv')
    education_file = os.path.join(data_path, 'Copy of EDUCATION.csv')

    df_candidates = pd.read_csv(candidates_file)
    df_jobs = pd.read_csv(jobs_file)
    df_education = pd.read_csv(education_file)

    return df_candidates, df_jobs, df_education