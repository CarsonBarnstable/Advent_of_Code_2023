def main():
    snowballs = []
    with open("input.txt") as f:
        for line in f.readlines():
            x, y, z = line.split(" @ ")[0].split(", ")
            dx, dy, dz = line.split(" @ ")[1].split(", ")
            snowballs.append({'x': int(x), 'y': int(y), 'z': int(z), 'dx': int(dx), 'dy': int(dy), 'dz': int(dz)})
    backup_snowballs = [s for s in snowballs]

    have_entered = False
    valid_range = range(200000000000000, 400000000000000+1)
    intercept_count = 0
    while not have_entered or any(s['x'] in valid_range and s['y'] in valid_range for s in snowballs):
        # check for hits
        for s1 in snowballs[:10]:
            for s2 in snowballs[:10]:
                if s1 != s2 and s1['x'] == s2['x'] and s1['y'] == s2['y']:
                    intercept_count += 1
        # update positions
        snowballs = [{'x': s['x']+s['dx'], 'y': s['y']+s['dy'], 'dx': s['dx'], 'dy': s['dy']} for s in snowballs]
    print(intercept_count)


if __name__ == "__main__":
    main()
