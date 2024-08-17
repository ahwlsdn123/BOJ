import sys
input = sys.stdin.readline

n = int(input())
x_min = 10001
x_max = -10001
y_min = 10001
y_max = -10001
for _ in range(n):
    a, b = map(int, input().split())
    if x_min > a:
        x_min = a
    if x_max < a:
        x_max = a
    if y_min > b:
        y_min = b
    if y_max < b:
        y_max = b
print((x_max-x_min)*(y_max-y_min))