def dive_pt1():
    with open("inputpt1.txt", 'r') as f:
        depth = 0
        horizontal = 0
        lines = f.readlines()
        for line in lines:
            if "forward" in line:
                horizontal += int(line.split(" ")[1])
            if "down" in line:
                depth -= int(line.split(" ")[1])
            if "up" in line:
                depth += int(line.split(" ")[1])
        return abs(depth * horizontal)


def dive_pt2():
    with open("inputpt1.txt", 'r') as f:
        depth = 0
        horizontal = 0
        aim = 0
        lines = f.readlines()
        for line in lines:
            if "forward" in line:
                forward_value = int(line.split(" ")[1])
                horizontal += forward_value
                depth += aim * forward_value
            if "down" in line:
                aim += int(line.split(" ")[1])
            if "up" in line:
                aim -= int(line.split(" ")[1])
        return abs(depth * horizontal)


print(f'Part one: {dive_pt1()}')
print(f'Part one: {dive_pt2()}')
