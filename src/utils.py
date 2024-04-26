import os
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
