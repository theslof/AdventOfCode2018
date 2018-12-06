from collections import defaultdict

input_gen = [row.rstrip() for row in open("day04.in", 'r') if row != '\n']
input_gen.sort()
data = [[date, int(time[3:]), action] for (date, time), action in ((row[6:17].split(), row[19:]) for row in input_gen)]

active_guard = 0
sleep_start = 0

minutes = [defaultdict(int) for _ in range(60)]

for date, time, action in data:
    if action[0] == 'G':
        # Guard x begins shift
        active_guard = int(action.split()[1][1:])
    elif action[0] == 'f':
        # Guard falls asleep
        sleep_start = time
    elif action[0] == 'w':
        # Guard wakes up
        for minute in range(sleep_start, time):
            minutes[minute][active_guard] += 1

sleepiest_minute = -1
number_minutes = -1
guard = -1

for minute in minutes:
    if len(minute) < 1:
        continue
    (guard_, number_minutes_) = sorted(minute.items(), key=lambda x: x[1], reverse=True)[0]
    if number_minutes_ > number_minutes:
        guard = guard_
        number_minutes = number_minutes_
        sleepiest_minute = minutes.index(minute)
print(guard * sleepiest_minute)
