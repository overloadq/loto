# generate a list of all the possible combinations of 6 numbers from 1 to 49
import pandas as pd
import warnings
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
xl_file.close()
extrageri = df.values.tolist()

extrageri_asc = [[varianta[0], sorted(varianta[1:7])] for varianta in extrageri]


indexes = []
for extr in extrageri_asc:
    a = [all_numbers.index(extr[1]), extr[0]]
    indexes.append(a)

indexes_asc = sorted(indexes, key=itemgetter(0))


def find_neighbors(numbers, value):
  try:
    # find the index of the searched value in the list
    index = numbers.index(value)

    # get the values at the index before and after the searched value
    before = numbers[index - 1] if index > 0 else None
    after = numbers[index + 1] if index < len(numbers) - 1 else None

    # return the neighbors and a message indicating that the searched value was found
    return before, after, "Value found in list"
  except ValueError:
    # if the value is not in the list, find the closest values
    closest = min(numbers, key=lambda x: abs(x - value))
    index = numbers.index(closest)
    before = numbers[index - 1] if index > 0 else None
    after = numbers[index + 1] if index < len(numbers) - 1 else None

    # return the neighbors and a message indicating that the searched value was not found
    return before, after, "Value not found in list"


### show neighbours

value = 6875120
indexes_plain = [i[0] for i in indexes_asc]

find_neighbors(indexes_plain, value)

###
all_numbers.index([5, 22, 27, 30, 34, 49])

# with open('e:\loto_indexex.txt', 'w') as f:
#     for line in indexes:
#         f.write(f"{line}\n")
