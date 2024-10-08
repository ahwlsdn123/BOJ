import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n,m = map(int, input().split())
task = [list(map(int,input().split()))[1:] for _ in range(n)]

visit = [-1]*(m+1) # 직원을 배정함

def dfs(x):
    for i in task[x]:
        if not check[i]:
            check[i] = True
            if visit[i] == -1 or dfs(visit[i]): # 원래 직원을 새로운 일에 배정함. 배정이 안 되면 그대로 놔둠.
                visit[i] = x
                return True
    return False

result = 0

for i in range(n):
    check = [False]*(m+1)
    if dfs(i):
        result += 1
print(result)