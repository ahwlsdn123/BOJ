import sys
input = sys.stdin.readline

h, m = map(int, input().split())
m -= 45
if m < 0:
    h = (h-1)%24
    m %= 60
    print(f"{h} {m}")
else:
    print(f"{h} {m}")