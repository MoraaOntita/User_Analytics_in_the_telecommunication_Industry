import os
import sys
import logging
from exception import CustomException
from components.db_connections import DBConnection
from utils import log_exception, save_cleaned_file
from utils import load_cleaned_data


class DataCleaner:
    """
    A class to perform data cleaning operations.
    """

    def __init__(self, threshold=0.7):
        """
        Initializes the DataCleaner object.

        Args:
        - threshold (float): The threshold for dropping columns with missing values.
        """
        self.threshold = threshold

    @log_exception
    def remove_columns_with_missing_values(self, df):
        """
        Removes columns with missing values exceeding the threshold.

        Args:
        - df (pd.DataFrame): The input DataFrame.

        Returns:
        - pd.DataFrame: The DataFrame with columns removed.
        """
        missing_percentage = df.isnull().mean()
        columns_to_drop = missing_percentage[missing_percentage > self.threshold].index
        cleaned_df = df.drop(columns=columns_to_drop)
        return cleaned_df

    @log_exception
    def fill_missing_values_numerical(self, df):
        """
        Fills missing values in numerical columns with mean.

        Args:
        - df (pd.DataFrame): The input DataFrame.

        Returns:
        - pd.DataFrame: The DataFrame with missing values filled in numerical columns.
        """
        numerical_cols = df.select_dtypes(include='number').columns
        for col in numerical_cols:
            mean_value = df[col].mean()
            df[col].fillna(mean_value, inplace=True)
        return df

    @log_exception
    def fill_missing_values_categorical(self, df):
        """
        Fills missing values in categorical columns with the mode.

        Args:
        - df (pd.DataFrame): The input DataFrame.

        Returns:
        - pd.DataFrame: The DataFrame with missing values filled in categorical columns.
        """
        categorical_cols = df.select_dtypes(include='object').columns
        for col in categorical_cols:
            mode_value = df[col].mode()[0]
            df[col].fillna(mode_value, inplace=True)
        return df



def main():
    try:
        # Load cleaned data
        cleaned_data = load_cleaned_data("../artifacts/cleaned_xdr_data.csv")

        # Perform data cleaning operations
        cleaner = DataCleaner()
        cleaned_df = cleaner.remove_columns_with_missing_values(cleaned_data)
        cleaned_df = cleaner.fill_missing_values_numerical(cleaned_df)
        cleaned_df = cleaner.fill_missing_values_categorical(cleaned_df)
        
        # Print the cleaned DataFrame for debugging
        print("Cleaned DataFrame:", cleaned_df)

        # Save the cleaned DataFrame
        save_cleaned_file(cleaned_df, "path/to/save/cleaned_data.csv")  # Adjust the save file path as needed

    except CustomException as e:
        # Handle any custom exceptions raised during the operations
        log_exception(e)

if __name__ == "__main__":
    main()





