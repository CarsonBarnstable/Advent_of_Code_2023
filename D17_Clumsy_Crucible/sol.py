from sys import maxsize as kinda_infinity


directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
valid_dirs = {"U": "LR", "D": "LR", "L": "UD", "R": "UD"}


def main():
    # getting input
    grid = get_input_from("input.txt")
    start, target = (0, 0), (len(grid)-1, len(grid[-1])-1)

    # performing both parts
    print("Part 1:", modified_dijkstra(grid, _min=0, _max=3, _from=start, _to=target))
    print("Part 2:", modified_dijkstra(grid, _min=0, _max=3, _from=start, _to=target))


def get_input_from(filename):
    # parses input and returns grid
    with open(filename) as f:
        lines = [line.strip('\n') for line in f.readlines()]
    return [[int(num) for num in line] for line in lines]


def val_get(array, coords):
    # returns array entry with alternate input style
    intermediate = array
    for dim_val in coords:
        intermediate = intermediate[dim_val]
    return intermediate


def initialize_min_costs_on(grid, possible_directions, auto_fill=kinda_infinity):
    min_costs = []
    for row in range(len(grid)):
        mid_row = []
        for col in range(len(grid[-1])):
            mid_row.append({direction: auto_fill for direction in possible_directions})
        min_costs.append(mid_row)
    return min_costs


def modified_dijkstra(cost_grid, _min=0, _max=-1, _from=(0, 0), _to=(kinda_infinity, kinda_infinity), _start_dirs="DR"):
    # remembering costs (at each cell / from each direction)
    min_costs = initialize_min_costs_on(cost_grid, directions)
    # starting positions have 0 cost
    for d in _start_dirs:
        val_get(min_costs, _from)[d] = 0
    # initializing all nodes' "visited" status
    visited = [[{d: False for d in directions} for _ in cost_grid[-1]] for __ in cost_grid]
    to_traverse = [(0, (0, 0), d) for d in _start_dirs]

    # performing basic (but modified) dijkstra
    while to_traverse:
        # getting a node that needs to be addressed
        cumulative_heat_loss, coords, direction = to_traverse.pop()
        val_get(visited, coords)[direction] = True
        
        print(cumulative_heat_loss, coords, direction)





if __name__ == "__main__":
    main()
