import os
import sys
import logging
from typing import Optional, Any
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
from logger import logging  
from exception import CustomException
from sqlalchemy.sql import text
  

class DBConnection:
    """
    A class to handle database connections and operations.
    """

    def __init__(self) -> None:
        """
        Initializes the DBConnection object.
        """
        self._load_env_variables()
        self._setup_logging()

    def _setup_logging(self) -> None:
        """
        Sets up logging configuration.
        """
        self.logger = logging.getLogger(__name__)

    def _load_env_variables(self) -> None:
        """
        Loads environment variables from the specified .env file.
        """
        try:
            load_dotenv()
            self.db_name = os.getenv('DB_NAME')
            self.db_user = os.getenv('DB_USER')
            self.db_password = os.getenv('DB_PASSWORD')
            self.db_host = os.getenv('DB_HOST')
            self.port = os.getenv('PORT')
        except Exception as e:
            error_message = f"Error loading environment variables: {str(e)}"
            self.logger.error(error_message)
            raise CustomException(error_message, error_detail=sys.exc_info())

    def _get_db_url(self) -> str:
        """
        Constructs and returns the database URL.

        Returns:
        - str: The database URL.
        """
        return f'postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.port}/{self.db_name}'

    def read_table_to_dataframe(self, table_name: str) -> pd.DataFrame:
        """
        Reads a table from the database into a Pandas DataFrame.

        Args:
        - table_name (str): The name of the table to read.

        Returns:
        - pandas.DataFrame: The DataFrame containing the table data.
        """
        try:
            db_url = self._get_db_url()
            engine = create_engine(db_url)
            query = f'SELECT * FROM {table_name}'
            df = pd.read_sql(query, con=engine)
            return df
        except Exception as e:
            error_message = f"Error reading table '{table_name}': {str(e)}"
            self.logger.error(error_message)
            raise CustomException(error_message, error_detail=sys.exc_info())


    def write_dataframe_to_table(self, df: pd.DataFrame, table_name: str) -> None:
        """
        Writes a Pandas DataFrame to a new table in the database.

        Args:
        - df (pandas.DataFrame): The DataFrame to write.
        - table_name (str): The name of the new table.
        """
        try:
            db_url = self._get_db_url()
            engine = create_engine(db_url)
            df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        except Exception as e:
            error_message = f"Error writing DataFrame to table '{table_name}': {str(e)}"
            self.logger.error(error_message)
            raise CustomException(error_message, error_detail=sys.exc_info())

    def append_dataframe_to_table(self, df: pd.DataFrame, table_name: str) -> None:
        """
        Appends a Pandas DataFrame to an existing table in the database.

        Args:
        - df (pandas.DataFrame): The DataFrame to append.
        - table_name (str): The name of the existing table.
        """
        try:
            db_url = self._get_db_url()
            engine = create_engine(db_url)
            df.to_sql(table_name, con=engine, if_exists='append', index=False)
        except Exception as e:
            error_message = f"Error appending DataFrame to table '{table_name}': {str(e)}"
            self.logger.error(error_message)
            raise CustomException(error_message, error_detail=sys.exc_info())

    def delete_table(self) -> None:
        """
        Deletes a specified table from the database.

        Prompts the user to input the table name.
        """
        try:
            table_name = input("Enter the name of the table to delete: ")
            db_url = self._get_db_url()
            engine = create_engine(db_url)
            with engine.connect() as conn:
                conn.execute(text('DROP TABLE IF EXISTS :table_name'), {'table_name': table_name})
                self.logger.info(f"Table '{table_name}' deleted successfully.")
        except Exception as e:
            self.logger.error(f"Error deleting table '{table_name}': {str(e)}")
            raise



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python db_connections.py <table_name>")
        sys.exit(1)

    table_name = sys.argv[1]

    # Instantiate the DBConnection class
    db_connection = DBConnection()

    try:
        # Read the specified table from the database into a Pandas DataFrame
        table_df = db_connection.read_table_to_dataframe(table_name)

        # Print the DataFrame
        print("Table Data:")
        print(table_df)

        # Write the DataFrame to a new table in the database
        db_connection.write_dataframe_to_table(table_df, "new_table_name")

        # Append the DataFrame to an existing table in the database
        db_connection.append_dataframe_to_table(table_df, "existing_table_name")


    except CustomException as e:
        # Handle any custom exceptions raised during the operations
        print("Custom Exception occurred:", e)

