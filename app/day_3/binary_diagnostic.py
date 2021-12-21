from app.helpers.input_helper import read_input
from app.helpers.print_output import print_output

my_input = read_input(day_num=3)


def _get_power_consumption():
    new_input_array = []
    for i in range(len(my_input)):
        for ix in range(len(my_input[i])):
            if len(new_input_array) <= ix:
                new_input_array.append(my_input[i][ix])
            else:
                new_input_array[ix] += my_input[i][ix]

    gamma_rate = ''
    epsilon_rate = ''
    for i in range(len(new_input_array)):
        zeroes = 0
        ones = 0
        for x in range(len(new_input_array[i])):
            if new_input_array[i][x] == '0':
                zeroes += 1
            else:
                ones += 1

        if zeroes > ones:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


print_output(day=1, part=1, output=_get_power_consumption())
