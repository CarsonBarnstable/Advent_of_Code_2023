def main():
    with open("input.txt") as f:
        times, records = f.readlines()[:2]

    # extracting times
    extracted_times = []
    for line in (times, records):
        line = line.strip("\n").split(' ')[1:]
        line = list(filter(lambda num: len(num) > 0, line))
        extracted_times.append([int(num) for num in line])
    times, records = extracted_times

    # getting valid "improved times"
    cutoff_ranges = []
    for time, cutoff in zip(times, records):
        min_hold, max_hold = 0, 0
        for hold_time in range(time//2):
            if hold_time * (time - hold_time) < cutoff:
                min_hold = hold_time
        min_hold, max_hold = min_hold+1, time-min_hold-1
        cutoff_ranges.append((min_hold, max_hold))

    # calculating result
    product = 1
    for pair in cutoff_ranges:
        product *= pair[1]-pair[0]+1

    # result
    print(product)


if __name__ == "__main__":
    main()
