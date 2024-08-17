import sys
input = sys.stdin.readline

max = 0
max_index = -1
for i in range(1,10):
    n = int(input())
    if max < n:
        max = n
        max_index = i
print(max)
print(max_index)