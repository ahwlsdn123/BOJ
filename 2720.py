import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    c = int(input())
    print(c//25, end=" ")
    c %= 25
    print(c//10, end=" ")
    c %= 10
    print(c//5, end=" ")
    c %= 5
    print(c)