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


def plot_histplot(df, x_column, y_column):
    """
    Plot a histogram of a numerical column.

    Args:
    - df (pd.DataFrame): The DataFrame containing the data.
    - x_column (str): The name of the numerical column.
    - y_column (str): The name of the categorical column (optional).
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df[x_column], kde=True, hue=y_column, multiple="stack")
    plt.title(f'Histogram of {x_column}')
    plt.xlabel(x_column)
    plt.ylabel('Frequency')
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

