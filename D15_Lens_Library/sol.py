def main():
    # getting input
    sequence = []
    with open("input.txt") as f:
        for subseq in f.readline().strip('\n').split(','):
            sequence.append(subseq)

    # calculating sum of hashes
    hash_sum = 0
    for subseq in sequence:
        hash_sum += s_hash(subseq)
    # part 1 result
    print("Part 1:", hash_sum)


def s_hash(subseq):
    # direct HASH algorithm
    val = 0
    for char in subseq:
        val = (val+ord(char))*17 % 256
    return val


if __name__ == "__main__":
    main()
