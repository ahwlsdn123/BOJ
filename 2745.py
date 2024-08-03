import sys
input = sys.stdin.readline

n, b = input().rstrip().split()
b = int(b)
answer = 0
for i in range(len(n)):
    if ord(n[i]) >= ord('A') and ord (n[i]) <= ord('Z'):
        answer += (ord(n[i])-ord('A')+10)*b**(len(n)-i-1)
    else:
        answer += int(n[i])*b**(len(n)-i-1)
print(answer)