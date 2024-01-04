def main():
    # variables
    n_steps = 64
    start, present, expanding = 'S', 'O', 'X'
    allowed, blocked = '.', '#'
    valid_steps = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    # getting input into standard grid
    grid = get_grid()

    # finding start position (location of 'S')
    start_pos = get_pos_of(grid, start)
    # performing step expanding
    grid = perform_steps(grid, present, expanding, allowed, blocked, valid_steps, start_pos=start_pos, steps=n_steps)

    # part 1 solution - counting number of steps
    print("Part 1:", sum(sum(1 if c == present else 0 for c in row) for row in grid))


def get_grid(file="input.txt"):
    grid = []
    with open(file) as f:
        for line in f.readlines():
            grid.append([symbol for symbol in line.strip('\n')])
    return grid


def get_pos_of(grid, symbol):
    r = [r.count(symbol) for r in grid].index(1)
    c = grid[r].index(symbol)
    return r, c


def perform_steps(grid, present, expanding, allowed, blocked, valid_steps, start_pos=(0, 0), steps=1):
    # adjusting to turn start position into "first valid step"
    grid[start_pos[0]][start_pos[1]] = present
    # then performing steps
    for _ in range(steps):
        indicate_possible_steps(grid, present, expanding, blocked, valid_steps)
        grid = hide_old_steps(grid, present, allowed)
        grid = relabel_new_steps(grid, expanding, present)
    return grid


def indicate_possible_steps(grid, old, new, wall, moves):
    rows, cols = len(grid), len(grid[-1])
    # going through all the cells
    for r_i, row in enumerate(grid):
        for c_i, char in enumerate(row):
            if char == old:
                # trying all possible steps
                for cr, cc in moves.values():
                    n_r, n_c = r_i+cr, c_i+cc
                    if n_r in range(rows) and n_c in range(cols):
                        # update only if not a wall
                        if grid[n_r][n_c] != wall:
                            grid[n_r][n_c] = new
    # fully adjusted grid
    return grid


def hide_old_steps(grid, old, ground):
    return [[c.replace(old, ground) for c in row] for row in grid]


def relabel_new_steps(grid, possible, confirmed):
    return [[c.replace(possible, confirmed) for c in row] for row in grid]


if __name__ == "__main__":
    main()
