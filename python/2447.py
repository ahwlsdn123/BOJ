import math
n = int(math.log(int(input()),3))
answer = [['*']]
for i in range(1,9):
    l = len(answer[i-1])
    tmp = []
    for s in answer[i-1]:
        tmp.append(s*3)
    for s in answer[i-1]:
        tmp.append(s+' '*len(s)+s)
    for s in answer[i-1]:
        tmp.append(s*3)
    answer.append(tmp)
for s in answer[n]:
    print(s)