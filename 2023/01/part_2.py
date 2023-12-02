coords_shuffle = open("input.txt").read().split("\n")
tmp = []
coords = []

for co in coords_shuffle:
    for i, c in enumerate(co):
        if c.isdigit():
            tmp.append(c)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if co[i:].startswith(val):
                tmp.append(str(d+1))
    coord = f"{tmp[0]}{tmp[-1]}"
    coords.append(int(coord))
    tmp.clear()

print(sum(coords))