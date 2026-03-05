import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("finance.db")

# Load data
df = pd.read_sql_query("SELECT * FROM expenses", conn)
conn.close()

# Convert date column
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period("M")

# Monthly spending
monthly = df.groupby('month')['amount'].sum()

print("Monthly Spending:")
print(monthly)

# Plot
monthly.plot(kind='bar')
plt.title("Monthly Spending")
plt.xlabel("Month")
plt.ylabel("Total Spending")
plt.show()