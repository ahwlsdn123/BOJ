import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = 0
for i in range(n):
    x = int(input())
    while stack and stack[-1][1] > x:
        answer = max(answer, (i-stack[-1][0])*stack[-1][1], (i-stack[-1][0]+1)*x)
        stack.pop()
    stack.append([i,x])
while stack:
    answer = max(answer, (n-stack[-1][0])*stack[-1][1])
    stack.pop()
print(answer)