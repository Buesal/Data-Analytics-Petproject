import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_project.csv')
print(df.head())

print(df.isnull().sum())

df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
df['Date'] = pd.to_datetime(df['Date'])
df.drop(columns=['Unnamed: 4'], inplace = True)

print(df.describe())

sales_by_category = df.groupby('Category')['Sales'].sum()
print(sales_by_category)

sales_by_date = df.groupby('Date')['Sales'].sum()

sales_by_category.plot(kind='bar', title = 'Sales by category')
plt.ylabel('total sales')
plt.show()

plt.figure(figsize = (10,6))
plt.plot(sales_by_date, marker = 'o', linestyle = '-')
plt.title('Sales by date')
plt.ylabel('Sales')
plt.xlabel('Date')
plt.grid(True)
plt.show()