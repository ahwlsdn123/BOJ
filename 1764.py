import sys
input = sys.stdin.readline

n,m = map(int, input().split())
set1 = set()
set2 = set()
for _ in range(n):
    set1.add(input().rstrip())
for _ in range(m):
    set2.add(input().rstrip())
list = list(set1.intersection(set2))
list.sort()
print(len(list))
for i in range(len(list)):
    print(list[i])