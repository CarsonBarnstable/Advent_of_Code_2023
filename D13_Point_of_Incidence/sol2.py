def main():
    ash, rock = '.', '#'
    printout_all = False

    # getting input
    grids = []
    with open("input.txt") as f:
        new_grid = []
        for line in f.readlines():
            if len(line) == 1:  # grid break
                grids.append(new_grid)
                new_grid = []
            else:  # extending current grid
                new_grid.append([char for char in line.strip('\n')])
        grids.append(new_grid)  # last one in file

    # transposing matrix (swapping rows/columns
    grids_transposed = []
    for grid in grids:
        grids_transposed.append([list(cols) for cols in zip(*grid)])

    # lines of reflection
    vertical_reflections, horizontal_reflections = [], []
    for grid, t_grid in zip(grids, grids_transposed):
        vertical_reflections.append(get_horiz_reflection(grid))
        horizontal_reflections.append(get_horiz_reflection(t_grid))

    # printout w/ lines
    if printout_all:
        print_reflections(grids, horizontal_reflections, vertical_reflections)

    # lines of reflection
    new_vertical_reflections, new_horizontal_reflections = [], []
    for grid, t_grid, old_vr, old_hr in zip(grids, grids_transposed, vertical_reflections, horizontal_reflections):

        # trying all possible smudges
        vertical_reflection, horizontal_reflection = 0, 0
        for pos_r in range(len(grid)):
            for pos_col in range(len(t_grid)):

                # adjusting to add smudge
                grid[pos_r][pos_col] = ash if grid[pos_r][pos_col] == rock else rock
                t_grid[pos_col][pos_r] = ash if t_grid[pos_col][pos_r] == rock else rock

                # finding new line of reflection
                vertical_reflection = max(vertical_reflection, get_horiz_reflection(grid, illegal=old_vr))
                horizontal_reflection = max(horizontal_reflection, get_horiz_reflection(t_grid, illegal=old_hr))

                # inverting to remove smudge
                grid[pos_r][pos_col] = ash if grid[pos_r][pos_col] == rock else rock
                t_grid[pos_col][pos_r] = ash if t_grid[pos_col][pos_r] == rock else rock

        # adding new reflections to lists
        new_vertical_reflections.append(vertical_reflection)
        new_horizontal_reflections.append(horizontal_reflection)

    # printout w/ lines
    if printout_all:
        print_reflections(grids, new_horizontal_reflections, new_vertical_reflections)

    # computing sums and resultand
    h_sum = sum(new_horizontal_reflections)
    v_sum = sum(new_vertical_reflections)
    resultand = 100*h_sum + v_sum
    print(resultand)  # result


def get_horiz_reflection(grid, illegal=0):
    reflection = 0
    for cutoff in range(1, len(grid[0])):
        minlen = min(cutoff, len(grid[0])-cutoff)
        valid = True
        for i, row in enumerate(grid):
            left_seq = row[cutoff-1:cutoff-minlen-1:-1] if (cutoff-minlen != 0) else row[cutoff-1::-1]
            right_seq = row[cutoff:cutoff+minlen:1]
            if left_seq != right_seq or cutoff == illegal:
                valid = False
                break
        if valid:
            reflection = cutoff
            break
    return reflection


def print_reflections(grids, h_reflections, v_reflections):
    for h, v, g in zip(h_reflections, v_reflections, grids):
        print("HOR: ", h, "  VER: ", v)
        for i, line in enumerate(g):
            if v == 0:
                if h == i:
                    print("-"*len(line))
                    print("-"*len(line))
                print("".join(line))
            if h == 0:
                letters = "".join(line)
                print(letters[:v] + '||' + letters[v:])
        print('\n')


if __name__ == "__main__":
    main()
