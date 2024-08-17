import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = deque(map(int, input().split()))
b = deque(map(int, input().split()))
m = int(input())
c = deque(map(int,input().split()))
print(b[a])