import math
import heapq


class Node:
    def __init__(self, key, cost):
        self.key = key
        self.distance = math.inf
        self.previous = None
        self.cost = cost

    def __lt__(self, other):
        return self.distance < other.distance


def chiton_pt1():
    with open('input', 'r') as f:
        grid = [list(map(int, list(x.strip()))) for x in f.readlines()]

    unvisited_set = {}
    visited_set = {}

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cost = grid[y][x]
            unvisited_set[(x, y)] = Node((x, y), cost)

    def djikstra(graph):
        unvisited_set[(0, 0)].distance = 0

        queue = [(0, unvisited_set[(0, 0)])]
        while True:
            if not queue:
                break
            dist, current = heapq.heappop(queue)
            visited_set[current] = True

            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = current.key[0] + dir[0]
                ny = current.key[1] + dir[1]
                neighbour = (nx, ny)
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    if neighbour in visited_set:
                        continue

                    neighbour_node = unvisited_set[neighbour]
                    current_node = current

                    new_distance = current_node.distance + neighbour_node.cost
                    if new_distance < neighbour_node.distance:
                        neighbour_node.distance = new_distance
                        neighbour_node.previous = current
                        heapq.heappush(queue, (neighbour_node.distance, neighbour_node))

    djikstra(unvisited_set)

    index_of_last_node = len(grid) - 1
    return unvisited_set[(index_of_last_node, index_of_last_node)].distance


def chiton_pt2():
    with open('input', 'r') as f:
        grid = [list(map(int, list(x.strip()))) for x in f.readlines()]
        width = len(grid)
        height = len(grid)

        big_grid = []
        for section in range(5 * height):
            big_grid.append([0] * (width * 5))

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                big_grid[y][x] = grid[y][x]

        time = 5
        for row in range(1, time + 1):
            for section in range(1, time):
                yoffset_next = row * width
                yoffset_current = row * width - width

                offset_previous = section * width - width
                offset_current = section * width

                for y in range(len(grid)):
                    for x in range(len(grid[0])):
                        previous = big_grid[y + yoffset_current][x + offset_previous]
                        if previous + 1 > 9:
                            big_grid[y + yoffset_current][x + offset_current] = 1
                        else:
                            big_grid[y + yoffset_current][x + offset_current] = previous + 1
                if row != 5:
                    # COPY SECOND SECTION DOWN AND LEFT
                    for y in range(len(grid)):
                        for x in range(len(grid[0])):
                            previous = big_grid[y + yoffset_current][x + offset_previous]
                            if previous + 1 > 9:
                                big_grid[y + yoffset_next][x + offset_previous] = 1
                            else:
                                big_grid[y + yoffset_next][x + offset_previous] = previous + 1

    grid = big_grid
    unvisited_set = {}
    visited_set = {}

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cost = grid[y][x]
            unvisited_set[(x, y)] = Node((x, y), cost)

    def djikstra(graph):
        unvisited_set[(0, 0)].distance = 0

        queue = [(0, unvisited_set[(0, 0)])]
        while True:
            if not queue:
                break
            dist, current = heapq.heappop(queue)
            visited_set[current] = True
            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = current.key[0] + dir[0]
                ny = current.key[1] + dir[1]
                neighbour = (nx, ny)
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    if neighbour in visited_set:
                        continue

                    neighbour_node = unvisited_set[neighbour]
                    current_node = current

                    new_distance = current_node.distance + neighbour_node.cost
                    if new_distance < neighbour_node.distance:
                        neighbour_node.distance = new_distance
                        neighbour_node.previous = current
                        heapq.heappush(queue, (neighbour_node.distance, neighbour_node))

    djikstra(unvisited_set)

    index_of_last_node = len(grid) - 1
    return unvisited_set[(index_of_last_node, index_of_last_node)].distance


print(f'Part one: {chiton_pt1()}')
print(f'Part two: {chiton_pt2()}')
