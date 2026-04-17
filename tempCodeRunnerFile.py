# 3️⃣ City-wise startup count
# plt.figure(figsize=(10,6))
# top_cities = df['city'].value_counts().head(10)
# sns.barplot(x=top_cities.values, y=top_cities.index, palette='viridis')
# plt.title('Top 10 Cities by Startup Count')
# plt.xlabel('Number of Startups')
# plt.ylabel('City')
# plt.show()

# # 4️⃣ Correlation heatmap (numeric columns)
# plt.figure(figsize=(8,6))
# sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm', fmt='.2f')
# plt.title('Correlation Heatmap')
# plt.show()

# # 5️⃣ Funding vs Employees (bubble chart)
# if 'num_employees' in df.columns:
#     plt.figure(figsize=(8,6))
#     plt.scatter(df['num_employees'], df['Funding(in $)'], alpha=0.6)
#     plt.title('Funding vs Number of Employees')
#     plt.xlabel('Number of Employees')
#     plt.ylabel('Total Funding')
#     plt.show()