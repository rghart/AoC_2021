def read_input(day_num):
    with open(f'app/day_{day_num}/input.txt') as f:
        return f.read().splitlines()
