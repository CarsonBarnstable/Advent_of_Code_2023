X, Y, Z = 'x', 'y', 'z'


def main():
    # getting pre-arranged input
    blocks = sorted_block_input()

    # applying gravity
    dropped_blocks = apply_gravity_to(blocks)
    for block in dropped_blocks:
        print(block)


def sorted_block_input(file="input.txt"):
    # getting input
    block_ends = []
    with open(file) as f:
        for line in f.readlines():
            end1, end2 = line.strip('\n').split('~')
            end1cc, end2cc = end1.split(','), end2.split(',')
            end1cc = {'x': int(end1cc[0]), 'y': int(end1cc[1]), 'z': int(end1cc[2])}
            end2cc = {'x': int(end2cc[0]), 'y': int(end2cc[1]), 'z': int(end2cc[2])}
            block_ends.append((end1cc, end2cc))

    # "extending" blocks
    block_blocks = []
    for e1, e2 in block_ends:
        block_pieces = []
        if e1[Y] == e2[Y] and e1[Z] == e2[Z]:  # aligned with x
            block_pieces = [{X: x, Y: e1[Y], Z: e1[Z]} for x in range(min(e1[X], e2[X]), max(e1[X], e2[X])+1)]
        if e1[X] == e2[X] and e1[Z] == e2[Z]:  # aligned with y
            block_pieces = [{X: e1[X], Y: y, Z: e1[Z]} for y in range(min(e1[Y], e2[Y]), max(e1[Y], e2[Y])+1)]
        if e1[X] == e2[X] and e1[Y] == e2[Y]:  # vertical (aligned with z)
            block_pieces = [{X: e1[X], Y: e1[Y], Z: z} for z in range(min(e1[Z], e2[Z]), max(e1[Z], e2[Z])+1)]
        block_blocks.append(tuple(block_pieces))

    # sorting all blocks by lowest z height
    block_blocks.sort(key=lambda x: min(c[Z] for c in x))
    return block_blocks


def block_moved(full_block, dim, dist):
    for individual_block in full_block:
        individual_block[dim] += dist
    return full_block


def apply_gravity_to(floating_blocks):
    resting_mass = set()
    sitting_blocks = []
    for i, full_block in enumerate(floating_blocks):
        # incrementing down until intersection...
        while not any(tuple(coords.values()) in resting_mass or coords[Z] <= 0 for coords in full_block):
            full_block = block_moved(full_block, Z, -1)
        full_block = block_moved(full_block, Z, 1)  # then bumping back up

        # then adding block to bottom (unmoving) mass
        for sub_block in full_block:
            resting_mass.add(tuple(sub_block.values()))
        sitting_blocks.append(full_block)
    return sitting_blocks


if __name__ == "__main__":
    main()
