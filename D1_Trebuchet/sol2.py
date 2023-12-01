def main():
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    summ = 0
    with open("input.txt") as f:
        for line in f.readlines():
            sub_int = 0
            line = line.strip("\n")
            
            # forward
            for cutoff in range(len(line)):
                in_list = [num in line[0:cutoff] for num in nums]
                if any(in_list):
                    sub_int += in_list.index(True)
                    break
                elif line[cutoff].isdigit():
                    sub_int += int(line[cutoff])
                    break
            sub_int *= 10
            # backward
            for cutoff in reversed(range(len(line))):
                in_list = [num in line[cutoff:] for num in nums]
                if any(in_list):
                    sub_int += in_list.index(True)
                    break
                elif line[cutoff].isdigit():
                    sub_int += int(line[cutoff])
                    break
            summ += sub_int

    print(summ)  # solution


if __name__ == "__main__":
    main()
