X, Y, Z = 'x', 'y', 'z'


def main():
    # getting pre-arranged input
    blocks = sorted_block_input("input.txt")

    # applying gravity
    dropped_blocks = apply_gravity_to(blocks)

    # calculating part 1 value
    critical_counter = 0
    for block in dropped_blocks:
        critical_counter += 1 if len(blocks_only_supported_by(dropped_blocks, block)) == 0 else 0
    print("Part 1:", critical_counter)

    # calculating part 2 value
    chain_react_counter = 0
    print("This will take a few min...")
    for i, base_block in enumerate(dropped_blocks):
        chain_react_counter += get_waterfalling(base_block, dropped_blocks)
    print("Part 2:", chain_react_counter)


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
    new_block = []
    for sub_block in full_block:
        new_dict = {}
        for d in sub_block.keys():
            new_dict[d] = sub_block[d]+dist if d == dim else sub_block[d]
        new_block.append(new_dict)
    return tuple(new_block)


def coords_of(block):
    return tuple(block.values())


def apply_gravity_to(floating_blocks):
    resting_mass = set()
    sitting_blocks = []
    for i, full_block in enumerate(floating_blocks):
        # incrementing down until intersection...
        while not any(coords_of(block) in resting_mass or block[Z] <= 0 for block in full_block):
            full_block = block_moved(full_block, Z, -1)
        full_block = block_moved(full_block, Z, 1)  # then bumping back up

        # then adding block to bottom (unmoving) mass
        for sub_block in full_block:
            resting_mass.add(coords_of(sub_block))
        sitting_blocks.append(full_block)
    return sitting_blocks


def blocks_only_supported_by(all_blocks, supporting_block, invisible_coords=None):
    if invisible_coords is None:
        invisible_coords = []

    # creating note of "total mass of all blocks"
    solely_supported, entire_mass = [], set()
    for block in all_blocks:
        for sub_block in block:
            entire_mass.add(coords_of(sub_block))
    # then doing logic
    for complete_block in all_blocks:
        support_blocks = []
        # taking note of all blocks that support 'complete block'
        one_down_block = block_moved(complete_block, Z, -1)
        if all(one_down_block[-1][Z] == odb[Z] for odb in one_down_block):  # horizontal
            for single_block in one_down_block:
                if coords_of(single_block) in entire_mass:
                    support_blocks.append(coords_of(single_block))
        else:  # vertical blocks (only need to check bottom block)
            support_blocks.append(min(coords_of(lb) for lb in one_down_block))
        # checking to see if condition still holds
        if support_blocks and all(supported_by in [coords_of(supporting) for supporting in supporting_block] or supported_by in invisible_coords for supported_by in support_blocks):
            solely_supported.append(complete_block)
    return solely_supported


def get_waterfalling(base_block, dropped_blocks):
    to_drop = [base_block]
    all_dropped = set()
    all_dropped.add(dropped_blocks.index(base_block))
    while to_drop:
        invisible = []
        for block_i in all_dropped:
            invisible += [coords_of(block) for block in dropped_blocks[block_i]]
        single_dropped = blocks_only_supported_by(dropped_blocks, to_drop.pop(0), invisible_coords=invisible)
        for drop in all_dropped:
            if drop in single_dropped:
                single_dropped.remove(drop)
        to_drop += [drop for drop in single_dropped]
        old_dropped = set([a for a in all_dropped])
        for drop in single_dropped:
            all_dropped.add(dropped_blocks.index(drop))
        if old_dropped == all_dropped:
            break

    all_dropped.remove(dropped_blocks.index(base_block))
    return len(all_dropped)


if __name__ == "__main__":
    main()
