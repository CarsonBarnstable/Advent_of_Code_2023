def main():
    # getting input from file
    with open("input.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
    break_index = lines.index('')
    flow_lines, rating_lines = lines[:break_index], lines[break_index+1:]

    # parsing input
    flows = extract_flows_from_lines(flow_lines)
    ratings = extract_ratings_from_lines(rating_lines)

    # getting resultant 'destination' per part
    results = [get_destination_from_part(part, flows) for part in ratings]

    # calculating resultant sum
    summ = sum_accepted(results, ratings)
    print("Part 1:", summ)

    # Part 2 Note
    print("Part 2 is just a re-work of Day 5's Part 2")
    print("Due to Time Constraints, it will be skipped for now")


def extract_flows_from_lines(flow_lines):
    # parses flow lines according to problem description
    flows = {}
    for line in flow_lines:
        name = line.split('{')[0]
        clauses = line.split('{')[1].split(',')
        flows[name] = []
        for clause in clauses:
            if ':' in clause:
                condition, target = clause.split(':')[:2]
                flows[name].append((condition, target))
            else:
                flows[name].append(('else', clause.strip('}')))
    return flows


def extract_ratings_from_lines(rating_lines):
    # parses ratings lines according to problem description
    ratings = []
    for line in rating_lines:
        line = line.strip('{').strip('}').split(',')
        new_dict = {}
        for part in line:
            var, val = part.split('=')
            new_dict[var] = int(val)
        ratings.append(new_dict)
    return ratings


def get_destination_from_part(part, flows, start_target="in", goal_vals=('A', 'R')):
    # finds resulting destination given an input part (and requisite flows)
    to_go_to = start_target
    while to_go_to not in goal_vals:
        for potential_branch in flows[to_go_to]:
            if evaluate(potential_branch[0], part):
                to_go_to = potential_branch[1]
                break
    return to_go_to


def evaluate(conditional, part, default="else", vals="xmas"):
    # "safely" evaluates conditional from input condition
    if conditional == default:
        return True
    var, comp, comp_value = conditional[:1], conditional[1:2], int(conditional[2:])
    if comp == "<":
        return any(part[var] < comp_value and var == i_var for i_var in vals)
    if comp == ">":
        return any(part[var] > comp_value and var == i_var for i_var in vals)


def sum_accepted(results, ratings, accept="A"):
    # sums all ratings from accepted parts
    return sum(sum(rating.values()) if result in accept else 0 for rating, result in zip(ratings, results))


if __name__ == "__main__":
    main()
