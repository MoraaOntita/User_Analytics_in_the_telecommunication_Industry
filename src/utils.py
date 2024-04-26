import os
import sys
import logging
import pandas as pd
from exception import CustomException


def log_exception(func):
    """
    A decorator function to log exceptions.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_message = f"Error in {func.__name__}: {str(e)}"
            logging.error(error_message)
            raise CustomException(error_message, error_detail=sys.exc_info())

    return wrapper


def save_cleaned_file(df: pd.DataFrame, filename: str) -> None:
    """
    Saves the cleaned DataFrame to the artifacts directory.

    Args:
    - df (pd.DataFrame): The cleaned DataFrame.
    - filename (str): The filename for the cleaned file.
    """
    artifacts_dir = os.path.join(os.getcwd(), "artifacts")
    os.makedirs(artifacts_dir, exist_ok=True)
    cleaned_file_path = os.path.join(artifacts_dir, filename)
    df.to_csv(cleaned_file_path, index=False)
    logging.info(f"Cleaned file saved to: {cleaned_file_path}")
    
def load_cleaned_data(file_path: str) -> pd.DataFrame:
    """
    Load cleaned data from a file.

    Args:
        file_path (str): The path to the cleaned data file.

    Returns:
        pd.DataFrame: The cleaned data.
    """
    try:
        cleaned_data = pd.read_csv(file_path)  # Adjust this according to your data format
        return cleaned_data
    except Exception as e:
        raise IOError(f"Error loading cleaned data from {file_path}: {str(e)}")


########## Transformation ######################################

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        pd.DataFrame: The loaded data.
    """
    try:
        data = pd.read_csv(file_path)  # Modify this according to your data format
        return data
    except Exception as e:
        raise IOError(f"Error loading data from {file_path}: {str(e)}")

def save_data(data: pd.DataFrame, file_path: str) -> None:
    """
    Save data to a file.

    Args:
        data (pd.DataFrame): The data to save.
        file_path (str): The path to save the file.
    """
    try:
        data.to_csv(file_path, index=False)  # Modify this according to your data format
    except Exception as e:
        raise IOError(f"Error saving data to {file_path}: {str(e)}")

def save_transformed_data(transformed_data: pd.DataFrame, file_path: str) -> None:
    """
    Save transformed data to a file.

    Args:
        transformed_data (pd.DataFrame): The transformed data to save.
        file_path (str): The path to save the file.
    """
    try:
        save_data(transformed_data, file_path)
    except IOError as e:
        raise IOError(f"Error saving transformed data: {str(e)}")

