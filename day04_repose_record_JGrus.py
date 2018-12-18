RAW = [
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-01 23:58] Guard #99 begins shift',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-03 00:05] Guard #10 begins shift',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-05 00:45] falls asleep',
    '[1518-11-05 00:55] wakes up'
    ]

from typing import NamedTuple, List, Tuple
import re

class Timestamp(NamedTuple):
    year: int
    month: int
    day: int
    hour: int
    minute: int

class Nap(NamedTuple):
    guard_id: int
    sleep: int  # minutes
    wake: int   # minutes

rgx = r"\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})\] (.*)"
guard_id_rgx = r"Guard #([0-9]+)"

def find_naps(entries: List[str]) -> List[Nap]:
    naps: List[Nap] = []
    entries = sorted(entries)

    guard_id = sleep = wake = None

    for entry in entries:
        #print(entry)
        year, month, day, hour, minute, comment = re.match(rgx, entry).groups()
        ts = Timestamp  (
                    int(year), int(month), int(day),
                    int(hour), int(minute)
                        )
        guard = re.match(guard_id_rgx, comment)

        if guard:
            assert sleep is None and wake is None
            guard_id = int(guard.groups()[0])

        elif "falls asleep" in comment:
            assert guard_id is not None and sleep is None and wake is None
            sleep = int(minute)
        elif  "wakes up" in comment:
            assert guard_id is not None and sleep is not None and wake is None
            wake = int(minute)
            naps.append(Nap(guard_id, sleep, wake))
            sleep = wake = None
    
    return naps

from collections import Counter                        

def sleepiest_guard(naps: List[Nap]) -> int:
    sleep_counts = Counter()
    
    for nap in naps:
        sleep_counts[nap.guard_id] += (nap.wake - nap.sleep)
    print(sleep_counts)
    return sleep_counts.most_common(1)[0][0]

def most_common_sleepy_minute(naps: List[Nap], guard_id: int) -> int:
    minutes = Counter()
    for nap in naps:
        if nap.guard_id == guard_id:
            for minute in range(nap.sleep, nap.wake):
                minutes[minute] += 1
    [(minute1,count1),(minute2,count2)] = minutes.most_common(2)
    assert count1 > count2
    return minute1


list_of_naps = find_naps(RAW)
#print(list_of_naps)
#print(list_of_naps[0].guard_id)

sleepiest = sleepiest_guard(list_of_naps)
assert sleepiest == 10
assert most_common_sleepy_minute(list_of_naps, 10) == 24


with open ('data/day04.txt') as f:
    lines = [line.strip() for line in f]

print('*'*50)
list_of_naps = find_naps(lines)
sleepiest_guard = sleepiest_guard(list_of_naps)
sleepiest_minute = most_common_sleepy_minute(list_of_naps, sleepiest_guard)
print(sleepiest_guard)
print(sleepiest_minute)
print(str(sleepiest_guard) + 'x' + str(sleepiest_minute) + '= ' + str(sleepiest_guard*sleepiest_minute))

def most_freq_minute(naps: List[Nap]) -> Tuple[int, int]:
    minutes = Counter()
    for nap in naps:
        for minute in range(nap.sleep, nap.wake):
                minutes[(nap.guard_id, minute)] += 1
    [((id1, minute1), count1),((id2, minute2),count2)] = minutes.most_common(2)
    assert count1 > count2
    return (id1, minute1)


assert most_freq_minute(find_naps(RAW)) == (99, 45)

print('(id,minuto más frecuente')
id_minute = (id_, minute) = most_freq_minute(list_of_naps)
print(id_minute)
print(str(id_) + 'x' + str(minute) + '= ' + str(id_*minute))