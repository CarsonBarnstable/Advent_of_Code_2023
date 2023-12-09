def main():
    # getting program input
    sequences = []
    with open("input.txt") as f:
        for line in f.readlines():
            sequences.append([int(num) for num in line.strip('\n').split(' ')])

    # finding "next nums"
    seq_nn = []
    for seq in sequences:
        seq_nn.append(recursive_finite_difference(seq))

    # test/debug print
    # for seq, next_n in zip(sequences, seq_nn):
    #     print(seq, next_n)

    # calculating sums of next_nums
    summ = 0
    for nn in seq_nn:
        summ += nn

    # result
    print(summ)


def recursive_finite_difference(sequence):
    if any(num != 0 for num in sequence):
        new_seq = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
        return sequence[-1] + recursive_finite_difference(new_seq)
    else:
        return 0


if __name__ == "__main__":
    main()
