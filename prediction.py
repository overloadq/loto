import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np

##### Prediction ####################
df = pd.DataFrame(win_index, columns=["index", "date", "numbers", "factors"])

# Select the date and number columns
df = df[["index", "date"]]
# Preprocess the data
df["date"] = pd.to_datetime(df["date"])
df["date"] = (df["date"] - df["date"].min()) / np.timedelta64(365, 'D')
# df["date"] = pd.to_datetime(df["date"])
# df["date"] = (df["date"] - df["date"].min()) / np.timedelta64(1, 'D')


# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df[["date"]], df["index"], test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Make a prediction on a future date
future_date = pd.to_datetime("2023-01-11")
future_date = (future_date - pd.to_datetime(df["date"].min())) / np.timedelta64(2190, 'D')
# prediction = model.predict([[future_date]])
prediction = int(model.predict([[future_date]])[0])
# print(f"Prediction for {future_date}: {prediction[0]:.2f}")
print(f"Prediction for {future_date}: {prediction}")
###



pairs = []
for i in range(100):
    model = WinIndexModel(win_index)
    mse = model.evaluate()
    prediction = model.predict("2023-01-11")
    pairs.append((mse, prediction))

min_pair = min(pairs, key=lambda x: x[0])
min_first = min_pair[0]
min_second = min_pair[1]
print("Smallest first element:", min_first)
print("Second element in pair for smallest first:", min_second)