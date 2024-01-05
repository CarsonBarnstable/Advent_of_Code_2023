PATH, WALL = '.', '#'
MOVES = {'<': [(0, -1)], '>': [(0, 1)], 'v': [(1, 0)], '^': [(-1, 0)], PATH: [(0, -1), (0, 1), (1, 0), (-1, 0)]}


def main():
    # getting character-based input
    maze = read_input("mini_input.txt")
    start, end = (0, maze[0].index(PATH)), (len(maze)-1, maze[-1].index(PATH))

    # getting all 'vertextes' in graph-to-be
    intersections = get_intersections(maze)
    intersections = [start]+intersections+[end]  # and adding both ends

    # creating adjacency list to fully formulate graph
    adjacents = get_adjacents(maze, intersections)
    print(intersections)
    print(adjacents)

    # def exploration to find the longest path


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
            for row_shift, col_shift in MOVES[PATH]:
                row_u, col_u = row_i+row_shift, col_i+col_shift
                if row_u not in row_bounds or col_u not in col_bounds:
                    continue
                if not grid[row_u][col_u] == WALL:
                    num_neighbors += 1
            if num_neighbors >= 3:
                # then position is an intersection of paths
                intersections.append((row_i, col_i))
    # only after getting all possible intersections in grid
    return intersections


def get_adjacents(grid, vertices):
    row_bounds, col_bounds = range(len(grid)), range(len(grid[-1]))
    # have to use "crawling searcher" to determine which verticies are immediately reachable (and how far away)
    adjacent_vertices = {vertex: {} for vertex in vertices}
    # using a somewhat-modified DFS on each vertex
    for vertex in vertices:
        already_visited = set()
        to_expand_queue = [(0, vertex[0], vertex[1])]
        while to_expand_queue:
            dist, r_i, c_i = to_expand_queue.pop()
            already_visited.add((r_i, c_i))
            # if point of interest is a real vertex
            if (r_i, c_i) in vertices and dist != 0 and not (r_i, c_i) == vertex:
                # remember how far away from the chosen start it is
                adjacent_vertices[vertex][(r_i, c_i)] = dist
                continue
            # try searching anything in valid direction otherwise
            for row_shift, col_shift in MOVES[grid[r_i][c_i]]:
                row_u, col_u = r_i+row_shift, c_i+col_shift
                if row_u not in row_bounds or col_u not in col_bounds:
                    continue  # as long as it is within the grid
                if ((row_u, col_u) in already_visited and (row_u, col_u) not in vertices) or grid[row_u][col_u] == WALL:
                    continue  # and it's a valid location to expand to
                to_expand_queue.append((dist+1, row_u, col_u))
    # only once all the adjacencies are found
    return adjacent_vertices


if __name__ == "__main__":
    main()
