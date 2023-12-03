def main():
    sep = '.'

    # getting input "grid"
    grid = []
    with open("input.txt") as f:
        for line in f.readlines():
            row = []
            for char in line.strip():
                row.append(char)
            grid.append(row)

    # finding symbol locations
    locations = set()  # set of symbol coordinates
    for row_n, row in enumerate(grid):
        for col_n, char in enumerate(row):
            if not (char.isdigit() or char == sep):
                locations.add((row_n, col_n))

    # finding and summing surrounding numbers
    part_nums = set()
    bounds_row, bounds_col = range(0, len(grid)), range(0, len(grid[0]))
    for y_c, x_c in locations:
        for y, x in [(y_c + i, x_c + j) for i in (-1, 0, 1) for j in (-1, 0, 1)]:
            if y in bounds_row and x in bounds_col and grid[y][x].isdigit():  # valid numberical surrounding cells
                left, right = x, x
                # finding bounds of num
                while left-1 in bounds_col and grid[y][left-1].isdigit():
                    left -= 1
                while right+1 in bounds_col and grid[y][right+1].isdigit():
                    right += 1
                # forming number and adding to sum
                num = int("".join(grid[y][left:right+1]))
                part_nums.add((num, y, left))

    # result
    part_num_sum = 0
    for num_det in part_nums:
        part_num_sum += num_det[0]
    print(part_num_sum)


if __name__ == "__main__":
    main()
