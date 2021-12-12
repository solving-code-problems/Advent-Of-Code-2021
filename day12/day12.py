def passaga_pt1():
    def connect(frm, to, dict):
        if frm not in dict:
            dict[frm] = []
        if to not in dict:
            dict[to] = []
        dict[frm].append(to)
        if frm != "start":
            dict[to].append(frm)

    with open('input', 'r') as f:
        adjecancy = {}

        lines = [x.strip().split("-") for x in f.readlines()]
        for connection in lines:
            frm, too = connection
            connect(frm, too, adjecancy)

        def explore(point, path, seen):
            found_paths = 0
            if point == "end":
                print(path)
                return 1
            visitable_points = adjecancy[point]
            for point in visitable_points:
                new_path, new_seen = path.copy(), seen.copy()
                if point in seen:
                    if point.isupper():
                        new_path.append(point)
                        new_seen[point] = True
                        found_paths += explore(point, new_path, new_seen)
                else:
                    new_path.append(point)
                    new_seen[point] = True
                    found_paths += explore(point, new_path, new_seen)
            return found_paths

        path = ["start"]
        seen = {"start": True}
        return explore("start", path, seen)


def passaga_pt2():
    def connect(frm, to, dict):
        if frm not in dict:
            dict[frm] = []
        if to not in dict:
            dict[to] = []
        dict[frm].append(to)
        if frm != "start":
            dict[to].append(frm)

    with open('input', 'r') as f:
        adjecancy = {}

        lines = [x.strip().split("-") for x in f.readlines()]
        for connection in lines:
            frm, too = connection
            connect(frm, too, adjecancy)

        def explore(point, path, seen, visited_small_cave):
            found_paths = 0
            if point == "end":
                print(path)
                return 1
            visitable_points = adjecancy[point]
            for point in visitable_points:
                if point == "start":
                    continue

                new_path, new_seen = path.copy(), seen.copy()
                if point in seen:
                    if point.isupper():
                        new_path.append(point)
                        found_paths += explore(point, new_path, new_seen, visited_small_cave)
                    if point.islower() and not visited_small_cave:
                        found_paths += explore(point, new_path, new_seen, True)
                else:
                    new_path.append(point)
                    new_seen[point] = True
                    found_paths += explore(point, new_path, new_seen, visited_small_cave)
            return found_paths

        path = ["start"]
        seen = {"start": True}
        has_visited_small_cave = False
        return explore("start", path, seen, has_visited_small_cave)


print(passaga_pt1())
print(passaga_pt2())
