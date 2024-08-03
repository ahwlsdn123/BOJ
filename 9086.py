import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    string = input().rstrip()
    print(string[0], string[-1], sep="")