n = int(input())
nicks = set([])
answer = 0
for _ in range(n):
    m = input()
    if m == 'ENTER':
        answer += len(nicks)
        nicks = set([])
    else:
        nicks.add(m)
answer += len(nicks)
print(answer)