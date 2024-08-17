import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = [0]*n
for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        basket[l] = k
for l in range(n):
    print(basket[l], end=" ")
print()