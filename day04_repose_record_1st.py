import re
import datetime
from typing import List, Iterator, Set, Dict, NamedTuple, Tuple
from collections import Counter

with open ('data/day04.txt') as f:
    records = [line.strip() for line in f]

#print(records[:5])

def get_regex (text, regex):
    match = re.search(regex, text)       
    print([x for x in match.groups()])

def first (list):
    return list[0]

def parse_lines (records: List[str]) -> List:
    output_list = []
    rgx_guard = r"#(\d+)"
    rgx_sleep = r"\[(\d+-\d+-\d+ \d+:\d+)\] (\w+)"

    for record in records:
        
        match = re.search(rgx_sleep, record)
        output = [x for x in match.groups()]
        
        if output[-1] == "Guard":
            match_id = re.search(rgx_guard, record)
            output[-1] = int(match_id.group(1))
        
        date_str = output[0]
        format_str = '%Y-%m-%d %H:%M' # The format
        output[0] = datetime.datetime.strptime(date_str, format_str)
        
        output_list.append(output)
        
    return sorted(output_list, key=first)

def cronograma (consolidada_list: List):
    cronograma_list = []
    for reg in consolidada_list:
        timeline = [False]*60
        for tup in reg[2]:
            timeline[tup[0]:tup[1]] = [True]*(tup[1]-tup[0])
        
        cronograma_list.append(reg[:2] + [timeline])
    
    return cronograma_list


def consolidate_list (sorted_list: List):
    consolidada = []
    for i in range(len(sorted_list)):
        reg = sorted_list[i]
        tipo = type(reg[1])
        if tipo == int:
            apuntador = reg
            apuntador.append([])
            consolidada.append(apuntador)
        elif reg[1] == 'wakes':
            tup = (sorted_list[i-1][0].minute,sorted_list[i][0].minute)
            apuntador[2].append(tup)
            
    return consolidada

def a_contar (crono_list: List):
    counts = Counter()
    for reg in crono_list:
        counts[reg[1]] += sum(reg[2])
    
    return counts.most_common(2)
        
def counter_per_minute (crono_list: List, id:int):
    counts = Counter()
    for reg in crono_list:
        if reg[1] == id:
            for i, minute in enumerate(reg[2]):
                counts[i] += int(minute)
    
    return counts.most_common(2)

    

registros = parse_lines(records)
consolidada = consolidate_list(registros)
print(consolidada[2])
con_cronograma = cronograma(consolidada)
#print(con_cronograma[2])
#print(sum(con_cronograma[2][2]))

print('A Contar:')
print(a_contar(con_cronograma))
print('A Contar x minute:')
print(counter_per_minute (con_cronograma, 857))

print(857*46)




assertar = [
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

registros = parse_lines(assertar)
consolidada = consolidate_list(registros)
con_cronograma = cronograma(consolidada)

print('A Contar:')
print(a_contar(con_cronograma))
print('A Contar x minute:')
print(counter_per_minute (con_cronograma, 10))