rollable, stationary, blank = 'O', '#', '.'


def main():
    # getting input
    platform = []
    with open("input.txt") as f:
        for line in f.readlines():
            platform.append([cell for cell in line.strip('\n')])

    # updaing plaform roll
    platform = do_roll(platform, "N")

    # calculating platform load
    platform_load = get_load(platform)

    # result
    print(platform_load)


def do_roll(platform, direction):
    # using grid flips to always only have to roll east
    if direction == "N":
        # requires transpose then horizontal flip
        return transposed(h_flipped(roll_east(h_flipped(transposed(platform)))))
    if direction == "S":
        # transpose only
        return transposed(roll_east(transposed(platform)))
    if direction == "E":
        # base case
        return roll_east(platform)
    if direction == "W":
        # just horizontal flip
        return h_flipped(roll_east(h_flipped(platform)))


def roll_east(platform):
    rolled_platform = []
    for line in platform:
        rolled_platform.append(line_roll_east(line))
    return rolled_platform


def line_roll_east(line):
    # split on immovable rocks
    segments = "".join(line).split(stationary)
    # sends rollable rocks to right
    segments = [sorted(seg) for seg in segments]

    # rejoin
    reconstructed = []
    for seg in segments:
        for char in seg:
            reconstructed.append(char)
        reconstructed.append(stationary)
    reconstructed.pop()  # removing spare immovable rock

    return reconstructed


def h_flipped(platform):
    return [line[::-1] for line in platform]


def transposed(platform):
    return [list(cols) for cols in zip(*platform)]


def print_platform(platform):
    for line in platform:
        print("".join(line))


def get_load(platform):
    load = 0
    for i, line in enumerate(platform[::-1]):
        load += (i+1) * "".join(line).count(rollable)
    return load


if __name__ == "__main__":
    main()
