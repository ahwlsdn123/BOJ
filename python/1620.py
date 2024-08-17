import sys
input = sys.stdin.readline

n,m = map(int, input().split())
list = []
for _ in range(n):
    list.append(input().rstrip())
for _ in range(m):
    problem = input().rstrip()
    if problem.isdigit():
        num = int(problem)
        print(list[num-1])
    else:
        print(list.index(problem)+1)