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
        print(resta_list)
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
print(puntos_list)
sum_list = sum_all(puntos_list)
print(sum_list)
print('Result: ', sum_list[0]*sum_list[1])