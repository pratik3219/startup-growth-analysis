import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your cleaned Excel file
df = pd.read_excel(r'C:\Users\prati\OneDrive\Desktop\project\Project Data.xlsx')

# Show first few rows
print("\n===== FIRST 5 ROWS =====")
print(df.head())

# Show basic info about data
print("\n===== DATA INFO =====")
print(df.info())

# Show summary statistics
print("\n===== STATISTICS =====")
print(df.describe())

# Check for missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

df['Funding(in $)'] = pd.to_numeric(df['Funding(in $)'], errors='coerce')




# 1️⃣ Funding distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Funding(in $)'], bins=30, kde=True)
plt.title('Funding Distribution')
plt.xlabel('Total Funding (in ₹ or $)')
plt.ylabel('Count')
plt.show()

# 2️⃣ Sector-wise average funding
plt.figure(figsize=(10,6))
top_industry = df.groupby('Industry')['Funding(in $)'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=top_industry.values, y=top_industry.index, palette='coolwarm')
plt.title('Top 10 Sectors by Average Funding')
plt.xlabel('Average Funding')
plt.ylabel('Sector')
plt.show()

# 3️⃣ City-wise startup count
plt.figure(figsize=(10,6))
top_cities = df['City'].value_counts().head(10)
sns.barplot(x=top_cities.values, y=top_cities.index, palette='viridis')
plt.title('Top 10 Cities by Startup Count')
plt.xlabel('Number of Startups')
plt.ylabel('City')
plt.show()

# 4️⃣ Correlation heatmap (numeric columns)
plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# 5️⃣ Funding vs Employees (bubble chart)
if 'Number of Employees' in df.columns:
    plt.figure(figsize=(8,6))
    plt.scatter(df['Number of Employees'], df['Funding(in $)'], alpha=0.6)
    plt.title('Funding vs Number of Employees')
    plt.xlabel('Number of Employees')
    plt.ylabel('Total Funding')
    plt.show()

print("\n✅ EDA completed successfully!")
