def main():
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
    # print_reflections(grids, horizontal_reflections, vertical_reflections)

    # computing sums and resultand
    h_sum = sum(horizontal_reflections)
    v_sum = sum(vertical_reflections)
    resultand = 100*h_sum + v_sum
    print(resultand)


def get_horiz_reflection(grid):
    reflection = 0
    for cutoff in range(1, len(grid[0])):
        minlen = min(cutoff, len(grid[0])-cutoff)
        valid = True
        for i, row in enumerate(grid):
            left_seq = row[cutoff-1:cutoff-minlen-1:-1] if (cutoff-minlen != 0) else row[cutoff-1::-1]
            right_seq = row[cutoff:cutoff+minlen:1]
            if left_seq != right_seq:
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
