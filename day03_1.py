GRID_SIZE = 1000
input_gen = (row.split() for row in open("day03.in", 'r') if row != '\n')
data = ([id_string, tuple(map(int, xy[:-1].split(','))), tuple(map(int, wh.split('x')))] for id_string, _, xy, wh in input_gen)
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

for claim in data:
    x1, y1 = claim[1]
    w1, h1 = claim[2]
    for x in range(x1, x1 + w1):
        for y in range(y1, y1 + h1):
            grid[y][x] += 1

result = len([x for y in grid for x in y if x > 1])
print(result)
