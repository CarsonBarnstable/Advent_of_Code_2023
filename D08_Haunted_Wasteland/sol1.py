def main():
    path_to_from = ("AAA", "ZZZ")
    paths = {}

    # getting file input
    with open("input.txt") as f:
        choices = f.readline().strip()
        f.readline()  # empty line
        for line in f.readlines():
            # Format:  ||GXF = (XQB, GFH)||
            line = line.strip('\n').strip(')').split(" = (")
            paths[line[0]] = tuple(line[1].split(", "))

    # traversing from AAA to ZZZ
    dist_count = 0
    current_ch = path_to_from[0]
    while current_ch != path_to_from[1]:
        direction = 0 if choices[dist_count % len(choices)] == 'L' else 1
        current_ch = paths[current_ch][direction]
        dist_count += 1

    # result
    print(dist_count)


if __name__ == "__main__":
    main()
