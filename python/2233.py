import sys
from collections import deque
from math import log2
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n+1)]
track = input().rstrip()