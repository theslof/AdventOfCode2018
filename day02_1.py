from collections import Counter

data = set(Counter(row).values() for row in open("day02.in", 'r'))

twos = 0
threes = 0

for row in data:
    if 2 in row:
        twos += 1
    if 3 in row:
        threes += 1
print(twos * threes)
