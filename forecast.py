import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
conn = sqlite3.connect("finance.db")
df = pd.read_sql_query("SELECT * FROM expenses", conn)
conn.close()

df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period("M")

monthly = df.groupby('month')['amount'].sum().reset_index()

# Convert month to number
monthly['month_number'] = np.arange(len(monthly))

X = monthly[['month_number']]
y = monthly['amount']

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next 3 months
future_months = np.arange(len(monthly), len(monthly) + 3).reshape(-1, 1)
predictions = model.predict(future_months)

print("Future Predictions:")
print(predictions)

# Plot
plt.plot(monthly['month_number'], y, label="Actual")
plt.plot(future_months, predictions, linestyle='--', label="Predicted")
plt.legend()
plt.title("Expense Forecast")
plt.show()