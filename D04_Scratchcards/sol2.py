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

    # finding "copiers"
    to_repeat_and_multiplier = [0 for _ in range(len(cards))]
    for index, card in enumerate(cards):
        num_matches = len(card[2])  # number of matches
        for update in range(index, index+num_matches):
            if update in range(len(to_repeat_and_multiplier)):
                # update rule
                to_repeat_and_multiplier[update+1] += 1*(to_repeat_and_multiplier[index]+1)
        to_repeat_and_multiplier[index] += 1

    # result
    print(sum(to_repeat_and_multiplier))


if __name__ == "__main__":
    main()
