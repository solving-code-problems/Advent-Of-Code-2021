def transparent(is_part_one):
    folds = []
    points = set()

    def print_points():
        arr = [[0] * 50 for x in range(10)]
        for p in points:
            arr[p[1]][p[0]] = 8
        s = ""
        for row in arr:
            for c in row:
                if c == 0:
                    s += "░"
                else:
                    s += "▓"
            s += "\n"
        print(s)

    with open('input', 'r') as f:
        lines = [x.strip() for x in f.readlines()]
        for line in lines:
            if line:
                if line.startswith("fold"):
                    direction, magnitude = line.split("along ")[1].split("=")
                    folds.append((direction, int(magnitude)))
                else:
                    x, y = line.split(",")
                    points.add((int(x), int(y)))

        def translate_up(point, magnitude):
            x, y = point
            diff = abs(point[1] - magnitude)
            return x, y - (diff * 2)

        def translate_left(point, magnitude):
            x, y = point
            diff = abs(point[0] - magnitude)
            return x - (diff * 2), y

        for fold in folds:
            direction, magnitude = fold
            if direction == "y":
                points_to_move = list(filter(lambda p: p[1] > magnitude, points))
                for p in points_to_move:
                    points.remove(p)
                    points.add(translate_up(p, magnitude))
            if direction == "x":
                points_to_move = list(filter(lambda p: p[0] > magnitude, points))
                for p in points_to_move:
                    points.remove(p)
                    points.add(translate_left(p, magnitude))
            if is_part_one:
                print(len(points))
                break
    if not is_part_one:
        print_points()
    else:
        return len(points)


print(f'Part one {transparent(True)}')
print(f'Part two {transparent(False)}')
