# A simple script to get you started with data analysis!
# We'll use a classic dataset, but you can swap in your own CSV file.

# First, we need to load a few libraries we'll use.
# pandas is for working with data tables (DataFrames).
# matplotlib and seaborn are for creating visualizations.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# --- Part 1: Getting the Data Ready ---

# For this example, we'll load the Iris dataset.
# If you had your own data in a file, you'd use a line like this instead:
# my_data = pd.read_csv("your_file.csv")

iris_data = load_iris()
df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df['species'] = iris_data.target_names[iris_data.target]

# Let's take a peek at the first few rows to see what our data looks like.
print("Here's a look at the first 5 rows of our data:")
print(df.head())
print("-" * 40) # A simple line to make the output easy to read

# The Iris dataset is very clean, but it's always a good idea to check for missing data.
print("Checking for any missing data (we expect to see all zeros):")
print(df.isnull().sum())
print("-" * 40)


# --- Part 2: Doing some basic math on the data ---

# A quick summary of the main statistics (like the average, min, and max)
# for all the numerical columns.
print("A quick summary of the numbers in our dataset:")
print(df.describe())
print("-" * 40)

# Let's find the average measurements for each type of flower.
# This helps us see the differences between the species.
print("Average measurements for each species:")
print(df.groupby('species').mean())
print("-" * 40)


# --- Part 3: Making some charts to see the patterns ---

# We'll make a few different types of charts to help us understand the data better.
# We'll use seaborn for a nicer visual style.
sns.set_style("whitegrid")

# Chart 1: A bar chart to compare the average petal length of each species.
plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal length (cm)', data=df, palette='pastel')
plt.title('Average Petal Length of Each Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# Chart 2: A histogram to see how the sepal width is distributed across all flowers.
# The 'kde=True' option adds a smooth curve to show the overall shape.
plt.figure(figsize=(8, 6))
sns.histplot(df['sepal width (cm)'], kde=True, color='teal')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Count of Flowers')
plt.show()

# Chart 3: A scatter plot to see the relationship between sepal length and petal length.
# This chart is great for seeing if two numbers are related.
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='viridis')
plt.title('Relationship Between Sepal Length and Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()

# That's it! You can now adapt this script for your own datasets.
# Just change the file loading part at the top and the column names in the charts.
