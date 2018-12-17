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

from typing import NamedTuple, List
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



def find_naps(entries: List[str]) -> List[Nap]:
    entries = sorted(entries)

    current_guard_id = None

    for entry in entries:
        year, month, day, hour, minute, comment = re.search()



#def parse_line (line: str) -> Tuple



match = re.search(rgx, '[1518-11-01 00:00] Guard #10 begins shift')
print(match)
