coords_shuffle = open("input.txt").read().split("\n")
tmp = []
coords = []

for c in coords_shuffle:
    for char in c:
        if char.isdigit():
            tmp.append(char)
        else:
            pass
    coord = f"{tmp[0]}{tmp[-1]}"
    coords.append(int(coord))
    tmp.clear()
 
print(sum(coords))