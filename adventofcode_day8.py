with open('input8a', 'r') as file:
    input = []
    for line in file:
        line = line.rstrip().split(' ')
        input.append((line[0], int(line[1])))


def acc_p1(data):
    acc_sum = 0
    index = 0
    data_len = len(data)

    while index >= 0 and index < data_len:
        operation = data[index][0]
        argument = data[index][1]

        # rewrites used operation based on index
        data[index] = ('inf', argument)

        if operation == 'acc':  # 'acc' updates 'acc_sum' based on argument
            acc_sum += argument
        elif operation == 'jmp':  # 'jmp' updates 'index' based on argument
            index += argument
        elif operation == 'inf':  # stops when hits 'inf'
            break

        # 'acc' and 'nop' umpades 'index' by +1
        if operation != 'jmp':
            index += 1

    return acc_sum, operation


def part1():
    acc_sum, last_opperation = acc_p1(input[:])
    return acc_sum


print("Part 1: ", part1())


def part2():
    index_change = 0
    input_copy = input[:]
    keep_going = True
    input_copy_len = len(input_copy)

    while keep_going:
        acc_sum, last_operation = acc_p1(input_copy)

        # last operations 'inf' keep running loop
        if last_operation == 'inf':
            keep_going = True
            input_copy = input[:]

            while input_copy[index_change][0] == 'acc':
                index_change += 1

            # changed instructions, and repeat
            if input_copy[index_change][0] == 'nop':
                input_copy[index_change] = ('jmp', input_copy[index_change][1])
            elif input_copy[index_change][0] == 'jmp':
                input_copy[index_change] = ('nop', input_copy[index_change][1])

            index_change += 1

        # last operation not 'inf', stop loop
        else:
            keep_going = False

    return acc_sum


print("Part 2: ", part2())
