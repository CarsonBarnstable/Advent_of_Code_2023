rollable, stationary, blank = 'O', '#', '.'


def main():
    # getting input
    platform = []
    with open("input.txt") as f:
        for line in f.readlines():
            platform.append([cell for cell in line.strip('\n')])

    # - - - - - PART ONE - - - - -

    # updaing plaform roll
    platform = do_roll(platform, "N")
    # calculating platform load
    platform_load = get_load(platform)
    # result (Part 1)
    print("P1:", platform_load)

    # - - - - - PART TWO - - - - -

    # spinning should be repetetive, finding cycle length
    starting_buffer = len(platform)*2  # could likely be lower, but works
    cycle_length = get_spin_cycle_len(platform, initialize=starting_buffer)

    # spinning 1000000000 (kinda) times:
    for _ in range(1000000000 % cycle_length + cycle_length*starting_buffer):
        # should have just remembered from within spin_cycle iterations
        platform = do_spin(platform)

    # recalculating platform load
    platform_load = get_load(platform)
    # result (Part 2)
    print("P2:", platform_load)


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


def do_spin(platform):
    for direction in ("N", "W", "S", "E"):
        platform = do_roll(platform, direction)
    return platform


def get_spin_cycle_len(platform, initialize=12):
    # initializing into "steady state"
    for _ in range(initialize):
        platform = do_spin(platform)
    new_platform = do_spin(platform)

    # finding pattern length
    rep_index = 1
    while platform != new_platform:
        new_platform = do_spin(new_platform)
        rep_index += 1
        if rep_index % 100 == 0:
            print(rep_index)
            print_platform(new_platform)
            print()
    return rep_index


if __name__ == "__main__":
    main()
