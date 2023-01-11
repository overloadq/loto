# generate a list of all the possible combinations of 6 numbers from 1 to 49
import pandas as pd
import warnings
from operator import itemgetter
from itertools import combinations
from pprint import pprint
import time

import numpy as np
# import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)
# get the start time
st = time.time()


def prime_factorization(number):
    factors = []
    # Start with the smallest prime number (2)
    divisor = 2
    while number > 1:
        # If the number is divisible by the divisor, add it to the list of factors and divide the number by the divisor
        while number % divisor == 0:
            factors.append(divisor)
            number = number / divisor
        # Increment the divisor by 1
        divisor += 1
    return factors


def generate_all_combinations():
    # create a list of all numbers in the range 1 to 49
    numbers = list(range(1, 50))
    # generate all possible combinations of 6 numbers from the list of numbers
    combinations_list = list(combinations(numbers, 6))
    # convert each tuple in the combinations_list to a list
    # combinations_lists = [list(t) for t in combinations_list]
    # return the list of lists
    return combinations_list


all_numbers = generate_all_combinations()

# Open the excel file containing the winning lottery numbers, from 2016
# return the content as a list
file_name = ("e:\loto.xlsx")
with pd.ExcelFile(file_name) as xl_file:
    df = pd.read_excel(file_name, sheet_name='Sheet2')
    # df.loc[0]
    df['Data tragerii->'] = df['Data tragerii->'].dt.strftime('%Y-%m-%d')
    extrageri = df.values.tolist()

# order the number ascending
winnings = [[field[0], sorted(field[1:7])] for field in extrageri]

# map the indexes of the winning numbers with the indexes of all the possibilities, 13.983.816 combination
win_index = []
for win in winnings:
    my_index = all_numbers.index(tuple(win[1]))
    a = [my_index, win[0], win[1], prime_factorization(my_index)]
    win_index.append(a)

win_index_asc = sorted(win_index, key=itemgetter(0))


class Neighbours:
    def __init__(self, mylist, value, all_numbers):
        self.before = None
        self.after = None
        self.mylist = mylist
        self.all_numbers = all_numbers
        self.value = value
        self.found = ""

        numbers = [n[0] for n in self.mylist]

        # helper function to find the closest values to the searched value
        def closest_neighbors(value):
            closest = min(numbers, key=lambda x: abs(x - value))
            index = numbers.index(closest)
            self.before = numbers[index - 1] if index > 0 else None
            self.after = numbers[index + 1] if index < len(numbers) - 1 else None

        try:
            # find the index of the searched value in the list
            index = numbers.index(value)

            # get the values at the index before and after the searched value
            closest_neighbors(value)

            # return a message indicating that the searched value was found
            self.found = "Value found in list"
        except ValueError:
            # if the value is not in the list, find the closest values
            closest_neighbors(value)

            # return a message indicating that the searched value was not found
            self.found = "Value not found in list"

    def select_lines(self):
        lines = []
        indexes = [self.before, self.after]
        for win in self.mylist:
            if win[0] is not None and win[0] in indexes:
                lines.append(win)
        lines.append(self.found)
        searched = ["My Search:", self.value, self.all_numbers[self.value], prime_factorization(self.value)]
        lines.append(searched)
        return lines


class WinIndexModel:
    def __init__(self, win_index):
        self.df = pd.DataFrame(win_index, columns=["index", "date", "numbers", "factors"])
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
        # print(f"Mean Squared Error: {mse:.2f}")
        return mse

    def predict(self, future_date):
        future_date = pd.to_datetime(future_date)
        future_date = (future_date - pd.to_datetime(self.df["date"].min())) / np.timedelta64(365, 'D')
        prediction = int(self.model.predict([[future_date]])[0])
        # print(f"Prediction for {future_date}: {prediction}")
        return prediction


# model = WinIndexModel(win_index)
# mse = model.evaluate()
# prediction = model.predict("2023-01-11")


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
        print("Smallest first element:", min_first)
        print("Second element in pair for smallest first:", min_second)
        return min_second


mse_pred = MSE_Prediction(win_index, "2023-01-11")
mse_pred.run_n_times(10000)
best_prediction = mse_pred.get_min_pair()

n = Neighbours(win_index_asc, best_prediction, all_numbers)
pprint(n.select_lines())

### show neighbours
# if __name__ == "__main__":
show = win_index[-70:]
pprint(show)

# factor = [prime_factorization(f[0]) for f in show]
# pprint(factor)

value = 6067946
n = Neighbours(win_index_asc, value, all_numbers)
pprint(n.select_lines())

prime_factorization(value)
# get the end time
et = time.time()

elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

# all_numbers.index((5, 22, 27, 30, 34, 49))

# with open('e:\loto_indexex.txt', 'w') as f:
#     for line in indexes:
#         f.write(f"{line}\n")
