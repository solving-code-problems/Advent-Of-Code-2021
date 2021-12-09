

def smoke_basin_pt1():

    with open('input', 'r') as f:
        grid = [list(map(int,list(line.strip()))) for line in f.readlines()]
        low_points = []
        low_points_xy = []

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                cell = grid[y][x]
                isLowPoint = True
                for dir in [(1,0), (-1,0), (0, 1), (0,-1)]:
                    new_y = y + dir[0]
                    new_x = x + dir[1]
                    if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                        neighbour_value = grid[new_y][new_x]
                        if cell >= neighbour_value:
                            isLowPoint = False
                            break
                if isLowPoint:
                    low_points.append(cell + 1)
                    low_points_xy.append((y,x))
        return sum(low_points), low_points_xy

def smoke_basin_pt2(minimums):
    grid = []
    with open('input', 'r') as f:
        grid = [list(map(int, list(line.strip()))) for line in f.readlines()]

    def flood(m, visited):
        if m in visited:
            return
        visited[m] = True
        y,x = m
        for dir in [(1,0), (-1,0), (0, 1), (0,-1)]:
            new_y = y + dir[0]
            new_x = x + dir[1]
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):
                neighbour_value = grid[new_y][new_x]
                if neighbour_value != 9:
                    flood((new_y,new_x), visited)
        return visited

    basin_sizes = []
    for m in minimums:
        basin_sizes.append(len(flood(m, {})))

    basin_sizes.sort()
    prod = 1
    for size in basin_sizes[-3:]:
        prod *= size
    return prod

res, minimums = smoke_basin_pt1()

print(f'Part one {res}')
print(f'Part two {smoke_basin_pt2(minimums)}')