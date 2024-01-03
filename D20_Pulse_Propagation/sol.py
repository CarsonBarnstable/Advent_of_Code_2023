starter_symbol, flip_flop, conj = "broadcaster", "%", "&"


# going purely functional programming on this one
def main():
    # getting input as dict
    symbols = {}
    with open("input.txt") as f:
        for line in f.readlines():
            left, right_list = line.strip('\n').split(" -> ")
            symbols[left] = right_list.split(", ")

    # mostly initializing collections
    start_symbols, flip_flops, conjunctions = [], {}, {}
    for symbol, targets in symbols.items():
        if symbol == starter_symbol:
            start_symbols += targets
        if symbol[0] == flip_flop:
            flip_flops[symbol[1:]] = {"targets": targets, "status": 0}
        if symbol[0] == conj:
            conjunctions[symbol[1:]] = {"targets": targets, "recieved": {}}

    # pre-setting all statuses for conjunction inputs
    for target, details in conjunctions.items():
        for symbol, targets in symbols.items():
            if target in targets:
                details["recieved"][symbol[1:]] = 0

    print(start_symbols)
    print(flip_flops)
    print(conjunctions)


if __name__ == "__main__":
    main()
