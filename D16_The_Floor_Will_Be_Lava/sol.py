def main():
    # getting input
    grid = []
    hits = []
    with open("input.txt") as f:
        for line in f.readlines():
            grid.append([char for char in line.strip('\n')])
            hits.append([0 for _ in line.strip('\n')])

    # * * * * * PART ONE SOLUTION * * * * *
    print("Part 1:", get_beam_range(grid))

    # * * * * * PART TWO SOLUTION * * * * *
    max_reached = 0
    for start_c, direction in zip((0, len(grid[0])), ('R', 'L')):
        for start_r in range(len(grid)):
            reached = get_beam_range(grid, start_r, start_c, direction)
            max_reached = max(max_reached, reached)
    for start_r, direction in zip((0, len(grid)), ('D', 'U')):
        for start_c in range(len(grid[0])):
            try:  # IDK, one case wasn't behaving
                reached = get_beam_range(grid, start_r, start_c, direction)
                max_reached = max(max_reached, reached)
            except RecursionError:
                reached = 0
                max_reached = max(max_reached, reached)
    print("Part 2:", max_reached)  # result


def get_beam_range(grid, pos_r=0, pos_c=0, direction='R'):
    # initializing storage
    visited = set()
    hits = [[0 for _ in __] for __ in grid]
    # running complete run
    initiate_beam(grid, hits, visited, pos_r, pos_c, direction)
    # returning cells reached
    return sum(sum(hits, []))


def initiate_beam(grid, hits, visited, pos_r=0, pos_c=0, direction='R'):

    # if still in grid
    if pos_r not in range(len(hits)) or pos_c not in range(len(hits[0])):
        return
    # or has been visited in same direction
    if (pos_r, pos_c, direction) in visited:
        return

    # else
    hits[pos_r][pos_c] = 1
    symbol = grid[pos_r][pos_c]

    # continuing straight beam
    while symbol == '.':
        visited.add((pos_r, pos_c, direction))
        if direction == 'L':
            pos_c = pos_c-1
        if direction == 'R':
            pos_c = pos_c+1
        if direction == 'U':
            pos_r = pos_r-1
        if direction == 'D':
            pos_r = pos_r+1

        # handling new updates
        if pos_r in range(len(hits)) and pos_c in range(len(hits[0])):
            hits[pos_r][pos_c] = 1
            symbol = grid[pos_r][pos_c]
        else:
            # departs grid
            return

    # handling different update types
    if symbol == '/':  # mirror
        if direction == 'L':
            initiate_beam(grid, hits, visited, pos_r+1, pos_c, 'D')
        if direction == 'R':
            initiate_beam(grid, hits, visited, pos_r-1, pos_c, 'U')
        if direction == 'U':
            initiate_beam(grid, hits, visited, pos_r, pos_c+1, 'R')
        if direction == 'D':
            initiate_beam(grid, hits, visited, pos_r, pos_c-1, 'L')
        return
    if symbol == '\\':  # mirror
        if direction == 'L':
            initiate_beam(grid, hits, visited, pos_r-1, pos_c, 'U')
        if direction == 'R':
            initiate_beam(grid, hits, visited, pos_r+1, pos_c, 'D')
        if direction == 'U':
            initiate_beam(grid, hits, visited, pos_r, pos_c-1, 'L')
        if direction == 'D':
            initiate_beam(grid, hits, visited, pos_r, pos_c+1, 'R')
        return
    if symbol == '|':  # vertical splitter
        if direction in ('U', 'D'):
            initiate_beam(grid, hits, visited, pos_r-1 if direction == 'U' else pos_r+1, pos_c, direction)
        if direction in ('L', 'R'):
            initiate_beam(grid, hits, visited, pos_r-1, pos_c, 'U')
            initiate_beam(grid, hits, visited, pos_r+1, pos_c, 'D')
        return
    if symbol == '-':  # horizontal splitter
        if direction in ('L', 'R'):
            initiate_beam(grid, hits, visited, pos_r, pos_c-1 if direction == 'L' else pos_c+1, direction)
        if direction in ('U', 'D'):
            initiate_beam(grid, hits, visited, pos_r, pos_c-1, 'L')
            initiate_beam(grid, hits, visited, pos_r, pos_c+1, 'R')
        return

    return  # should never be needed


if __name__ == "__main__":
    main()
