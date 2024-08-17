import sys
import math
input = sys.stdin.readline

t = int(input())
numbers = [1 for _ in range(1000001)] # 0~n
for i in range(3,1001,2):
    for j in range(3,1000000//i+1,2):
        numbers[i*j] = 0 # 합성수
for _ in range(t):
    n = int(input())
    if n == 4:
        print(1)
        continue
    answer = 0
    for i in range(3,n//2+1,2):
        if numbers[i] == 1 and numbers[n-i] == 1:
            answer += 1
    print(answer)