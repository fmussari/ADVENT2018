import re
from typing import List, Iterator, Set, Dict, NamedTuple, Tuple

with open ('data/day03a.txt') as f:
    ids = [line.strip() for line in f]

# print(ids[:2])

def regex_search (text:str, regex:str) -> Dict:
    match = re.search(regex, text)
    rightdown = (
        int(match.group(2))+int(match.group(4)),
        int(match.group(3))+int(match.group(5))
                )
    return {
        'id': int(match.group(1)), 
        'leftup': (int(match.group(2)),int(match.group(3))), 
        'widetall': (int(match.group(4)),int(match.group(5))),
        'rightdown': rightdown
        }

# En lugar de regex, aquí otra forma:
# https://github.com/octonion/adventofcode/blob/master/2018/3/general.py

def another_search (text:str):
    input = []
    a = text.split()
    print('a:',a)
    id = int(a[0].strip('#'))
    print('id:',id)
    x,y = [int(i) for i in a[2].strip(':').split(',')]
    m,n = [int(i) for i in a[3].split('x')]
    #input.append(Rectangle(x,y,x+m,y+n,[id]))
    return (x,y,x+m,y+n,[id])

###



def xy_max (ids:List[str]):
    regex = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
    min_x = []
    min_y = []
    max_x = []
    max_y = []
    for id in ids:
        id_dict = regex_search (id, regex)
        min_x.append(id_dict['leftup'][0])
        min_y.append(id_dict['leftup'][1])
        max_x.append(id_dict['rightdown'][0])
        max_y.append(id_dict['rightdown'][1])
    return {'min_x': min_x, 'min_y': min_y, 'max_x': max_x, 'max_y': max_y}

s = ids[100]
print(s)
regex = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'

id_dict = regex_search (s, regex)
print(id_dict)
print(another_search(s))

xy_max = xy_max (ids)
print(min(xy_max['min_x']))
print(min(xy_max['min_y']))
print(max(xy_max['max_x']))
print(max(xy_max['max_y']))

# Abandoné,
# Joel Grus::
print('Joel Grus::::'*5)
from typing import NamedTuple, Set, Tuple, Iterator
import re
from collections import Counter
Coord = Tuple[int, int]

class Rectangle(NamedTuple):
    id: int
    x_lo: int
    y_lo: int
    x_hi: int
    y_hi: int

    @staticmethod
    def from_claim(claim: str) -> 'Rectangle':
        #rgx = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
        id, x_lo, y_lo, width, height = [int(x) for x in re.match(rgx, claim).groups()]
        return Rectangle(id, x_lo, y_lo, x_lo + width, y_lo + height)
    
    #def all_squares_set(self) -> Set[Coord]:
    #    return {(i, j) 
    #        for i in range(self.x_lo, self.x_hi)
    #        for j in range(self.y_lo, self.y_hi)
    #    }
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
    #print(sorted(counts.items()))
    #print(sorted(counts.items()))

    return len([count for count in counts.values() if count >= 2])
    #return counts

TEST_CLAIMS = ['#1 @ 1,3: 4x4','#2 @ 3,1: 4x4','#3 @ 5,5: 2x2']

assert multi_claimed(TEST_CLAIMS) == 4

claims = ids
counter_claims = multi_claimed(claims)
print(counter_claims)


def non_overlapping_claim(claims: List[str]) -> int:
    rectangles = [Rectangle.from_claim(claim) for claim in claims]
    counts = coverage(rectangles)

    good_rectangles = [rectangle 
                        for rectangle in rectangles 
                        if all(counts[coord] == 1 for coord in rectangle.all_squares_iterator())]

    assert len(good_rectangles) == 1
    return good_rectangles[0].id

assert non_overlapping_claim(TEST_CLAIMS) == 3

print(non_overlapping_claim(claims))