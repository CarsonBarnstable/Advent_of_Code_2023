card_num = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}


def main():
    # getting input
    hands = []
    with open("input.txt") as f:
        for line in f.readlines():
            line = line.split(" ")
            hands.append([line[0], int(line[1].strip('\n')), 0])

    # get hand score
    for hand in hands:
        hand[2] = getscore(hand)

    # sort by score
    for _ in range(len(hands)):
        for left in range(0, len(hands)-1-_):
            right = left+1
            diff_score = hands[left][2] - hands[right][2]
            if diff_score > 0 or (diff_score == 0 and high_score(hands[left]) > high_score((hands[right]))):
                hands[left], hands[right] = hands[right], hands[left]

    # calculate "total sum"
    sum_scores = 0
    for pos, hand in enumerate(hands):
        sum_scores += (pos+1) * hand[1]

    # result
    print(sum_scores)


def getscore(hand):
    if 'J' in hand[0]:
        for pos, card in enumerate(hand[0]):
            if card == 'J':
                old_card = card
                maxscore = 0
                for replacement in "23456789TQKA":
                    hand[0] = hand[0][:pos] + replacement + hand[0][pos+1:]
                    if 'J' in hand[0]:
                        maxscore = max(getscore(hand), maxscore)
                    else:
                        maxscore = max(scoreof(hand), maxscore)
                hand[0] = hand[0][:pos] + old_card + hand[0][pos+1:]
                return maxscore
    return scoreof(hand)


def scoreof(hand):
    cards_in_hand = set(hand[0])
    if len(cards_in_hand) == 1:
        return 1000006  # 5 of a kind
    if len(cards_in_hand) == 2:
        if hand[0].count(hand[0][0]) in {1, 4}:
            return 1000005  # 4 of a kind
        if hand[0].count(hand[0][0]) in {2, 3}:
            return 1000004  # full house
    if len(cards_in_hand) == 3:
        if any(hand[0].count(hand[0][i]) == 3 for i in {0, 1, 2}):
            return 1000003  # 3 of a kind
        else:
            return 1000002  # 2 pair
    if len(cards_in_hand) == 4:
        return 1000001  # 1 pair
    # base case
    return high_score(hand)


def high_score(hand):
    # basically the base-15 value of the hand
    score = 0
    for pos in range(len(hand[0])):
        score = score * 15
        score += card_num[hand[0][pos]]
    return score


if __name__ == "__main__":
    main()
