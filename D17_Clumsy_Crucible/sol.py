direction = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def main():
    # getting input
    grid = get_input_from("input.txt")





def get_input_from(filename):
    with open(filename) as f:
        lines = [line.strip('\n') for line in f.readlines()]
    return [[int(num) for num in line] for line in lines]


if __name__ == "__main__":
    main()
