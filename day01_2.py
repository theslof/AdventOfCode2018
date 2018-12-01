data = [int(x.replace('+', '')) for x in open("day01.in", 'r')]
freqs = set()
freq = 0
freqs.add(freq)

while True:
    for x in data:
        freq += x
        if freq in freqs:
            print(freq)
            exit()
        freqs.add(freq)
