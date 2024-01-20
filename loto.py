import pandas as pd
import os
import warnings
from operator import itemgetter
from itertools import combinations
from pprint import pprint
import time
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

def prime_factorization(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number = number / divisor
        divisor += 1
    return factors

def generate_all_combinations():
    numbers = list(range(1, 50))
    combinations_list = list(combinations(numbers, 6))
    return combinations_list

def process_lottery_data(file_path):
    if not os.path.exists(file_path):
        raise ValueError(f"The file {file_path} does not exist.")
    with pd.ExcelFile(file_path) as xl_file:
        df = pd.read_excel(file_path, sheet_name='Sheet2')
        df['Data tragerii->'] = df['Data tragerii->'].dt.strftime('%Y-%m-%d')
        winnings = [[row[0], sorted(row[1:7])] for row in df.values.tolist()]
    return winnings

def map_win_index(all_numbers, winnings):
    win_index = []
    for win in winnings:
        my_index = all_numbers.index(tuple(win[1]))
        a = [my_index, win[0], win[1], calculate_gap(win[1]), prime_factorization(my_index)]
        win_index.append(a)
    return win_index

def calculate_gap(numbers):
    gap = []
    for i in range(len(numbers)-1):
        gap.append(numbers[i + 1] - numbers[i])
    return gap

class Neighbours:
    def __init__(self, win_index_asc, value, all_numbers):
        self.before = None
        self.after = None
        self.mylist = win_index_asc
        self.all_numbers = all_numbers
        self.value = value
        self.found = ""

        numbers = [n[0] for n in self.mylist]

        def closest_neighbors(value):
            closest = min(numbers, key=lambda x: abs(x - value))
            index = numbers.index(closest)
            self.before = numbers[index - 1] if index > 0 else None
            self.after = numbers[index + 1] if index < len(numbers) - 1 else None

        try:
            index = numbers.index(value)
            closest_neighbors(value)
            self.found = "Value found in list"
        except ValueError:
            closest_neighbors(value)
            self.found = "Value not found in list"

    def select_lines(self):
        lines = []
        indexes = [self.before, self.after]
        for win in self.mylist:
            if win[0] is not None and win[0] in indexes:
                lines.append(win)
        lines.append(self.found)
        searched = ["My Search:", self.value, self.all_numbers[self.value], calculate_gap(self.all_numbers[self.value]),
                    prime_factorization(self.value)]
        lines.append(searched)
        return searched

class WinIndexModel:
    def __init__(self, win_index):
        self.df = pd.DataFrame(win_index, columns=["index", "date", "numbers", "gap", "factors"])
        self.df = self.df[["index", "date"]]
        self.df["date"] = pd.to_datetime(self.df["date"])
        self.df["date"] = (self.df["date"] - self.df["date"].min()) / np.timedelta64(365, 'D')
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.df[["date"]], self.df["index"],
                                                                                test_size=0.2)
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)

    def evaluate(self):
        y_pred = self.model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, y_pred)
        return mse

    def predict(self, future_date):
        future_date = pd.to_datetime(future_date)
        future_date = (future_date - pd.to_datetime(self.df["date"].min())) / np.timedelta64(365, 'D')
        prediction = int(self.model.predict([[future_date]])[0])
        return prediction

class MSE_Prediction:
    def __init__(self, win_index, future_date):
        self.win_index = win_index
        self.future_date = future_date
        self.pairs = []

    def run_n_times(self, n):
        for i in range(n):
            model = WinIndexModel(self.win_index)
            mse = model.evaluate()
            prediction = model.predict(self.future_date)
            self.pairs.append((mse, prediction))

    def get_min_pair(self):
        min_pair = min(self.pairs, key=lambda x: x[0])
        min_first = min_pair[0]
        min_second = min_pair[1]
        return min_second

def search_number(win_index, number):
    for item in win_index:
        if item[0] == number:
            return item[:3]
    return None

all_numbers = generate_all_combinations()
file_path = "e:\\loto.xlsx"
winnings = process_lottery_data(file_path)
win_index = map_win_index(all_numbers, winnings)
win_index_asc = sorted(win_index, key=itemgetter(0))

for r in range(20):
    mse_pred = MSE_Prediction(win_index, "2024-01-21")
    mse_pred.run_n_times(1000)
    best_prediction = mse_pred.get_min_pair()
    n = Neighbours(win_index_asc, best_prediction, all_numbers)
    pprint(n.select_lines())

value = 8827091
n = Neighbours(win_index_asc, value, all_numbers)
pprint(n.select_lines())
# Print the neighbours
print(f"Before: {n.before}")
print(f"After: {n.after}")
print(f"Found: {n.found}")

search_number(win_index, n.after)
search_number(win_index, n.before)





# all_numbers.index((5, 22, 27, 30, 34, 49))

with open('e:\\loto_gaps.txt', 'w') as f:
    for line in win_index:
        output = ";".join(map(str, line))
        f.write(output+'\n')
        
# pprint(win_index[-10:])
pprint([x[0] for x in win_index[-100:]])