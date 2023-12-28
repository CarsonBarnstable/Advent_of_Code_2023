import sys
sys.setrecursionlimit(500000)


moves = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}


def main():
    # getting inputs from file
    paths = []
    with open("input.txt") as f:
        for line in f.readlines():
            details = line.strip('\n').split(" ")
            entry = {"dir": details[0], "dist": int(details[1]), "hex": details[2].strip('(#').strip(')')}
            paths.append(entry)

    # # * * * * * * * * PART 1 SOLUTION * * * * * * * *
    #
    # # taking note of visited nodes
    # instructions = extract_instructions(paths, 1)
    # visited = get_visited(instructions)
    #
    # # flood fill starting at start
    # fill = set()
    # fill = flood_fill(visited, fill)
    # # union of inside and edge
    # complete_fill = fill | visited
    #
    # # part 1 solution
    # print("Part 1:", len(complete_fill))
    # # print_grid(complete_fill)

    for part in (1, 2):
        # taking note of visited nodes
        instructions = extract_instructions(paths, part)
        visited = get_visited(instructions)

        # flood fill starting at start
        fill = set()
        fill = flood_fill(visited, fill)
        # union of inside and edge
        complete_fill = fill | visited

        # solution
        print("Part", part, ":", len(complete_fill))
        # print_grid(complete_fill)


def extract_instructions(paths, part):
    instructions = []
    for path in paths:
        if part == 1:
            instructions.append({"dir": path["dir"], "dist": path["dist"]})
        if part == 2:
            instructions.append({"dir": "RDLU"[int(path["hex"][-1])], "dist": int(path["hex"][:5], 16)})
    return instructions


def get_visited(instructions, start=(0, 0)):
    visited = set()
    current_pos = start
    for instruction in instructions:
        shift = moves[instruction["dir"]]
        while instruction["dist"] > 0:
            visited.add(current_pos)
            current_pos = tuple([c+s for c, s in zip(current_pos, shift)])
            instruction["dist"] -= 1
    return visited


def print_grid(highlighted, highlight=(0, 0)):
    # getting bounds
    min_r, max_r = min(r for r, c in highlighted), max(r for r, c in highlighted)
    min_c, max_c = min(c for r, c in highlighted), max(c for r, c in highlighted)
    print(min_r, max_r, min_c, max_c)

    # printing grid
    for row in range(min_r, max_r+1):
        for col in range(min_c, max_c+1):
            if (row, col) == highlight:
                print('@', end="")
            elif (row, col) in highlighted:
                print('#', end="")
            else:
                print('.', end="")
        print()


def flood_fill(edge, fill):
    stack = [(0, 0)]
    while len(stack) > 0:
        pos = stack.pop()
        if pos in fill:
            continue
        fill.add(pos)
        for direction in "UDLR":
            new_pos = tuple([c+s for c, s in zip(pos, moves[direction])])
            if new_pos not in edge:
                stack.append(new_pos)
    return fill


if __name__ == "__main__":
    main()
