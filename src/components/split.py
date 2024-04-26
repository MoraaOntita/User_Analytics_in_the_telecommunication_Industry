import sys
import pandas as pd
from utils import split_data, save_split_data
from config import ARTIFACTS_DIR
import logging
from exception import CustomException

# Get logger
logger = logging.getLogger(__name__)

def split_data_and_save(transformed_data_file):
    """
    Split the transformed data into train and test sets and save them to the artifacts folder.
    """
    try:
        # Load transformed data
        df = pd.read_csv(transformed_data_file)
        logger.info("Transformed data loaded successfully from %s", transformed_data_file)

        # Split data into train and test sets
        train_df, test_df = split_data(df)

        # Save train and test data
        save_split_data(train_df, test_df)
    except CustomException as e:
        # Handle custom exceptions
        logger.error("Custom Exception occurred: %s", e)
        raise
    except Exception as e:
        # Handle other exceptions
        error_message = f"Error splitting and saving data: {str(e)}"
        logger.error(error_message)
        raise CustomException(error_message, error_detail=sys.exc_info())

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python split.py <transformed_data_file>")
        sys.exit(1)

    # Get the path to the transformed data file from command-line argument
    transformed_data_file = sys.argv[1]

    # Call the split_data_and_save function with the provided file path
    split_data_and_save(transformed_data_file)
