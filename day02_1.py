from collections import Counter

data = [row.strip() for row in open("day02.in", 'r')]

twos = 0
threes = 0

for row in data:
    count = Counter(row)
    if 2 in count.values():
        twos += 1
    if 3 in count.values():
        threes += 1
print(twos * threes)
