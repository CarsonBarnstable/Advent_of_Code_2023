def main():
    gear = '*'

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
            if char == gear:
                locations.add((row_n, col_n))

    # finding and summing surrounding numbers
    gear_ratios = set()
    bounds_row, bounds_col = range(0, len(grid)), range(0, len(grid[0]))
    for y_c, x_c in locations:
        gear_ratio = 1
        gear_count = 0
        coords = []

        for y, x in [(y_c + i, x_c + j) for i in (-1, 0, 1) for j in (-1, 0, 1)]:
            if y in bounds_row and x in bounds_col and grid[y][x].isdigit():  # valid numberical surrounding cells
                left, right = x, x

                # finding bounds of num
                while left-1 in bounds_col and grid[y][left-1].isdigit():
                    left -= 1
                while right+1 in bounds_col and grid[y][right+1].isdigit():
                    right += 1

                # forming number and adding to sum (if not already added)
                if gear_count < 2 and (left, y) not in coords:
                    gear_ratio *= int("".join(grid[y][left:right+1]))
                    coords.append((left, y))
                    gear_count += 1

        # only adding applicable gears
        if gear_count == 2:
            gear_ratios.add((gear_ratio, y_c, x_c))

    # result
    ratio_sum = 0
    for ratio in gear_ratios:
        ratio_sum += ratio[0]
    print(ratio_sum)


if __name__ == "__main__":
    main()
