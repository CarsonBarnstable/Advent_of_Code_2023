def main():
    lines = []
    with open("input.txt") as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))
    print(lines)


if __name__ == "__main__":
    main()
