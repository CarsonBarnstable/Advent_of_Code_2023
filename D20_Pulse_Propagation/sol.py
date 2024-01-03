starter_symbol, flip_flop, conj = "broadcaster", "%", "&"
LOW, HIGH, REPEATS = "L", "H", 1000


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
            flip_flops[symbol[1:]] = {"targets": targets, "status": LOW}
        if symbol[0] == conj:
            conjunctions[symbol[1:]] = {"targets": targets, "recieved": {}}

    # pre-setting all statuses for conjunction inputs
    for target, details in conjunctions.items():
        for symbol, targets in symbols.items():
            if target in targets:
                details["recieved"][symbol[1:]] = LOW

    # counting all signals
    counter = {LOW: 0, HIGH: 0}
    # loop of chosen number of iterations
    for _ in range(REPEATS):
        counter[LOW] += 1
        # using a queue of sorts (essentially BFS) to deal with signals
        to_do = [(LOW, t, starter_symbol) for t in start_symbols]
        while to_do:
            signal, target, origin = to_do.pop(0)  # getting first element to be dealt with
            counter[signal] += 1
            # flip-flops
            if target in flip_flops:
                if signal == HIGH:
                    continue
                if signal == LOW:
                    # logic as defined
                    flip_flops[target]["status"] = LOW if flip_flops[target]["status"] == HIGH else HIGH
                    to_do += [(flip_flops[target]["status"], new_t, target) for new_t in flip_flops[target]["targets"]]
            # conjunctions
            if target in conjunctions:
                conjunctions[target]["recieved"][origin] = signal  # remembering last state
                if all(sig == HIGH for sig in conjunctions[target]["recieved"].values()):  # if all incoming were high
                    to_do += [(LOW, new_t, target) for new_t in conjunctions[target]["targets"]]
                else:
                    to_do += [(HIGH, new_t, target) for new_t in conjunctions[target]["targets"]]

    # result / solution
    print("Part 1:", counter[LOW]*counter[HIGH], "[ high:", counter[HIGH], "| low:", counter[LOW], "]")


if __name__ == "__main__":
    main()
