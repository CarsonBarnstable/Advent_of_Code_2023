def main():
    cols = ("red", "green", "blue")
    sum_games = 0
    with open("input.txt") as f:
        for line_num, line in enumerate(f.readlines()):
            line = line.strip("\n").split(":")[1].split(";")  # separating out groups of pulls
            max_rgb = {col: 0 for col in cols}  # storing max pulles in a single pull

            # getting max pulled at once
            for phase in line:
                for color in phase.split(","):  # looking at one die color at a time
                    num_col = color.split(" ")[1:]
                    for col in cols:
                        if num_col[1] == col:  # updaing maximum
                            max_rgb[col] = max(max_rgb[col], int(num_col[0]))

            # summing power of min subes usable
            product = 1
            for max_used in max_rgb.values():
                product *= max_used
            sum_games += product

        print(sum_games)  # result


if __name__ == "__main__":
    main()
