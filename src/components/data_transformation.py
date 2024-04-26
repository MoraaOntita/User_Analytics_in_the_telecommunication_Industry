import os
import sys
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.decomposition import PCA
from components.clean import load_cleaned_data
from utils import save_transformed_data
from logger import logging
from exception import CustomException
from typing import Optional, Any

class DataTransformer:
    """
    A class to perform data transformation on cleaned data.
    """

    def __init__(self) -> None:
        """
        Initializes the DataTransformer object.
        """
        self.logger = logging.getLogger(__name__)

    def encode_categorical_variables(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Encodes categorical variables using one hot encoding.

        Args:
            data (pd.DataFrame): The cleaned data.

        Returns:
            pd.DataFrame: The data with encoded categorical variables.
        """
        try:
            categorical_columns = data.select_dtypes(include=['object']).columns.tolist()

            if not categorical_columns:
                return data

            encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
            encoded_data = pd.DataFrame(encoder.fit_transform(data[categorical_columns]))

            data = pd.concat([data.drop(columns=categorical_columns), encoded_data], axis=1)
            return data
        except Exception as e:
            error_message = f"Error encoding categorical variables: {str(e)}"
            self.logger.error(error_message)
            raise CustomException(error_message, error_detail=sys.exc_info())

    def standardize_numerical_variables(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Standardizes numerical variables.

        Args:
            data (pd.DataFrame): The cleaned data.

        Returns:
            pd.DataFrame: The data with standardized numerical variables.
        """
        try:
            numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns.tolist()

            if not numerical_columns:
                return data

            scaler = StandardScaler()
            data[numerical_columns] = scaler.fit_transform(data[numerical_columns])
            return data
        except Exception as e:
            error_message = f"Error standardizing numerical variables: {str(e)}"
            self.logger.error(error_message)
            raise CustomException(error_message, error_detail=sys.exc_info())

    def reduce_dimensionality(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Reduces dimensionality using PCA.

        Args:
            data (pd.DataFrame): The cleaned data.

        Returns:
            pd.DataFrame: The data with reduced dimensionality.
        """
        try:
            pca = PCA()
            transformed_data = pca.fit_transform(data)
            return transformed_data
        except Exception as e:
            error_message = f"Error reducing dimensionality: {str(e)}"
            self.logger.error(error_message)
            raise CustomException(error_message, error_detail=sys.exc_info())

    def transform_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Transforms the cleaned data.

        Args:
            data (pd.DataFrame): The cleaned data.

        Returns:
            pd.DataFrame: The transformed data.
        """
        try:
            transformed_data = self.encode_categorical_variables(data)
            transformed_data = self.standardize_numerical_variables(transformed_data)
            transformed_data = self.reduce_dimensionality(transformed_data)
            return transformed_data
        except CustomException as e:
            self.logger.error(f"Custom Exception occurred: {str(e)}")
            raise

def main():
    try:
        # Load cleaned data
        cleaned_data = load_cleaned_data()

        # Instantiate DataTransformer
        transformer = DataTransformer()

        # Transform data
        transformed_data = transformer.transform_data(cleaned_data)

        # Save transformed data
        save_transformed_data(transformed_data, 'artifact/transformed_data.csv')
    except CustomException as e:
        logging.error(f"Custom Exception occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()







