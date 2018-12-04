from collections import defaultdict

input_gen = [row.rstrip() for row in open("day04.in", 'r') if row != '\n']
input_gen.sort()
# [1518-11-05 00:03] Guard #99 begins shift
data = [[date, int(time[3:]), action] for (date, time), action in ((row[6:17].split(), row[19:]) for row in input_gen)]

sleep = defaultdict(int)
active_guard = 0
sleep_start = 0

for date, time, action in data:
    if action[0] == 'G':
        # Guard x begins shift
        active_guard = int(action.split()[1][1:])
    elif action[0] == 'f':
        # Guard falls asleep
        sleep_start = time
    elif action[0] == 'w':
        # Guard wakes up
        sleep[active_guard] += time - sleep_start

result = sorted(sleep.items(), key=lambda x: x[1], reverse=True)
target_guard = result[0][0]


minutes = [0 for _ in range(60)]
for date, time, action in data:
    if action[0] == 'G':
        # Guard x begins shift
        active_guard = int(action.split()[1][1:])
    elif action[0] == 'f':
        # Guard falls asleep
        if active_guard != target_guard:
            continue
        sleep_start = time
    elif action[0] == 'w':
        # Guard wakes up
        if active_guard != target_guard:
            continue
        for minute in range(sleep_start, time):
            minutes[minute] += 1
print(target_guard * minutes.index(max(minutes)))
