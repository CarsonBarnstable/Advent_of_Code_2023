def main():
    lines = []
    # input
    with open("input.txt") as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))

    # node titles
    nodes = [line.split(": ")[0] for line in lines]
    # adjacencies
    adj = {nodes[i]: [to for to in line.split(": ")[1].split(' ')] for i, line in enumerate(lines)}
    full_adj = {}
    for _from, _to in adj.items():
        for target in _to:
            if target not in full_adj:
                full_adj[target] = []
            full_adj[target].append(_from)
        if _from not in full_adj:
            full_adj[_from] = []
        for t in _to:
            full_adj[_from].append(t)

    print(full_adj)


if __name__ == "__main__":
    main()
