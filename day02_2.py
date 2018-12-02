from itertools import combinations

data = (line.strip('\n') for line in open("day02.in", 'r') if line != '\n')

for word1, word2 in combinations(data, 2):
    common = [l1 for (l1, l2) in zip(word1, word2) if l1 == l2]
    if len(common) == len(word1) - 1:
        print(''.join(common))
        break
