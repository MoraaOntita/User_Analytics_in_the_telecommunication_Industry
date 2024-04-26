import sys
import os
import pandas as pd
import logging
from exception import CustomException
from utils import encode_categorical_variables, standardize_numerical_values, perform_pca, save_transformed_data

# Get logger
logger = logging.getLogger(__name__)

def transform_data(file_path):
    """
    Transform the cleaned data by encoding categorical variables, standardizing numerical values, and performing PCA.
    Save transformed data to artifacts folder.
    """
    try:
        # Load cleaned data
        df = pd.read_csv(file_path)
        logger.info("Cleaned data loaded successfully from %s", file_path)

        # Encode categorical variables
        df = encode_categorical_variables(df)

        # Standardize numerical values
        df = standardize_numerical_values(df)

        # Perform PCA
        df_pca = perform_pca(df)

        # Save transformed data
        save_transformed_data(df_pca, 'transformed_data.csv')
        logger.info("Transformed data saved successfully")

    except CustomException as e:
        # Handle custom exceptions
        logger.error("Custom Exception occurred: %s", e)
        raise
    except Exception as e:
        # Handle other exceptions
        error_message = f"Error transforming data: {str(e)}"
        logger.error(error_message)
        raise CustomException(error_message, error_detail=sys.exc_info())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python data_transformation.py <cleaned_data_path>")
        sys.exit(1)
    cleaned_data_path = sys.argv[1]
    print("Cleaned data path:", cleaned_data_path)  # Add this line for debugging
    transform_data(cleaned_data_path)
