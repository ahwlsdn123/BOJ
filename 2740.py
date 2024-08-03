import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]
m,k = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(m)]
answer = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            answer[i][j] += arr1[i][l]*arr2[l][j]
for i in range(n):
    for j in range(k):
        print(answer[i][j], end=" ")
    print()