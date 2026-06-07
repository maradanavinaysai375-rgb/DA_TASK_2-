import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\VINAY SAI\OneDrive\Desktop\DA TASKS\TASK1\cleaned_dataset.csv")

print(df.describe())

print("\nCategorical Summary")
print(df.describe(include=['object', 'string']))

# Histogram
plt.figure(figsize=(6,4))
df['age'].hist()
plt.title("Age Distribution")
plt.savefig("age_distribution.png")
plt.close()

# Survival Count
plt.figure(figsize=(6,4))
sns.countplot(x='survived', data=df)
plt.title("Survival Distribution")
plt.savefig("survival_distribution.png")
plt.close()

# Gender Count
plt.figure(figsize=(6,4))
sns.countplot(x='sex', data=df)
plt.title("Gender Distribution")
plt.savefig("gender_distribution.png")
plt.close()

# Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include='number').corr(),
            annot=True,
            cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.close()

# Scatter Plot
plt.figure(figsize=(6,4))
sns.scatterplot(x='age', y='fare', data=df)
plt.title("Age vs Fare")
plt.savefig("age_vs_fare.png")
plt.close()

print("EDA completed")