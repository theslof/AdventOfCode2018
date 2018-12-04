from collections import defaultdict

input_gen = [row.rstrip() for row in open("day04.in", 'r') if row != '\n']
input_gen.sort()
data = [[date, int(time[3:]), action] for (date, time), action in ((row[6:17].split(), row[19:]) for row in input_gen)]

sleep = defaultdict(int)
guards = set()
minutes = dict()
active_guard = 0
sleep_start = 0
sleepiest = 0

for date, time, action in data:
    if action[0] == 'G':
        # Guard x begins shift
        active_guard = int(action.split()[1][1:])
        if active_guard not in guards:
            minutes[active_guard] = [0 for _ in range(60)]
            guards.add(active_guard)
    elif action[0] == 'f':
        # Guard falls asleep
        sleep_start = time
    elif action[0] == 'w':
        # Guard wakes up
        sleep[active_guard] += time - sleep_start
        for minute in range(sleep_start, time):
            minutes[active_guard][minute] += 1
        if sleep[active_guard] > sleep[sleepiest]:
            sleepiest = active_guard

print(sleepiest * minutes[sleepiest].index(max(minutes[sleepiest])))
