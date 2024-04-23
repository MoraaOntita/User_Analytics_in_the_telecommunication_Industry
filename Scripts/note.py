import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
from sqlalchemy import create_engine
import sys
import os

def load_data_from_database(env_file_path):
    # Load environment variables from the specified .env file
    load_dotenv(env_file_path)

    # Access environment variables
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    port = os.getenv('PORT')
    table_name = os.getenv('TABLE_NAME')

    # Construct the database URL
    db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{port}/{db_name}'

    # Create the SQLAlchemy engine
    engine = create_engine(db_url)

    # Define your SQL query
    sql_query = f'SELECT * FROM {table_name}'

    # Load data into a Pandas DataFrame
    df = pd.read_sql(sql_query, con=engine)

    return df

def handle_missing_values(df):
    # Separate numerical and categorical columns
    numerical_cols = df.select_dtypes(include=['float64', 'int64'])
    categorical_cols = df.select_dtypes(include=['object'])

    # Handle missing values in numerical columns by filling with mean
    numerical_cols_filled = numerical_cols.fillna(numerical_cols.mean())

    # Concatenate numerical and categorical columns
    combined_df = pd.concat([numerical_cols_filled, categorical_cols], axis=1)

    return combined_df