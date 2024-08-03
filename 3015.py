import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = 0
for _ in range(n):
    x = int(input())
    while stack and stack[-1][0] < x:
        cnt = stack[-1][1]
        answer += (cnt*(cnt+1))//2
        stack.pop()
        if stack:
            answer += cnt
    if stack and stack[-1][0] == x:
        stack[-1][1] += 1
    else:
        stack.append([x,1])
while stack:
    cnt = stack[-1][1]
    answer += (cnt*(cnt-1))//2
    stack.pop()
    if stack:
        answer += cnt
print(answer)