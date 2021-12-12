def dumbo_pt1():
    with open('input', 'r') as f:
        grid = [list(map(int, list(x.strip()))) for x in f.readlines()]

        def flash(current_cell, already_flashed):
            sum = 1
            for direction in [(1, 0), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]:
                ny = current_cell[0] + direction[0]
                nx = current_cell[1] + direction[1]
                if 0 <= ny < len(grid) and 0 <= nx < len(grid):
                    grid[ny][nx] += 1
                    if grid[ny][nx] > 9 and (ny, nx) not in already_flashed:
                        already_flashed[(ny, nx)] = True
                        sum += flash((ny, nx), already_flashed)
            return sum

        total_flashes = 0
        for step in range(100):

            flashed_cells = {}

            for y in range(len(grid)):
                for x in range(len(grid)):
                    cell = (y, x)
                    grid[y][x] += 1
                    if grid[y][x] > 9 and (y, x) not in flashed_cells:
                        flashed_cells[(y, x)] = True
                        total_flashes += flash(cell, flashed_cells)
            for c in flashed_cells:
                grid[c[0]][c[1]] = 0
        return total_flashes


def dumbo_pt2():
    with open('input', 'r') as f:
        grid = [list(map(int, list(x.strip()))) for x in f.readlines()]

        def flash(current_cell, already_flashed):
            for direction in [(1, 0), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]:
                ny = current_cell[0] + direction[0]
                nx = current_cell[1] + direction[1]
                if 0 <= ny < len(grid) and 0 <= nx < len(grid):
                    grid[ny][nx] += 1
                    if grid[ny][nx] > 9 and (ny, nx) not in already_flashed:
                        already_flashed[(ny, nx)] = True
                        flash((ny, nx), already_flashed)

        step = 0
        while True:
            step += 1
            flashed_cells = {}

            for y in range(len(grid)):
                for x in range(len(grid)):
                    cell = (y, x)
                    grid[y][x] += 1
                    if grid[y][x] > 9 and (y, x) not in flashed_cells:
                        flashed_cells[(y, x)] = True
                        flash(cell, flashed_cells)
            for c in flashed_cells:
                grid[c[0]][c[1]] = 0
            if len(flashed_cells) == len(grid) * len(grid):
                return step


print(f'Part one {dumbo_pt1()}')
print(f'Part one {dumbo_pt2()}')
