def main():
    path_ends_to_from = ("A", "Z")
    paths = {}

    # getting file input
    with open("input.txt") as f:
        choices = f.readline().strip()
        f.readline()  # empty line
        for line in f.readlines():
            # GXF = (XQB, GFH)
            line = line.strip('\n').strip(')').split(" = (")
            paths[line[0]] = tuple(line[1].split(", "))

    # getting notes to traverse
    simultaneous_paths = []
    for start in paths.keys():
        if start.endswith(path_ends_to_from[0]):
            simultaneous_paths.append(start)

    # traverse from **A to *Z
    dist_counts = []
    current_positions = simultaneous_paths
    for index, start in enumerate(current_positions):
        dist_counts.append(0)
        current_pos = start
        while not current_pos[2] == path_ends_to_from[1]:
            direction = 0 if choices[dist_counts[index] % len(choices)] == 'L' else 1
            current_pos = paths[current_pos][direction]
            dist_counts[index] += 1
        current_positions[index] = current_pos

    # calculating LCM
    lcm = 1
    for dist in dist_counts:
        lcm = get_lcm(lcm, dist)

    # result
    print("Result is LCM of following path lengths:")
    print(dist_counts)
    print("LCM:", lcm)


# helper LCM function
def get_lcm(x, y):
    return abs(x * y) // get_gcd(x, y)


# helper GCD function
def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


if __name__ == "__main__":
    main()
