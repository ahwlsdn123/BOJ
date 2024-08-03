import sys
input = sys.stdin.readline

n = int(input())
b = True
for i in range(n):
    tmp = i
    list = []
    while tmp > 0:
        list.append(tmp%10)
        tmp //= 10
    sum = i
    for j in list:
        sum += j
    if sum == n:
        print(i)
        b = False
        break
if b:
    print(0)