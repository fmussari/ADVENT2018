from typing import List, Iterator, Set

with open('data/day02a.txt') as f:
    box_id_list = [line.strip() for line in f]
print(box_id_list[:5])

def return_resta_list (char_list: List[str], unique: List[str]) -> List[str]:
    resta_list = []
    unique = set(unique)  # Si pasaba el set, se modificaba en la otra función
    for char in char_list:
        if char in unique:
            unique.remove(char)
        else:
            resta_list.append(char)
    char_list = []
    return resta_list

def count_rep (id: str):
    char_list = list(id)
    unique_set = list(set(char_list))
    resta_list = return_resta_list(char_list,unique_set)
    return resta_list

def all_ids_puntos (box_list: List[str]):
    result_list = []
    for id in box_list:
        resta_list = count_rep(id)
        #print(resta_list)
        largo = len(resta_list)
        if largo == 1:
            result_list.append((1,0))
        elif largo == 2:
            resta_list = count_rep(resta_list)
            largo = len(resta_list)
            if largo == 1:
                result_list.append((0,1))
            else:
                result_list.append((1,0))
        else:
            resta_list = count_rep(resta_list)
            largo = len(resta_list)
            if largo == 2:
                result_list.append((0,0))
            elif largo == 1:
                result_list.append((1,1))
            else:
                result_list.append((1,0))
    return result_list

def sum_all (puntos_list: List[str]):
    return [sum(x) for x in zip(*puntos_list)]


puntos_list = all_ids_puntos (box_id_list)
#print(puntos_list)
sum_list = sum_all(puntos_list)
#print(sum_list)
print('Result: ', sum_list[0]*sum_list[1])

### Joel Grus Solution

from typing import Set
from collections import Counter

ids = box_id_list
def char_count_values (word:str) -> Set[int]:
    char_counts = Counter(word)
    #print(char_counts)
    return set(char_counts.values())

print(char_count_values(box_id_list[0]))
print(char_count_values(box_id_list[1]))
print(char_count_values(box_id_list[2]))

def checksum(ids:List[str]) -> int:
    """
    """
    num_twos = 0
    num_threes = 0
    for box_id in ids: 
        ccv = char_count_values(box_id)
        if 2 in ccv:
            num_twos += 1
        if 3 in ccv:
            num_threes += 1
    
    return num_twos * num_threes

assert checksum(['abcdef','bababc','abbcde',
                 'abcccd', 'aabcdd', 'abcdee',
                 'ababab']) == 12


print('Grus Result: ', checksum(ids))

## My code only works in this specifi puzzle.
## Grus' one works with any similar one.

