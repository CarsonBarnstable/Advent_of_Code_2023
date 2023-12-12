def main():
    # this will not work in any holiday timeframe

    # parsing input file
    problems = []
    with open("mini_input.txt") as f:
        for line in f.readlines():
            line = line.strip('\n').split(' ')
            symbols = [char for char in line[0]]
            nums = tuple(int(num) for num in line[1].split(','))
            problems.append({"nums": nums, "chars": symbols, "count": 0})

    # * * * * * Part 2 Update * * * * *
    for problem in problems:
        chars = problem["chars"]
        problem["chars"] = chars + ["?"] + chars + ["?"] + chars + ["?"] + chars + ["?"] + chars
        nums = list(problem["nums"])
        problem["nums"] = tuple(nums + nums + nums + nums + nums)

    # updating nums of combos
    for problem in problems:
        update_possibilities(problem)
        print(problem)

    # determining total sum of combos
    summ = sum(problem["count"] for problem in problems)
    print(summ)


def update_possibilities(problem):
    # basic backtracking
    unknown, confirmed, spacer = '?', '#', '.'
    if unknown in problem["chars"]:
        for pos, char in enumerate(problem["chars"]):
            if char == unknown:
                for replacement in (confirmed, spacer):
                    problem["chars"][pos] = replacement
                    if unknown in problem["chars"]:
                        update_possibilities(problem)
                    else:
                        increment_if_valid(problem)
                problem["chars"][pos] = unknown
                return
    return


def increment_if_valid(problem):
    # simple validity checker
    groupings, chars = problem["nums"], problem["chars"]
    grouped = list(filter(None, "".join(chars).strip('.').split('.')))
    if len(groupings) == len(grouped) and all([len(segment) == size for size, segment in zip(groupings, grouped)]):
        problem["count"] += 1


if __name__ == "__main__":
    main()
