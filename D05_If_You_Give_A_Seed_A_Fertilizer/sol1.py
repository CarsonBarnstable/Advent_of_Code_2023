def main():
    with open("input.txt") as f:
        # getting seeds
        seeds = get_seeds(f)
        f.readline()  # blank line

        # getting transformations
        transformations = []
        while f.readline():
            transformations.append(get_next_transform(f))

    # getting distances per seed
    distances = []
    for seed in seeds:
        updated_val = seed
        for transformation in transformations:
            updated_val = update_val_with_transformation(updated_val, transformation)
        distances.append(updated_val)

    # result
    print(min(distances))


def get_seeds(f):
    line = f.readline()
    line = line.split(":")[1].strip(' ').strip('\n')
    line = line.split(' ')
    line = [int(num) for num in line]
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
        if 0 < diff < transform[2]:
            return transform[0] + diff
    return value


if __name__ == "__main__":
    main()
