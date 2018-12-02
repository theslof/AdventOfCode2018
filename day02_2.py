from difflib import ndiff

data = [row.strip() for row in open("day02.in", 'r')]


for i, word1 in enumerate(data):
    for word2 in data[i+1:]:
        diffs = [diff[-1] for diff in ndiff(word1, word2) if diff[0] == ' ']
        if len(diffs) == len(word1) - 1:
            print(''.join(diffs))
            exit()
