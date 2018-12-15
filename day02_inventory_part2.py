### Joel Grus Solution

from typing import Set, List
from collections import Counter

with open('data/day02a.txt') as f:
    ids = [line.strip() for line in f]
print(ids[:5])

# Given a list of ids, axactly two differ by exactly one character
# find the remaining characters
def characters_in_common(ids: List[str]) -> str:
    leave_one_outs = Counter()
    for box_id in ids:
        for i in (range(len(box_id))):
            leave_one_out = tuple(box_id[:i] + "_" + box_id[(i+1):])
            leave_one_outs[leave_one_out] += 1
    #print(leave_one_outs.most_common(2))
    [(best,count), (not_best, not_best_count)] = leave_one_outs.most_common(2)
    assert count == 2
    assert not_best_count == 1
    return ("".join([c for c in best if c != '_']))

TEST_IDS = [
    'abcde', 'fghij', 'klmno', 
    'pqrst', 'fguij', 'axcye', 
    'wvxyz']

assert characters_in_common(TEST_IDS) == 'fgij'
print(characters_in_common(TEST_IDS))

print(characters_in_common(ids))

#box_id = 'oiwcdpbseqgxryfmlpktnupvza'
#i = 0
#leave_one_out = tuple(box_id[:i] + "_" + box_id[(i+1):])
#print(leave_one_out)