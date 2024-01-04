def main():
    # variables
    n_steps, n_steps_revised = 1, 26501365
    start, present, expanding = 'S', 'O', 'X'
    allowed, blocked = '.', '#'
    valid_steps = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    # getting input into standard grid
    grid = get_grid()

    # finding start position (location of 'S')
    start_pos = get_pos_of(grid, start)
    # performing step expanding
    default_step_info = (grid, present, expanding, allowed, blocked, valid_steps)
    reached = perform_steps(*default_step_info, start_pos=start_pos, steps=n_steps)

    # part 1 solution - counting number of steps
    print("Part 1:", reached, "\n")

    # part 2 brainstorming
    """
    I can't help but notice that there is a diagonal completely open between all "edge centeres"
    As well as a "open line of sight" between each edge center
    Thus, the extreme expansion will be able to expand towards neighbor edges at max speed (no barriers)
    
    I also know that once a grid is "maximally filled", it will just oscillate between two states...
    where the deciding factor of # of valid locations is which "parity" (odd/even) we end on
    Furthermore, because the grid is 131x131 (odd edge), adjacent "maps" will have opposite "parity"
    
    Thus, we will have giant diamond, with grid of odd/even parity grids, plus outer edge
    Which will look something like diagram below
    
    .....|.....|.....
    .....|..#..|.....
    ....o|.#.o.|o....
    -----+-----+-----
    ...o.|#.o##|.o...
    ..#.o|.o.o.|o.o..
    ...o.|##o.o|.#...
    -----+-----+-----
    ....#|.o.##|o....
    .....|..o..|.....
    .....|.....|.....
    """

    print("* * * * * Part 2 Logic Work * * * * *")
    print("Width/Height of Single Grid:", len(grid))
    print("Number of cells Reached Horizontally:", n_steps_revised//len(grid)-1)
    cells_reached = n_steps_revised//len(grid) - 1
    print("Number of \"Odd Parity\" Full Grids:")
    print(" = 1+9+25+49+...", cells_reached//2, "times")
    print(" =", ((cells_reached//2)*2 + 1) ** 2)
    print("Number of \"Even Parity\" Full Grids:")
    print(" = 0+4+16+36+...", cells_reached//2, "times")
    print(" =", (((cells_reached+1)//2)*2) ** 2)
    # important numbers
    odd_filled, even_filled = ((cells_reached//2)*2 + 1) ** 2, (((cells_reached+1)//2)*2) ** 2
    odd_count = perform_steps(*default_step_info, start_pos=start_pos, steps=524+1)
    even_count = perform_steps(*default_step_info, start_pos=start_pos, steps=524)
    print("Total for \"Fully Filled Grid\":")
    print(" = odd_filled * odd_count  +  even_filled * even_count")
    print(" =", odd_filled, "*", odd_count, " + ", even_filled, "*", even_count)
    print(" =", odd_filled*odd_count + even_filled*even_count)

    print(" * * NOW JUST NEED TO WORRY ABOUT EDGES * *")
    # corner cases
    corner_steps = n_steps_revised - len(grid)//2-1 - cells_reached*len(grid)
    print("Will have 4 corners, filled with", corner_steps, "steps from their respective edge")
    # doing the math
    top = perform_steps(*default_step_info, start_pos=(len(grid)-1, len(grid)//2), steps=corner_steps)
    bottom = perform_steps(*default_step_info, start_pos=(0, len(grid)//2), steps=corner_steps)
    left = perform_steps(*default_step_info, start_pos=(len(grid)//2, len(grid)-1), steps=corner_steps)
    right = perform_steps(*default_step_info, start_pos=(len(grid)//2, 0), steps=corner_steps)
    print("  Which gets us the following \"coverages\":")
    print("  Top:", top)
    print("  Bottom:", bottom)
    print("  Left:", left)
    print("  Right:", right)
    print("Adding the \"Stable Centers\" and Corners thus gets us a total of:",
          odd_filled*odd_count + even_filled*even_count + top + bottom + left + right)

    # edge cases
    print("Will have 4 Edges, with alternating \"Mostly Filled\" and \"Hardly Filled\" Edges")
    print("There will be 'cells_reached+1' hardly-filled, and 'cells_reached' mostly-filled Edges")
    print("  Where 'mostly filled' must endure len(grid) * 3 // 2 - 1 more steps")
    print("  Where 'hardly filled' must endure len(grid) // 2 - 1 more steps")
    # doing the math
    mostly_count, hardly_count = cells_reached, cells_reached+1
    mostly_steps, hardly_steps = len(grid)*3//2-1, len(grid)//2-1
    tr_hardly = perform_steps(*default_step_info, start_pos=(len(grid)-1, 0), steps=hardly_steps)
    tl_hardly = perform_steps(*default_step_info, start_pos=(len(grid)-1, len(grid)-1), steps=hardly_steps)
    br_hardly = perform_steps(*default_step_info, start_pos=(0, 0), steps=hardly_steps)
    bl_hardly = perform_steps(*default_step_info, start_pos=(0, len(grid)-1), steps=hardly_steps)
    tr_mostly = perform_steps(*default_step_info, start_pos=(len(grid)-1, 0), steps=mostly_steps)
    tl_mostly = perform_steps(*default_step_info, start_pos=(len(grid)-1, len(grid)-1), steps=mostly_steps)
    br_mostly = perform_steps(*default_step_info, start_pos=(0, 0), steps=mostly_steps)
    bl_mostly = perform_steps(*default_step_info, start_pos=(0, len(grid)-1), steps=mostly_steps)
    print("This results in the following \"Reached\" numbers")
    print("  tr_hardly:", tr_hardly)
    print("  tl_hardly:", tl_hardly)
    print("  br_hardly:", br_hardly)
    print("  bl_hardly:", bl_hardly)
    print("  tr_mostly:", tr_mostly)
    print("  tl_mostly:", tl_mostly)
    print("  br_mostly:", br_mostly)
    print("  bl_mostly:", bl_mostly)
    print()
    print("This results in a SUM TOTAL SUM of:",
          odd_filled*odd_count + even_filled*even_count
          + top + bottom + left + right
          + mostly_count * (tr_mostly+tl_mostly+br_mostly+bl_mostly)
          + hardly_count * (tr_hardly+tl_hardly+br_hardly+bl_hardly)
          )

    print("Wow.")


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
    return sum(sum(1 if c == present else 0 for c in row) for row in grid)


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
