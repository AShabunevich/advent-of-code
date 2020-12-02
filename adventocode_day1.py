import numpy as np

array = np.loadtxt('input1')

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] + array[j] == 2020:
            print(str(array[i]) + ' + ' + str(array[j]) + ' = 2020')
            print(str(array[i]) + ' * ' + str(array[j]) +
                  ' = ' + str(array[i] * array[j]))
        for k in range(j+1, len(array)):
            if array[i] + array[j] + array[k] == 2020:
                print(str(array[i]) + ' + ' + str(array[j]) +
                      ' + ' + str(array[k]) + ' = 2020')
                print(str(array[i]) + ' * ' + str(array[j]) + ' * ' +
                      str(array[k]) + ' = ' + str(array[i] * array[j] * array[k]))
