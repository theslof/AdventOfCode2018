def overlaps(rectangle_1, rectangle_2) -> bool:
    x1, y1 = rectangle_1[1]
    w1, h1 = rectangle_1[2]
    x2, y2 = rectangle_2[1]
    w2, h2 = rectangle_2[2]
    return x1 < (x2 + w2) and (x1 + w1) > x2 and y1 < (y2 + h2) and (y1 + h1) > y2


input_gen = (row.split() for row in open("day03.in", 'r') if row != '\n')
data = list([id_string[1:], tuple(map(int, xy[:-1].split(','))), tuple(map(int, wh.split('x')))] for id_string, _, xy, wh in input_gen)
collisions = set()

for i, claim1 in enumerate(data):
    for claim2 in data[i+1:]:
        if overlaps(claim1, claim2):
            collisions.add(claim1[0])
            collisions.add(claim2[0])
    if claim1[0] not in collisions:
        print(claim1[0])
        break
