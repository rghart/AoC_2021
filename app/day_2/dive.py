from app.helpers.input_helper import read_input
from app.helpers.print_output import print_output

my_input = read_input(day_num=2)


def _get_position(uses_aim):
    horizontal = 0
    aim = 0
    depth = 0

    for i in range(len(my_input)):
        str_array = my_input[i].split()
        movement, move_number = str_array[0], int(str_array[1])

        if movement == 'forward':
            horizontal += move_number
            if uses_aim:
                depth += (aim * move_number)
        elif movement == 'down':
            if uses_aim:
                aim += move_number
            else:
                depth += move_number
        elif movement == 'up':
            if uses_aim:
                aim -= move_number
            else:
                depth -= move_number

    return horizontal * depth


def part_1():
    print_output(day=2, part=1, output=_get_position(uses_aim=False))


def part_2():
    print_output(day=2, part=2, output=_get_position(uses_aim=True))


part_1()
part_2()
