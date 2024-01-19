from collections import defaultdict
from _future_ import print_function


def processData(lines):
    arr=[]
    name={}
    maxscore=defaultdict(lambda : float('-inf'))
    time=defaultdict(None)

    for ele in lines:
        arr.append(ele.split(','))
        name[arr[-1][0]]=arr[-1][1]
        if int(arr[-1][-1]) > maxscore[arr[-1][0]]:
            maxscore[arr[-1][0]] = int(arr[-1][-1])
            time[arr[-1][0]] = int(arr[-1][-2])
            
    final = {}
    for k, v in time.items():
        final[name[k].strip()] = v
    return final

def run():
    lines = []
    with open('input.txt') as f:
        for line in f:
            lines.append(line)

        ret_value = processData(lines)
        with open('output.txt', 'w') as fout:
            for k, v in ret_value.items():
                print("{}: {}".format(k, v), file=fout)

if _name_ == '_main_':
    run()