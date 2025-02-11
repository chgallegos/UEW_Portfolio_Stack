import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# Replace 'your_dataset.csv' with your file path
data = pd.read_csv('your_dataset.csv')

# 1. Inspecting the Dataset
print("First 5 Rows of the Dataset:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nSummary Statistics:")
print(data.describe())

# 2. Check for Missing Values
print("\nMissing Values Per Column:")
print(data.isnull().sum())

# 3. Visualizing Data Distributions
print("\nVisualizing Data Distributions:")
for column in data.select_dtypes(include='number').columns:
    plt.figure(figsize=(6, 4))
    sns.histplot(data[column], kde=True, bins=30)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

# 4. Correlation Analysis
print("\nCorrelation Matrix:")
correlation_matrix = data.corr()
print(correlation_matrix)

plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# 5. Categorical Data Analysis
categorical_columns = data.select_dtypes(include='object').columns
print("\nCategorical Column Value Counts:")
for column in categorical_columns:
    print(f"\n{column}:")
    print(data[column].value_counts())

    # Visualizing Categorical Data
    plt.figure(figsize=(6, 4))
    sns.countplot(data=data, x=column, order=data[column].value_counts().index)
    plt.title(f"Value Counts of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

# 6. Detecting Outliers
print("\nBoxplot Analysis for Numerical Columns:")
for column in data.select_dtypes(include='number').columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=data[column])
    plt.title(f"Boxplot for {column}")
    plt.show()
