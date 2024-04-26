import sys
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from joblib import load

def evaluate_model(model_path, test_data_path):
    # Load the trained K-means model
    kmeans_model = load(model_path)

    # Load the test data
    test_data = pd.read_csv(test_data_path)

    # Predict cluster labels for the test data
    test_cluster_labels = kmeans_model.predict(test_data)

    # Calculate evaluation metrics
    inertia = kmeans_model.inertia_
    silhouette = silhouette_score(test_data, test_cluster_labels)
    davies_bouldin = davies_bouldin_score(test_data, test_cluster_labels)
    calinski_harabasz = calinski_harabasz_score(test_data, test_cluster_labels)

    # Print the evaluation metrics
    print("Evaluation Metrics:")
    print(f"Inertia: {inertia}")
    print(f"Silhouette Score: {silhouette}")
    print(f"Davies-Bouldin Index: {davies_bouldin}")
    print(f"Calinski-Harabasz Index: {calinski_harabasz}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python evaluate_model.py <model_path> <test_data_path>")
        sys.exit(1)

    model_path = sys.argv[1]
    test_data_path = sys.argv[2]

    evaluate_model(model_path, test_data_path)
