def main():
    # getting input
    sequence = []
    with open("input.txt") as f:
        for subseq in f.readline().strip('\n').split(','):
            sequence.append(subseq)

    # * * * * * PART ONE SOLUTION * * * * *

    # calculating sum of hashes
    hash_sum = 0
    for subseq in sequence:
        hash_sum += s_hash(subseq)
    # part 1 result
    print("Part 1:", hash_sum)

    # * * * * * PART TWO SOLUTION * * * * *

    # initializing box storage
    boxes = [{} for _ in range(256)]

    # updating boxes by rules
    for operation in sequence:
        update_b_with_op(boxes, operation)

    # calculating total focusing power
    focusing_power = 0
    for b_num, box in enumerate(boxes):
        for s_index, (label, f_len) in enumerate(box.items()):
            # product of box number, slot index, and lens focal length
            focusing_power += (b_num+1) * (s_index+1) * f_len
    # result
    print("Part 2:", focusing_power)


def s_hash(subseq):
    # direct HASH algorithm
    val = 0
    for char in subseq:
        val = (val+ord(char))*17 % 256
    return val


def update_b_with_op(boxes, operation):
    label = operation.split('-')[0] if '-' in operation else operation.split('=')[0]
    b_num = s_hash(label)

    # 'remove' operation
    if '-' in operation:
        if label in boxes[b_num].keys():
            del boxes[b_num][label]

    # 'update' operation
    if '=' in operation:
        f_len = int(operation.split('=')[1])
        boxes[b_num][label] = f_len  # update


if __name__ == "__main__":
    main()
