def main():
    # getting input
    grid_cells = []
    with open("input.txt") as f:
        for line in f.readlines():
            grid_cells.append([c for c in line.strip('\n')])
    bounds_r, bounds_c = range(len(grid_cells)), range(len(grid_cells[0]))

    # determining start pos
    start_pos = (-1, -1)  # backup
    for r_i, row in enumerate(grid_cells):
        for c_i, char in enumerate(row):
            if char == "S":
                start_pos = (r_i, c_i)

    # ensuring something was found
    if start_pos == (-1, -1):
        return

    # initializing loop list and finding "initiation direction"
    loop_coords = [start_pos, find_start_neighbor(start_pos, bounds_r, bounds_c, grid_cells)]

    # making and tracking loop
    while loop_coords[-1] != start_pos:
        new_r, new_c = find_next_pos(loop_coords[-1], loop_coords[-2], bounds_r, bounds_c, grid_cells)
        loop_coords.append((new_r, new_c))

    # result is half of loop length
    print(len(loop_coords)//2)


def find_start_neighbor(start_pos, bounds_r, bounds_c, grid):
    new_r, new_c = start_pos[0]-1, start_pos[1]  # above start
    if new_r in bounds_r and new_c in bounds_c:
        if grid[new_r][new_c] in {'|', '7', 'F'}:
            return new_r, new_c

    new_r, new_c = start_pos[0]+1, start_pos[1]  # below start
    if new_r in bounds_r and new_c in bounds_c:
        if grid[new_r][new_c] in {'|', 'L', 'J'}:
            return new_r, new_c

    new_r, new_c = start_pos[0], start_pos[1]-1  # left of start
    if new_r in bounds_r and new_c in bounds_c:
        if grid[new_r][new_c] in {'-', 'L', 'F'}:
            return new_r, new_c

    new_r, new_c = start_pos[0], start_pos[1]+1  # right of start
    if new_r in bounds_r and new_c in bounds_c:
        if grid[new_r][new_c] in {'-', '7', 'J'}:
            return new_r, new_c


def find_next_pos(current, previous, bounds_r, bounds_c, grid):
    new_r, new_c = current[0]-1, current[1]  # above current
    if new_r in bounds_r and new_c in bounds_c:
        if grid[current[0]][current[1]] in {'|', 'L', 'J'}:
            if grid[new_r][new_c] in {'|', '7', 'F', 'S'}:
                if (new_r, new_c) != previous:
                    return new_r, new_c

    new_r, new_c = current[0]+1, current[1]  # below current
    if new_r in bounds_r and new_c in bounds_c:
        if grid[current[0]][current[1]] in {'|', '7', 'F'}:
            if grid[new_r][new_c] in {'|', 'L', 'J', 'S'}:
                if (new_r, new_c) != previous:
                    return new_r, new_c

    new_r, new_c = current[0], current[1]-1  # left of current
    if new_r in bounds_r and new_c in bounds_c:
        if grid[current[0]][current[1]] in {'-', '7', 'J'}:
            if grid[new_r][new_c] in {'-', 'L', 'F', 'S'}:
                if (new_r, new_c) != previous:
                    return new_r, new_c

    new_r, new_c = current[0], current[1]+1  # right of current
    if new_r in bounds_r and new_c in bounds_c:
        if grid[current[0]][current[1]] in {'-', 'L', 'F'}:
            if grid[new_r][new_c] in {'-', '7', 'J', 'S'}:
                if (new_r, new_c) != previous:
                    return new_r, new_c


if __name__ == "__main__":
    main()
