import sys
import pandas as pd
from utils import drop_missing_columns, impute_missing_values, save_cleaned_data
from components.db_connections import DBConnection
import logging
from exception import CustomException

# Get logger
logger = logging.getLogger(__name__)


def clean_data(table_name):
    """
    Clean the data by dropping columns with more than 70% missing values and imputing missing values.
    Save cleaned data to artifacts folder.
    """
    try:
        # Instantiate DBConnection class
        db_connection = DBConnection()

        # Read the specified table from the database into a Pandas DataFrame
        df = db_connection.read_table_to_dataframe(table_name)
        logger.info("Data loaded successfully from table: %s", table_name)

        # Drop columns with more than 70% missing values
        df = drop_missing_columns(df)

        # Impute missing values
        df = impute_missing_values(df)

        # Save cleaned data
        save_cleaned_data(df, 'cleaned_data.csv')
        logger.info("Data cleaned and saved successfully")

    except CustomException as e:
        # Handle custom exceptions
        logger.error("Custom Exception occurred: %s", e)
        raise
    except Exception as e:
        # Handle other exceptions
        error_message = f"Error cleaning data: {str(e)}"
        logger.error(error_message)
        raise CustomException(error_message, error_detail=sys.exc_info())


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python clean.py <table_name>")
        sys.exit(1)

    # Get the table name from command-line argument
    table_name = sys.argv[1]

    # Call the clean_data function with the provided table name
    clean_data(table_name)





