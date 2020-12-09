import numpy as np


with open('input6', 'r') as file:
    data = file.read().replace('\n', ' ').split('  ')
    new_data1 = []
    new_data2 = []

    # data for Part1 (sets of each group as a strings, intersections)
    for element in data:
        new_data1.append(''.join(set(element.replace(' ', ''))))

    # data for Part2 (nested array for each group)
    for element in range(len(data)):
        new_data2.append(data[element].split(' '))
    del new_data2[len(data)-1][-1]


# counts questions for Part 1
def yes_questions_P1(input1):
    size_strings = []
    sum = 0

    # length of each intersection
    for string in input1:
        size_strings.append(len(string))

    # sum of all intersections
    for num in size_strings:
        sum += num

    return sum


# counts questions for Part 2
def yes_questions_P2(input2):
    sets = []
    inter_array = []

    # creates sets for each group
    for i in range(len(input2)):
        sets2 = []
        for j in input2[i]:
            sets2.append(set(j))
        sets.append(sets2)

    # array of intersections for each group
    for i in range(len(sets)):
        inter = len(sets[i][0].intersection(*sets[i]))
        inter_array.append(inter)

    # sum of intersections
    sum2 = np.sum(inter_array)

    return sum2


print('Part 1: {}'.format(yes_questions_P1(new_data1)))
print('Part 2: {}'.format(yes_questions_P2(new_data2)))
