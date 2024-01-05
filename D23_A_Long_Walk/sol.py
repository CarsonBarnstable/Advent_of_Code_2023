PATH, WALL = '.', '#'
MOVES = {'<': [(0, -1)], '>': [(0, 1)], 'v': [(1, 0)], '^': [(-1, 0)], PATH: [(0, -1), (0, 1), (1, 0), (-1, 0)]}


def main():
    # getting character-based input
    maze = read_input()
    start, end = (0, maze[0].index(PATH)), (len(maze)-1, maze[-1].index(PATH))

    intersections = get_intersections(maze)
    print(intersections)


def read_input(file="input.txt"):
    grid = []
    with open(file) as f:
        for line in f.readlines():
            grid.append([ch for ch in line.strip('\n')])
    return grid


def get_intersections(grid):
    intersections = []
    row_bounds, col_bounds = range(len(grid)), range(len(grid[-1]))
    # going through all possible cells
    for row_i, row in enumerate(grid):
        for col_i, ch in enumerate(row):
            # if cell is not a wall...
            if ch == WALL:
                continue
            # and cell has 3 or more neighbors
            num_neighbors, row_u, col_u = 0, -1, -1
            for row_change, col_change in MOVES[PATH]:
                row_u, col_u = row_i+row_change, col_i+col_change
                if row_u not in row_bounds or col_u not in col_bounds:
                    continue
                if not grid[row_u][col_u] == WALL:
                    num_neighbors += 1
            if num_neighbors >= 3:
                # then position is an intersection of paths
                intersections.append((row_i, col_i))
    # only after getting all possible intersections in grid
    return intersections


if __name__ == "__main__":
    main()
