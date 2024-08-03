import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
list = list(map(int, input().split()))
for i in range(m):
    if list[i] in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")
print()