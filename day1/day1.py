def sonar_sweep_pt1():
    count = 0
    with open("day1/inputpt1.txt", 'r') as f:
        previous = None
        for line in f.readlines():
            if not previous:
                previous = int(line)
            else:
                if previous < int(line):
                    count += 1
            previous = int(line)
    return count


def sonar_sweep_pt2():
    left_point = 0
    right_point = 2
    count = 0
    with open("day1/inputpt2.txt", 'r') as f:
        values = list(map(lambda line: int(line), f.readlines()))
        previous = values[0] + values[1] + values[2]
        while right_point != len(values) - 1:
            new_window = previous - values[left_point] + values[right_point + 1]
            if new_window > previous:
                count += 1
            previous = new_window
            left_point += 1
            right_point += 1
    return count


print(f'Part one: {sonar_sweep_pt1()}')
print(f'Part one: {sonar_sweep_pt2()}')
