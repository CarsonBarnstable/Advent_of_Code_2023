def main():
    chosen_jump_factor = 1000

    with open("input.txt") as f:
        # getting seeds
        seeds = get_seeds(f)
        f.readline()  # blank line

        # getting transformations
        transformations = []
        while f.readline():
            transformations.append(get_next_transform(f))

    # getting distances per seed
    min_distance, min_seed = find_mins_from_seed_transform(seeds, transformations, jump_factor=chosen_jump_factor)

    # repeating on closest range
    min_distance, min_seed = find_mins_from_seed_transform(seeds, transformations, guess=min_seed)

    # result
    print("Distance:", min_distance)
    print(" w/ Seed:", min_seed)


def get_seeds(f):
    line = f.readline()
    line = line.split(":")[1].strip(' ').strip('\n')
    line = line.split(' ')
    line = [(int(line[2*index]), int(line[2*index+1])) for index in range(len(line)//2)]
    return line


def get_next_transform(f):
    transform = []
    while True:
        # getting line and breaking if break
        line = f.readline()
        line = line.strip('/n')
        line = [num for num in line.strip('\n').split(' ')]
        # only adding if 3-part num line
        if len(line) == 3:
            line = [int(num) for num in line]
            transform.append(line)
        else:
            return transform


def update_val_with_transformation(value, transformation):
    for transform in transformation:
        diff = value - transform[1]
        if 0 <= diff < transform[2]:
            return transform[0] + diff
    return value


def find_mins_from_seed_transform(seeds, transformations, guess=-1, jump_factor=10000):
    min_distance = -1
    min_seed = -1

    for seed in seeds:
        # adjusting range
        if guess == -1:
            broad_range = range(seed[0], seed[0]+seed[1], jump_factor)
        else:
            broad_range = range(guess-jump_factor, guess+jump_factor, 1)

        # iterating through range
        for new_seed in broad_range:
            updated_val = new_seed
            for transformation in transformations:
                updated_val = update_val_with_transformation(updated_val, transformation)
            # updating min distance
            if min_distance == -1:
                min_distance = updated_val
                min_seed = new_seed
            if min_distance != min(min_distance, updated_val):
                min_distance = min(min_distance, updated_val)
                min_seed = new_seed
    # final return
    return min_distance, min_seed


if __name__ == "__main__":
    main()
