# generate a list of all the possible combinations of 6 numbers from 1 to 49
#
import pandas as pd
import warnings
from bisect import bisect_right
from operator import itemgetter

warnings.simplefilter(action='ignore', category=FutureWarning)


def generate_all_combinations():
    l = []

    for i in range(1, 50):  # for each number in the range 1 to 49
        for j in range(i + 1, 50):  # for each number after i in the range 1 to 49
            for k in range(j + 1, 50):  # for each number after j in the range 1 to 49
                for m in range(k + 1, 50):  # for each number after k in the range 1 to 49
                    for n in range(m + 1, 50):  # for each number after m in the range 1 to 49
                        for o in range(n + 1, 50):  # for each number after n in the range 1to49
                            # if len([i, j, k, m]) == 4 and len([o]) == 2:
                            l.append([i, j, k, m, n, o])
    return l


all_numbers = generate_all_combinations()
# Program to extract number
# of rows using Python


# Give the location of the file
file_name = ("e:\loto.xlsx")
xl_file = pd.ExcelFile(file_name)
df = pd.read_excel(file_name, sheet_name='Sheet2')
df.loc[0]
df['Data tragerii->'] = df['Data tragerii->'].dt.strftime('%Y-%m-%d')

extrageri = df.values.tolist()

extrageri_asc = [[varianta[0], sorted(varianta[1:7])] for varianta in extrageri]
#
# [j.pop(0) for j in extrageri]
# [k.sort() for k in extrageri]

indexes = []
for extr in extrageri_asc:
    a = [all_numbers.index(extr[1]), extr[0]]
    indexes.append(a)

indexes_asc = sorted(indexes, key=itemgetter(0))


def neighbours(value, indexes):
    # right = the index of the first number in my_list that is larger than value
    right = bisect_right(indexes_plain, value)

    # Case where value is in my_list
    if indexes_plain[right - 1] == value:
        bounds = [indexes_plain[right - 1]]

    # No lower bound or upper bound
    elif right == 0:
        bounds = ["No lower bound", indexes_plain[right]]
    elif right == len(indexes_plain):
        bounds = [indexes_plain[right - 1], "No upper bound"]

    # value is in between 2 values in my_list
    else:
        bounds = [indexes_plain[right - 1], indexes_plain[right]]
    return bounds


### show neighbours

value = 4229610
indexes_plain = [i[0] for i in indexes_asc]
nei = neighbours(value, indexes_plain)
nei

###
all_numbers.index([3,13,26,28,29,30])

# with open('e:\loto_indexex.txt', 'w') as f:
#     for line in indexes:
#         f.write(f"{line}\n")
