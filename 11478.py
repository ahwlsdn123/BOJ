import sys
input = sys.stdin.readline

s = input().rstrip()
set = set()
for i in range(1,len(s)+1):
    for j in range(len(s)-i+1):
        set.add(s[j:j+i])
print(len(set))