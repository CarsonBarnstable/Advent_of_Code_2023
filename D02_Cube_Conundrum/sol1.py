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
            # determining if fair game
            if all(num <= max_allowed for num, max_allowed in zip(max_rgb.values(), [12, 13, 14])):
                sum_games += line_num+1  # adjusting for zero index
        print(sum_games)  # result


if __name__ == "__main__":
    main()
