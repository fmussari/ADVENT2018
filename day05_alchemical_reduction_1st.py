import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)


with open ('data/day05.txt') as f:
    records = [line for line in f][0]
    
def reduction (polymer: str) -> str:
    polymer = polymer + '*'
    removed_chain: str = ''
    changed = False
    removed = False
    for i in range(len(polymer)-1):
        if removed:
            removed = False
            continue

        if polymer[i] != polymer[i+1].swapcase():
            removed_chain += polymer[i]
            removed = False
        else:
            changed = True
            removed = True
    
    if changed:
        return reduction(removed_chain)
    else:
        return removed_chain



assert reduction('dabAcCaCBAcCcaDA') == 'dabCBAcaDA'
assert reduction('Aa') == ''
assert reduction('abAB') == 'abAB'
assert reduction('abBA') == ''
assert reduction('abcBAdffF') == 'abcBAdf'

print('.txt processing:')
polymer = records[:50]
print(polymer)
print(reduction(polymer))

polymer = records

#result = reduction(polymer)
print('Day 5 result:')
#print(len(result))

def remove_unit (polymer: str, unit:str) -> str:
    output: str = ''
    unit_low = unit.lower()
    unit_upp = unit.upper()

    for i in range(len(polymer)):
        if polymer[i] != unit_low and polymer[i] != unit_upp:
            output += polymer[i]
    
    assert (unit_low not in output)
    assert (unit_upp not in output)
    return output

print('Part 2:')

assert remove_unit ('dabAcCaCBAcCcaDA', 'a') == 'dbcCCBcCcD'
assert remove_unit ('dabAcCaCBAcCcaDA', 'b') == 'daAcCaCAcCcaDA'
assert remove_unit ('dabAcCaCBAcCcaDA', 'c') == 'dabAaBAaDA'
assert remove_unit ('dabAcCaCBAcCcaDA', 'd') == 'abAcCaCBAcCcaA'

polymer = records
print('Day 5, part 2 result:')
result = remove_unit (polymer, 'c')
print(result[:100])
result = reduction (result)
print(result[:100])
print(len(result))


## Joel Grus  ##
print('## Joel Grus  ##'*5)
def reduct(polymer: str) -> str:
    did_reduce = True
    while did_reduce:
        did_reduce = False

        for i in range(1,len(polymer)):
            u1 = polymer[i-1]
            u2 = polymer[i]
            if (u1.lower() == u2.lower()) and (u1 != u2):
                polymer = polymer[:i-1] + polymer[i+1:]
                did_reduce = True
                break
    
    return polymer

#result = reduct(polymer)
#print("Grus' day 5 result:")
#print(len(result))