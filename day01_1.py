data = [int(x.replace('+', '')) for x in open("day01.in", 'r')]
print(sum(data))
