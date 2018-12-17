from typing import NamedTuple, Set, Tuple, Iterator, List, Dict
import re
from collections import Counter

with open ('data/day03a.txt') as f:
    claims = [line.strip() for line in f]


# Joel Grus::
print('Joel Grus::::'*5)

Coord = Tuple[int, int]

class Rectangle(NamedTuple):
    id: int
    x_lo: int
    y_lo: int
    x_hi: int
    y_hi: int

    @staticmethod
    def from_claim(claim: str) -> 'Rectangle':
        id, x_lo, y_lo, width, height = [int(x) for x in re.match(rgx, claim).groups()]
        return Rectangle(id, x_lo, y_lo, x_lo + width, y_lo + height)
    
    def all_squares_iterator(self) -> Iterator[Coord]:
        for i in range(self.x_lo, self.x_hi):
            for j in range(self.y_lo, self.y_hi):
                yield(i, j)

rgx = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"

assert Rectangle.from_claim("#123 @ 868,343: 25x15") == \
    Rectangle(123, 868, 343, 868+25, 343+15)

def coverage(rectangles: List[Rectangle]) -> Dict[Coord, int]:
    counts = Counter()

    for rectangle in rectangles:
        for coord in rectangle.all_squares_iterator():
            counts[coord] += 1
    
    return counts

def multi_claimed(claims:List[str]) -> int:
    rectangles = [Rectangle.from_claim(claim) for claim in claims]
    
    counts = coverage(rectangles)

    #return len([count for count in counts.values() if count >= 2])
    return counts

TEST_CLAIMS = ['#1 @ 1,3: 4x4','#2 @ 3,1: 4x4','#3 @ 5,5: 2x2']
#assert multi_claimed(TEST_CLAIMS) == 4

test = multi_claimed(TEST_CLAIMS)
test_2 = set([x for x in test if test[x] >= 2])


print(test)
print(test_2)

#print([x for x in test if test[x] >= 2])
#print([x for x in test.values() if x >= 2])
