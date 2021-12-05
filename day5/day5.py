def hydro_pt1():
    points = {}
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        for l in lines:
            p1, p2 = l.split(" -> ")
            x1, y1 = [int(i) for i in p1.split(",")]
            x2, y2 = [int(i) for i in p2.split(",")]
            if x1 == x2:
                for p in range(min(y1, y2), max(y1, y2) + 1):
                    if (x1, p) in points:
                        points[(x1, p)] += 1
                    else:
                        points[(x1, p)] = 1
            if y1 == y2:
                for p in range(min(x1, x2), max(x1, x2) + 1):
                    if (p, y1) in points:
                        points[(p, y1)] += 1
                    else:
                        points[(p, y1)] = 1

        overlapping_points = 0
        for k, v in points.items():
            if v > 1:
                overlapping_points += 1
        return overlapping_points


def hydro_pt2():
    points = {}
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        for l in lines:
            p1, p2 = l.split(" -> ")
            x1, y1 = [int(i) for i in p1.split(",")]
            x2, y2 = [int(i) for i in p2.split(",")]

            left = None
            right = None
            starting_height = None
            ending_height = None

            if x1 < x2:
                left = x1
                right = x2
                starting_height = y1
                ending_height = y2
            else:
                left = x2
                right = x1
                starting_height = y2
                ending_height = y1

            if (left, starting_height) not in points:
                points[(left, starting_height)] = 1
            else:
                points[(left, starting_height)] += 1
            while True:

                if left != right:
                    left += 1

                if starting_height > ending_height:
                    starting_height -= 1
                elif starting_height < ending_height:
                    starting_height += 1
                point = (left, starting_height)
                if point not in points:
                    points[point] = 1
                else:
                    points[point] += 1

                if left == right and starting_height == ending_height:
                    break

        overlapping_points = 0
        for k, v in points.items():
            if v > 1:
                overlapping_points += 1
        return overlapping_points


print(f'Part one: {hydro_pt1()}')
print(f'Part one: {hydro_pt2()}')
