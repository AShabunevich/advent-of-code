import numpy as np
import re

with open('input2', 'r') as file:
    data = file.read().replace('\n', ' ')
    data = data.replace('-', ' ')

data_split = re.split(': |\n | ', data)
del data_split[-1]  # removes empty data

min_nums = data_split[0::4]  # min numbers

max_nums = data_split[1::4]  # max numbers

letters = data_split[2::4]  # letters of search

strings = data_split[3::4]  # strings of search

count_array = np.array([])

num = 0
num1 = 0

for i in range(len(letters)):
    count = strings[i].count(letters[i])
    # creates array with counted letters
    count_array = np.append(count_array, count)
    count_arr = int(count_array[i])
    min_num = int(min_nums[i])
    max_num = int(max_nums[i])
    
    # first condition (part 1)
    if count_arr >= min_num and count_arr <= max_num:
        num += 1
        
    # second condition (part 2)
    if strings[i][min_num-1] == letters[i] or strings[i][max_num-1] == letters[i]:
        if strings[i][min_num-1] != strings[i][max_num-1]:
            num1 += 1

print('Part1, # of correct passwords: ' + str(num))
print('Part2, # of correct passwords: ' + str(num1))
