# CREDIT EDA PROJECT
# By: Gadipudi Sirisha (Y21IT029)

# Step 1: Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Settings
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# Step 2: Load Dataset
df = pd.read_csv('credit_data.csv')  # Replace with your actual file name
print("First 5 Rows:\n", df.head())
print("Data Info:")
print(df.info())
print("Summary Stats:\n", df.describe())

# Step 3: Data Cleaning
# Handle Missing Values
print("Missing Values:\n", df.isnull().sum())
df.fillna(df.mean(numeric_only=True), inplace=True)

# Handle Duplicates
print("Duplicate Rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

# Save Cleaned Data (Optional)
df.to_csv('credit_data_cleaned.csv', index=False)

# Step 4: Univariate Analysis
# Histograms
sns.histplot(df['income'], kde=True)
plt.title('Income Distribution')
plt.show()

sns.histplot(df['loan_amount'], kde=True)
plt.title('Loan Amount Distribution')
plt.show()

# Boxplots
sns.boxplot(y=df['credit_score'])
plt.title('Credit Score Boxplot')
plt.show()

# Countplots
sns.countplot(x='gender', data=df)
plt.title('Gender Count')
plt.show()

sns.countplot(x='defaulted', data=df)
plt.title('Default Status Count')
plt.show()

# Step 5: Bivariate Analysis
# Boxplot - Income vs Default
sns.boxplot(x='defaulted', y='income', data=df)
plt.title("Income vs Default Status")
plt.show()

# Scatter Plot
sns.scatterplot(x='age', y='loan_amount', hue='defaulted', data=df)
plt.title("Age vs Loan Amount with Default Status")
plt.show()

# Heatmap
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# Step 6: Multivariate Analysis
# Pair Plot
sns.pairplot(df[['income', 'loan_amount', 'credit_score', 'defaulted']], hue='defaulted')
plt.show()

# 3D Scatter Plot (Optional)
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['income'], df['loan_amount'], df['credit_score'], c=df['defaulted'], cmap='viridis')
ax.set_xlabel('Income')
ax.set_ylabel('Loan Amount')
ax.set_zlabel('Credit Score')
plt.title("3D Scatter Plot")
plt.show()

# Step 7: Data Transformation
# Log Transform
df['log_income'] = np.log(df['income'] + 1)

# Standardization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['income_scaled', 'loan_amount_scaled']] = scaler.fit_transform(df[['income', 'loan_amount']])

# Min-Max Scaling
from sklearn.preprocessing import MinMaxScaler
minmax = MinMaxScaler()
df[['credit_score_scaled']] = minmax.fit_transform(df[['credit_score']])

# Final Output Check
print("Transformed Data Sample:\n", df.head())

# END
print("\n✅ Credit EDA Completed Successfully.")
