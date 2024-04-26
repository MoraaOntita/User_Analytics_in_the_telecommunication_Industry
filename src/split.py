# split.py

from src.components.db_connections import DBConnection
from typing import Tuple
from logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
import sys

logger = logging.getLogger(__name__)

class DataSplitter:
    def __init__(self, db_connection: DBConnection) -> None:
        self.db_connection = db_connection

    def load_data(self, table_name: str) -> pd.DataFrame:
        """
        Load data from the database.

        Args:
            table_name (str): The name of the table to load data from.

        Returns:
            pd.DataFrame: The loaded data.
        """
        try:
            data = self.db_connection.read_table_to_dataframe(table_name)
            logger.info(f"Data loaded from table '{table_name}'")
            return data
        except Exception as e:
            error_message = f"Error loading data from table '{table_name}': {str(e)}"
            logger.error(error_message)
            raise CustomException(error_message, error_detail=sys.exc_info())

    def split_data(self, data: pd.DataFrame, target_column: str, test_size: float = 0.2, random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """
        Split data into training and testing datasets.

        Args:
            data (pd.DataFrame): The dataset to split.
            target_column (str): The name of the target variable column.
            test_size (float, optional): The proportion of the dataset to include in the test split. Defaults to 0.2.
            random_state (int, optional): Controls the randomness of the data splitting. Defaults to 42.

        Returns:
            tuple: A tuple containing the training and testing datasets.
        """
        try:
            X = data.drop(columns=[target_column])
            y = data[target_column]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
            logger.info("Data split into training and testing datasets")
            return X_train, X_test, y_train, y_test
        except Exception as e:
            error_message = f"Error splitting data: {str(e)}"
            logger.error(error_message)
            raise CustomException(error_message, error_detail=sys.exc_info())

if __name__ == "__main__":
    db_connection = DBConnection()
    data_splitter = DataSplitter(db_connection)

    try:
        table_name = input("Enter the name of the table: ")  # Prompt user to enter the table name
        data = data_splitter.load_data(table_name)
        target_column = input("Enter the name of the target column: ")  # Prompt user to enter the target column name
        X_train, X_test, y_train, y_test = data_splitter.split_data(data, target_column)

        print("Training data shape:", X_train.shape)
        print("Testing data shape:", X_test.shape)
    except CustomException as e:
        logger.error(f"Custom Exception occurred: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
