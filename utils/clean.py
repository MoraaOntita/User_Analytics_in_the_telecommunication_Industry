import pandas as pd
from sklearn.impute import SimpleImputer

class DataCleaner:
    """
    A class to perform data cleaning operations.
    """

    def __init__(self, threshold=0.7) -> None:
        """
        Initializes the DataCleaner object.

        Args:
        - threshold (float): The threshold for dropping columns with missing values.
        """
        self.threshold = threshold

    def remove_columns_with_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
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

    def fill_missing_values_numerical(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Fills missing values in numerical columns with mean.

        Args:
        - df (pd.DataFrame): The input DataFrame.

        Returns:
        - pd.DataFrame: The DataFrame with missing values filled in numerical columns.
        """
        numerical_cols = df.select_dtypes(include=['number']).columns

        # Fill missing values in numerical columns with mean
        imputer_numerical = SimpleImputer(strategy='mean')
        df[numerical_cols] = imputer_numerical.fit_transform(df[numerical_cols])

        return df

    def fill_missing_values_categorical(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Fills missing values in categorical columns with the mode.

        Args:
        - df (pd.DataFrame): The input DataFrame.

        Returns:
        - pd.DataFrame: The DataFrame with missing values filled in categorical columns.
        """
        categorical_cols = df.select_dtypes(include=['object']).columns

        for col in categorical_cols:
            mode_val = df[col].mode()[0]
            df[col] = df[col].fillna(mode_val)

        return df