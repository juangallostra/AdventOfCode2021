from utils import parse_input

def part1(commands):
    # measurements = parse_input(m)
    # split by action
    actions = dict(forward=0, up=0, down=0)
    for cmd in commands:
        actions[cmd.split(' ')[0]] += int(cmd.split(' ')[1])
    return (-actions['up'] + actions['down']) * actions['forward']


def part2(commands):
    # up and down modify aim
    # forward moves x forward and increases depth by aim * x
    sign = {'up': -1, 'down': 1}
    f = d = aim = 0
    for cmd in commands:
        action, x = cmd.split(' ')
        value = int(x)
        if 'forward' in action:
            # update f and d
            f += value
            d += aim * value
        else:
            aim += sign[action] * value
    return d * f

def main(input_file):
    measurements = parse_input(input_file)
    print(part1(measurements))
    print(part2(measurements))


if __name__ == '__main__':
    main('d2/data/input.txt')
