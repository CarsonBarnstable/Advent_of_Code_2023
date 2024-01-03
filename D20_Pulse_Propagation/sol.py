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
    _p1_ff, _p1_cj = flip_flops, conjunctions
    for _ in range(REPEATS):
        res_counts, _p1_ff, _p1_cj = push_broadcast_button(start_symbols, _p1_ff, _p1_cj)
        counter = {sig: counter[sig]+res_counts[sig] for sig in (LOW, HIGH)}

    # result / solution
    print("Part 1:", counter[LOW]*counter[HIGH], "[ high:", counter[HIGH], "| low:", counter[LOW], "]")

    # part 2 thoughts
    """
    I tried brute-forcing part 2 for a minute, to no avail
    Looking at the input, [rx] is only the target of (the conjunction) [gf]
    Thus, [rx] will only get a low input when [gf] has gotten all high inputs
    Those inputs would have to be from (all conjunctions) [kr], [zs], [kf], and [qk]
    My gut is telling me to brute-force to see if there are cycles in their output states
    And there will likely be a LCM solution or some sort of pattern that can be extrapolated
    """


def push_broadcast_button(start_sym, ffs, cnjs):
    # conducts single press of a button, returning resultant state of game
    counter = {LOW: 0, HIGH: 0}
    counter[LOW] += 1
    # using a queue of sorts (essentially BFS) to deal with signals
    to_do = [(LOW, t, starter_symbol) for t in start_sym]
    while to_do:
        signal, target, origin = to_do.pop(0)  # getting first element to be dealt with
        counter[signal] += 1
        # flip-flops
        if target in ffs:
            if signal == HIGH:
                continue
            if signal == LOW:
                # logic as defined
                ffs[target]["status"] = LOW if ffs[target]["status"] == HIGH else HIGH
                to_do += [(ffs[target]["status"], new_t, target) for new_t in ffs[target]["targets"]]
        # conjunctions
        if target in cnjs:
            cnjs[target]["recieved"][origin] = signal  # remembering last state
            if all(sig == HIGH for sig in cnjs[target]["recieved"].values()):  # if all incoming were high
                to_do += [(LOW, new_t, target) for new_t in cnjs[target]["targets"]]
            else:
                to_do += [(HIGH, new_t, target) for new_t in cnjs[target]["targets"]]

    return counter, ffs, cnjs


if __name__ == "__main__":
    main()
