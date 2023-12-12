def main():
    # controlling vars
    galaxy_char = '#'
    galaxy_extra = 2-1

    # taking in input
    grid = []
    with open("input.txt") as f:
        for line in f.readlines():
            grid.append([char for char in line.strip('\n')])

    # determining breaks & noting galaxy positions
    galaxy_positions = []
    empty_rows, empty_cols = set(range(len(grid))), set(range(len(grid[0])))
    for row_num, row in enumerate(grid):
        for col_num, char in enumerate(row):
            if char == galaxy_char:
                # expansion breaks
                if row_num in empty_rows:
                    empty_rows.remove(row_num)
                if col_num in empty_cols:
                    empty_cols.remove(col_num)
                # noting galaxy positions
                galaxy_positions.append((row_num, col_num))

    # determining distances (w/ expansion)
    dist_sum = 0
    for index, (end_r, end_c) in enumerate(galaxy_positions):
        for start_r, start_c in galaxy_positions[index:]:
            dist = 0
            # rearranging for ordered comparisons
            s_r, e_r = (start_r, end_r) if start_r <= end_r else (end_r, start_r)
            s_c, e_c = (start_c, end_c) if start_c <= end_c else (end_c, start_c)
            # adding distances
            dist += abs(end_r-start_r) + abs(end_c-start_c)  # taxicab metric
            dist += galaxy_extra * len([extra_row for extra_row in empty_rows if extra_row in range(s_r, e_r+1)])
            dist += galaxy_extra * len([extra_col for extra_col in empty_cols if extra_col in range(s_c, e_c+1)])
            dist_sum += dist
            # print(s_r, s_c, e_r, e_c, dist, "(", abs(end_r-start_r), abs(end_c-start_c), ")  (", len([extra_row for extra_row in empty_rows if extra_row in range(s_r, e_r)]), len([extra_col for extra_col in empty_cols if extra_col in range(s_c, e_c)]), ")")

    # result
    print(dist_sum)


if __name__ == "__main__":
    main()
