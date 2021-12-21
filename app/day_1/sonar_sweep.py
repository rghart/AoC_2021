from app.helpers.input_helper import read_input
from app.helpers.print_output import print_output

measurement_list = [int(val) for val in read_input(day_num=1)]


def _should_increase(index, range_cap):
    if range_cap <= 1:
        return measurement_list[index + 1] > measurement_list[index]

    current_depth_amount = 0
    next_depth_amount = 0
    for i in range(index, index + range_cap):
        current_depth_amount += measurement_list[i]
        next_depth_amount += measurement_list[i + 1]
    return next_depth_amount > current_depth_amount


def _get_depth_increases(measurement_window):
    depth_increases = 0
    for i in range(len(measurement_list) - measurement_window):
        if _should_increase(i, measurement_window):
            depth_increases += 1
    return depth_increases


def part_1():
    print_output(day=1, part=1, output=_get_depth_increases(measurement_window=1))


def part_2():
    print_output(day=1, part=2, output=_get_depth_increases(measurement_window=3))


part_1()
part_2()
