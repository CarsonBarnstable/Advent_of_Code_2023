def main():
    cards = []

    # parsing input
    with open("input.txt") as f:
        for line in f.readlines():

            # separating line into two groups
            line = line.strip().split('|')
            line[0] = line[0].split(':')[1]

            # getting & saving correct nums
            mine_nums = set(line[0].strip().replace("  ", " ").split(' '))
            card_nums = set(line[1].strip().replace("  ", " ").split(' '))

            # saving my nums, card nums, and the matching numbers
            cards.append((mine_nums, card_nums, (mine_nums & card_nums)))

    # calculating sum
    score_sum = 0
    for card in cards:
        num_matches = len(card[2])  # number of matches
        score = 0 if num_matches == 0 else 2**(num_matches-1)
        score_sum += score  # incrementing score sum

    # result
    print(score_sum)


if __name__ == "__main__":
    main()
