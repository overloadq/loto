# generate a list of all the possible combinations of 6 numbers from 1 to 49
import pandas as pd
import warnings
from operator import itemgetter
from itertools import combinations

warnings.simplefilter(action='ignore', category=FutureWarning)


def generate_all_combinations():
    # create a list of all numbers in the range 1 to 49
    numbers = list(range(1, 50))
    # generate all possible combinations of 6 numbers from the list of numbers
    combinations_list = list(combinations(numbers, 6))
    # convert each tuple in the combinations_list to a list
    combinations_lists = [list(t) for t in combinations_list]
    # return the list of lists
    return combinations_lists


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
    a = [all_numbers.index(win[1]), win[0], win[1]]
    win_index.append(a)

win_index_asc = sorted(win_index, key=itemgetter(0))



def find_neighbors(numbers, value):
    """numbers list is like: [20832, '2017-03-23', [1, 2, 4, 11, 35, 39]]"""
    # helper function to find the closest values to the searched value
    def closest_neighbors(value):
        closest = min(numbers, key=lambda x: abs(x - value))
        index = numbers.index(closest)
        before = numbers[index - 1] if index > 0 else None
        after = numbers[index + 1] if index < len(numbers) - 1 else None
        return before, after

    try:
        # find the index of the searched value in the list
        index = numbers.index(value)

        # get the values at the index before and after the searched value
        before, after = closest_neighbors(value)

        # return the neighbors and a message indicating that the searched value was found
        return before, after, "Value found in list"
    except ValueError:
        # if the value is not in the list, find the closest values
        before, after = closest_neighbors(value)

        # return the neighbors and a message indicating that the searched value was not found
        return before, after, "Value not found in list"


### show neighbours

indexes_plain = [i[0] for i in win_index_asc]


value = 6788360
find_neighbors(indexes_plain, 6788360)

###
all_numbers.index([5, 22, 27, 30, 34, 49])

# with open('e:\loto_indexex.txt', 'w') as f:
#     for line in indexes:
#         f.write(f"{line}\n")
