def main():
    # getting input from file
    with open("input.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
    break_index = lines.index('')
    flow_lines, rating_lines = lines[:break_index], lines[break_index+1:]

    # parsing input
    flows = extract_flows_from_lines(flow_lines)
    ratings = extract_ratings_from_lines(rating_lines)


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
            new_dict[var] = val
        ratings.append(new_dict)
    return ratings


if __name__ == "__main__":
    main()
