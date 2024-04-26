import os

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS_DIR = os.path.join(os.path.dirname(BASE_DIR), 'artifacts')

# Constants
MISSING_THRESHOLD = 0.7
# Number of principal components for PCA
PCA_COMPONENTS = 45

# the test size for splitting
TEST_SIZE = 0.2

