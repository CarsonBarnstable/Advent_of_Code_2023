def main():
    summ = 0
    with open("input.txt") as f:
        for line in f.readlines():
            sub_int = 0
            for _ in range(2):
                sub_int *= 10
                for index, char in enumerate(line):
                    if char.isdigit():
                        sub_int += int(char)
                        line = line[::-1]  # reverse line
                        break
            summ += sub_int

    print(summ)


if __name__ == "__main__":
    main()
