import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]

max_value = 0
row = 1
col = 1
for i in range(9):
    for j in range(9):
        if max_value < arr[i][j]:
            max_value = arr[i][j]
            row = i+1
            col = j+1
print(max_value)
print(f"{row} {col}")