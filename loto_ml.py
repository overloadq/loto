import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Load data into a DataFrame
df = pd.read_csv("E:\\loto_data.csv")

# Preprocess the data
df["date"] = pd.to_datetime(df["date"])
df["date"] = (df["date"] - df["date"].min()) / np.timedelta64(365, 'D')

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df[["date"]], df["number"], test_size=0.2)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Make a prediction on a future date
future_date = pd.to_datetime("2022-10-30")
future_date = (future_date - pd.to_datetime(df["date"].min())) / np.timedelta64(365, 'D')
# prediction = model.predict([[future_date]])
prediction = int(model.predict([[future_date]])[0])
#print(f"Prediction for {future_date}: {prediction[0]:.2f}")
print(f"Prediction for {future_date}: {prediction}")
