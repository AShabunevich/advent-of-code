with open('input5', 'r') as file:
    file = file.read().splitlines()


def new_array(input_file):
    array = []
    num_id = []

    # convers to binary values
    for line in input_file:
        a = line.replace('F', '0')
        a = a.replace('B', '1')
        a = a.replace('L', '0')
        a = a.replace('R', '1')
        array.append(a)

    # converts binary to value
    for i in range(len(array)):
        num = int(array[i], 2)
        num_id.append(num)

    seat_id = set(range(min(num_id), max(num_id))).difference(set(num_id))

    print('Max seat id: {}'.format(max(num_id)))
    print('My seat id: {}'.format(list(seat_id)[0]))


print(new_array(file))
