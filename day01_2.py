from itertools import cycle

data = map(int, open("day01.in", 'r').readlines())
freq = 0
freqs = {freq}

for x in cycle(data):
    freq += x
    if freq in freqs:
        break
    freqs.add(freq)
print(freq)
