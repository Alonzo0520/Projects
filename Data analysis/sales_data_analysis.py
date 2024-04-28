import pandas as pd
import matplotlib.pyplot as plt

# Load sales data from CSV file
sales_df = pd.read_csv("Cannabis_Retail_Sales_by_Week_Ending.csv")

# Plot histogram of Adult-Use Retail Sales
plt.figure(figsize=(8, 6))
plt.hist(sales_df['Adult-Use Retail Sales'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Adult-Use Retail Sales')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Plot histogram of Medical Marijuana Retail Sales
plt.figure(figsize=(8, 6))
plt.hist(sales_df['Medical Marijuana Retail Sales'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribution of Medical Marijuana Retail Sales')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
