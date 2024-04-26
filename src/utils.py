import pandas as pd
import os
import logging
from config import MISSING_THRESHOLD, ARTIFACTS_DIR
from exception import CustomException
import sys

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from config import PCA_COMPONENTS
from sklearn.model_selection import train_test_split
from config import ARTIFACTS_DIR, TEST_SIZE 

import pickle

# Get logger
logger = logging.getLogger(__name__)


def drop_missing_columns(df):
    """
    Drop columns with more than MISSING_THRESHOLD missing values.
    """
    try:
        threshold = MISSING_THRESHOLD * len(df)
        cleaned_df = df.dropna(axis=1, thresh=threshold)
        logger.info("Dropped columns with more than %d missing values", threshold)
        return cleaned_df
    except Exception as e:
        error_message = f"Error dropping missing columns: {str(e)}"
        logger.error(error_message)
        raise CustomException(error_message, error_detail=sys.exc_info())


def impute_missing_values(df):
    """
    Impute missing values in numerical columns with mean and categorical columns with mode.
    """
    try:
        numerical_cols = df.select_dtypes(include='number').columns
        categorical_cols = df.select_dtypes(exclude='number').columns

        # Impute numerical columns with mean
        df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

        # Impute categorical columns with mode
        df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])

        logger.info("Imputed missing values")
        return df
    except Exception as e:
        error_message = f"Error imputing missing values: {str(e)}"
        logger.error(error_message)
        raise CustomException(error_message, error_detail=sys.exc_info())


def save_cleaned_data(df, file_name):
    """
    Save cleaned data to artifacts folder.
    """
    try:
        # Create artifacts directory if it doesn't exist
        if not os.path.exists(ARTIFACTS_DIR):
            os.makedirs(ARTIFACTS_DIR)

        file_path = os.path.join(ARTIFACTS_DIR, file_name)
        df.to_csv(file_path, index=False)
        logger.info("Cleaned data saved successfully to %s", file_path)
    except Exception as e:
        error_message = f"Error saving cleaned data: {str(e)}"
        logger.error(error_message)
        raise CustomException(error_message, error_detail=sys.exc_info())


################################################################################################################################ Data_transformation

def encode_categorical_variables(df):
    """
    Encode categorical variables using label encoding.
    """
    # Identify categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    # Perform label encoding
    label_encoder = LabelEncoder()
    for col in categorical_cols:
        df[col] = label_encoder.fit_transform(df[col])
    
    return df


def standardize_numerical_values(df):
    """
    Standardize numerical values using StandardScaler.
    """
    # Identify numerical columns
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Perform standardization
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    return df


def perform_pca(df):
    """
    Perform PCA for dimensionality reduction.
    """
    pca = PCA(n_components=PCA_COMPONENTS)
    pca_data = pca.fit_transform(df)
    
    return pd.DataFrame(data=pca_data, columns=[f'PC{i}' for i in range(1, PCA_COMPONENTS+1)])

def save_transformed_data(df, file_name):
    """
    Save transformed data to artifacts folder.
    """
    try:
        # Create artifacts directory if it doesn't exist
        if not os.path.exists(ARTIFACTS_DIR):
            os.makedirs(ARTIFACTS_DIR)

        file_path = os.path.join(ARTIFACTS_DIR, file_name)
        df.to_csv(file_path, index=False)
        logger.info("Transformed data saved successfully to %s", file_path)
    except Exception as e:
        error_message = f"Error saving transformed data: {str(e)}"
        logger.error(error_message)
        raise CustomException(error_message, error_detail=sys.exc_info())
    
###################################################################################################################################################Splitting Data

def split_data(df):
    """
    Split the transformed data into train and test sets.
    """
    try:
        # Split the data using train_test_split
        train_df, test_df = train_test_split(df, test_size=TEST_SIZE, random_state=42)
        return train_df, test_df
    except Exception as e:
        error_message = f"Error splitting data: {str(e)}"
        logger.error(error_message)
        raise CustomException(error_message, error_detail=sys.exc_info())

def save_split_data(train_df, test_df):
    """
    Save train and test data to artifacts folder.
    """
    try:
        # Create artifacts directory if it doesn't exist
        if not os.path.exists(ARTIFACTS_DIR):
            os.makedirs(ARTIFACTS_DIR)

        # Save train and test data
        train_file_path = os.path.join(ARTIFACTS_DIR, 'train_data.csv')
        test_file_path = os.path.join(ARTIFACTS_DIR, 'test_data.csv')
        train_df.to_csv(train_file_path, index=False)
        test_df.to_csv(test_file_path, index=False)
        logger.info("Train data saved successfully to %s", train_file_path)
        logger.info("Test data saved successfully to %s", test_file_path)
    except Exception as e:
        error_message = f"Error saving split data: {str(e)}"
        logger.error(error_message)
        raise CustomException(error_message, error_detail=sys.exc_info())
    
##################################################################################################################################################Model pickle file

# Get logger
logger = logging.getLogger(__name__)

def save_model(model, model_name):
    """
    Save a trained model to the artifacts directory.
    
    Args:
        model: The trained model object to be saved.
        model_name: The name of the model file.
    """
    try:
        model_dir = os.path.join(ARTIFACTS_DIR, "models")
        os.makedirs(model_dir, exist_ok=True)
        model_file = os.path.join(model_dir, model_name)
        with open(model_file, 'wb') as f:
            pickle.dump(model, f)
        logger.info("Model saved successfully to %s", model_file)
    except Exception as e:
        error_message = f"Error saving model: {str(e)}"
        logger.error(error_message)
        raise CustomException(error_message, error_detail=sys.exc_info())
