import sys
import pandas as pd
from sklearn.cluster import KMeans
from utils import save_model
import logging
from exception import CustomException
from config import ARTIFACTS_DIR

# Get logger
logger = logging.getLogger(__name__)

def train_kmeans(train_data_file, num_clusters):
    """
    Train a K-means clustering model on the train data.
    """
    try:
        # Load train data
        train_df = pd.read_csv(train_data_file)
        logger.info("Train data loaded successfully from %s", train_data_file)

        # Instantiate K-means model
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)

        # Train K-means model
        kmeans.fit(train_df)

        # Save the trained model
        save_model(kmeans, "kmeans_model.pkl")
        logger.info("K-means model trained and saved")
    except CustomException as e:
        # Handle custom exceptions
        logger.error("Custom Exception occurred: %s", e)
        raise
    except Exception as e:
        # Handle other exceptions
        error_message = f"Error training K-means model: {str(e)}"
        logger.error(error_message)
        raise CustomException(error_message, error_detail=sys.exc_info())

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python model_training.py <train_data_file> <num_clusters>")
        sys.exit(1)

    # Get the path to the train data file and number of clusters from command-line arguments
    train_data_file = sys.argv[1]
    num_clusters = int(sys.argv[2])

    # Call the train_kmeans function with the provided file path and number of clusters
    train_kmeans(train_data_file, num_clusters)
