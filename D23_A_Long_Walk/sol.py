PATH, WALL = '.', '#'
MOVES = {'<': [(0, -1)], '>': [(0, 1)], 'v': [(1, 0)], '^': [(-1, 0)], PATH: [(0, 1), (1, 0), (-1, 0), (0, -1)]}


def main():
    moves = MOVES
    # getting character-based input
    maze = read_input("input.txt")
    start, end = (0, maze[0].index(PATH)), (len(maze)-1, maze[-1].index(PATH))

    # * * * * * PART 1 SOLUTION * * * * *
    print("Part 1:", get_longest_path(maze, moves, start, end))

    # * * * * * PART 2 SOLUTION * * * * *
    moves = {pos: moves[PATH] for pos in moves.keys()}
    print("Part 2:", get_longest_path(maze, moves, start, end))


def read_input(file="input.txt"):
    grid = []
    with open(file) as f:
        for line in f.readlines():
            grid.append([ch for ch in line.strip('\n')])
    return grid


def get_longest_path(_maze, _moves, _from, _to):
    # getting all 'vertextes' in graph-to-be
    intersections = get_intersections(_maze, _moves)
    intersections = [_from]+intersections+[_to]  # and adding both ends
    # creating adjacency list to fully formulate graph
    adjacents = get_adjacents(_maze, intersections, _moves)
    # dfs exploration to find the longest path
    return dfs_longest(adjacents, _from, _to)


def get_intersections(grid, valid_moves):
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
            for row_shift, col_shift in valid_moves[PATH]:
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


def get_adjacents(grid, vertices, valid_moves):
    row_bounds, col_bounds = range(len(grid)), range(len(grid[-1]))
    # have to use "crawling searcher" to determine which verticies are immediately reachable (and how far away)
    adjacent_vertices = {vertex: {} for vertex in vertices}
    # using a somewhat-modified DFS on each vertex
    for vertex in vertices:
        already_visited = set()
        to_expand_queue = [(0, vertex[0], vertex[1])]
        while to_expand_queue:
            dist, r_i, c_i = to_expand_queue.pop()
            if (r_i, c_i) in already_visited:
                continue
            already_visited.add((r_i, c_i))
            # if point of interest is a real vertex
            if (r_i, c_i) in vertices and dist != 0 and not (r_i, c_i) == vertex:
                # remember how far away from the chosen start it is
                adjacent_vertices[vertex][(r_i, c_i)] = dist
                continue
            # try searching anything in valid direction otherwise
            for row_shift, col_shift in valid_moves[grid[r_i][c_i]]:
                row_u, col_u = r_i+row_shift, c_i+col_shift
                if row_u not in row_bounds or col_u not in col_bounds:
                    continue  # as long as it is within the grid
                if ((row_u, col_u) in already_visited and (row_u, col_u) not in vertices) or grid[row_u][col_u] == WALL:
                    continue  # and it's a valid location to expand to
                to_expand_queue.append((dist+1, row_u, col_u))
    # only once all the adjacencies are found
    return adjacent_vertices


def dfs_longest(adjacents, dfs_from, dfs_to, visited=None):
    if visited is None:
        visited = set()

    dist = 0
    for neighbour in adjacents[dfs_from]:
        # stopping any potential loops
        if neighbour in visited:
            continue
        # base case
        if neighbour == dfs_to:
            return adjacents[dfs_from][dfs_to]
        # standard recursion
        visited.add(neighbour)
        dist = max(dist, adjacents[dfs_from][neighbour] + dfs_longest(adjacents, neighbour, dfs_to, visited=visited))
        visited.remove(neighbour)
    return dist


if __name__ == "__main__":
    main()
