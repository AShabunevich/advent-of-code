# counts trees
class tree_counter_tob:
    def __init__(self, run, rise, input_file):
        self.run = int(run)
        self.rise = int(rise)
        self.input_file = input_file

    def tree_count(self):
        with open(self.input_file, 'r') as file:
            data = file.read().splitlines()

        skip = 0
        tree_num = 0

        for i in range(0, len(data), self.rise):
            height = data[i]

            if height[skip % len(height)] == '#':
                tree_num = tree_num + 1

            skip = skip + self.run
        return tree_num

# loop through class


def class_loop(slope_input):
    result = []
    for i in range(len(slope_input)):
        answer = tree_counter_tob(
            slope_input[i][0], slope_input[i][1], 'input3')
        result.append(answer.tree_count())
    return result

# multiply results


def mult_array(array):
    r = 1
    for x in array:
        r = r * x
    print('Multiplication: ' + str(r))


# results
slope_part2 = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print('Array of trees: ' + str(class_loop(slope_part2)))
print('Part 1, trees: ' + str(class_loop(slope_part2)[1]))
mult_array(class_loop(slope_part2))
