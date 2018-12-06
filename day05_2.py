data = open("day05.in", 'r').readline().rstrip()

shortest = len(data)
for illegal in range(ord('a'), ord('z')):
    processed = []
    for c in data:
        if c.lower() == chr(illegal):
            continue
        if processed and c != processed[-1] and c.lower() == processed[-1].lower():
            processed.pop()
        else:
            processed.append(c)
    shortest = min(shortest, len(processed))
print(shortest)
