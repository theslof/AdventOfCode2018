data = list(open("day05.in", 'r').readline().rstrip())

processed = []
for c in data:
    if processed and c != processed[-1] and c.lower() == processed[-1].lower():
        processed.pop()
    else:
        processed.append(c)
print(len(processed))
