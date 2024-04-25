import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, column):
    """
    Plot distribution of a numerical column using a histogram.

    Args:
    - df (pd.DataFrame): The DataFrame containing the data.
    - column (str): The name of the column to plot.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_boxplot(df, x_column, y_column):
    """
    Plot boxplot of a numerical column grouped by a categorical column.

    Args:
    - df (pd.DataFrame): The DataFrame containing the data.
    - x_column (str): The name of the categorical column.
    - y_column (str): The name of the numerical column.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=x_column, y=y_column, data=df)
    plt.title(f'Boxplot of {y_column} by {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def plot_heatmap(df):
    """
    Plot a heatmap of the correlation matrix of the DataFrame.

    Args:
    - df (pd.DataFrame): The DataFrame containing the data.
    """
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.show()

def plot_barplot(df, x_column, y_column):
    """
    Plot a bar plot of a numerical column grouped by a categorical column.

    Args:
    - df (pd.DataFrame): The DataFrame containing the data.
    - x_column (str): The name of the categorical column.
    - y_column (str): The name of the numerical column.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x_column, y=y_column, data=df)
    plt.title(f'Bar plot of {y_column} by {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def plot_histplot(df, batch_size=5):
    """
    Plot histograms for all columns in the dataset.
    
    Parameters:
        df (DataFrame): The DataFrame containing the data.
        batch_size (int): Number of columns to plot in each batch.
    """
    num_columns = len(df.columns)
    num_batches = (num_columns + batch_size - 1) // batch_size  # Calculate number of batches

    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, num_columns)
        
        batch_columns = df.columns[start_idx:end_idx]
        
        fig, axes = plt.subplots(nrows=1, ncols=len(batch_columns), figsize=(16, 6))
        
        for ax, column in zip(axes, batch_columns):
            if df[column].dtype == 'float64' or df[column].dtype == 'int64':
                sns.histplot(df[column], kde=True, ax=ax)
                ax.set_title(f'Histogram of {column}')
                ax.set_xlabel(column)
                ax.set_ylabel('Frequency')
            else:
                sns.countplot(data=df, x=column, order=df[column].value_counts().index, ax=ax)
                ax.set_title(f'Bar plot of {column}')
                ax.set_xlabel(column)
                ax.set_ylabel('Frequency')
                ax.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.show()

def plot_scatterplot(df, x_column, y_column):
    """
    Plot a scatter plot of two numerical columns.

    Args:
    - df (pd.DataFrame): The DataFrame containing the data.
    - x_column (str): The name of the first numerical column.
    - y_column (str): The name of the second numerical column.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_column, y=y_column, data=df)
    plt.title(f'Scatter plot of {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def plot_countplot(df, column):
    """
    Plot a count plot of a categorical column.

    Args:
    - df (pd.DataFrame): The DataFrame containing the data.
    - column (str): The name of the categorical column.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(x=column, data=df)
    plt.title(f'Count plot of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

def plot_lineplot(df, x_column, y_column):
    """
    Plot a line plot of two numerical columns.

    Args:
    - df (pd.DataFrame): The DataFrame containing the data.
    - x_column (str): The name of the first numerical column.
    - y_column (str): The name of the second numerical column.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x_column, y=y_column, data=df)
    plt.title(f'Line plot of {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

