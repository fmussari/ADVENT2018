
with open('data/day01a.txt') as f:
    numbers = [int(line.strip()) for line in f]
    
print(sum(numbers))
print(numbers[:5])


from typing import List, Iterator, Set

def return_seen_freq (numbers: Set[int], start: int = 0):
    i = 0
    freq = start
    seen = {freq}
    while True:
        for number in numbers:
            freq += number
            if freq in seen:
                print(len(seen))
                return {'Repeated Freq': freq}
            seen.add(freq)

print(len(numbers))
print(return_seen_freq (numbers, 0))


## Joel Grus:
def all_frequencies(numbers: List[int], start: int = 0) -> Iterator[int]:
    """
    Generate all frequencies...
    """
    frequency = start
    #seen: Set[int] = set()
    #seen = {0}

    while True:
        for number in numbers:
            yield frequency
            frequency += number

def first_repeat_frequency(numbers: List[int], start: int = 0) -> int:
    seen = set()
    for frequency in all_frequencies(numbers, start):
        if frequency in seen:
            print('grus: ', len(seen))
            return frequency
        else:
            seen.add(frequency)

#assert first_repeat_frequency([1,-1]) == 0
#assert first_repeat_frequency([3,3,4,-2,-4]) == 10
#assert first_repeat_frequency([-6,3,8,5,-6]) == 5
#assert first_repeat_frequency([7,7,-2,-7,-4]) == 14

print('grus:', first_repeat_frequency(numbers,0))