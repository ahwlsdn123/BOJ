# https://www.acmicpc.net/problem/13334

import sys
import heapq

n = int(sys.stdin.readline().strip())
locations = []
for _ in range(n):
    h, o = map(int, sys.stdin.readline().strip().split())
    locations.append((min(h,o), max(h,o)))
d = int(sys.stdin.readline().strip())

locations.sort(key=lambda x: (x[1], x[0]))

heap = []
max_cnt = 0

for location in locations:
    start, end = location
    heapq.heappush(heap, start)
    line_start = end - d
    while heap and heap[0] < line_start:
        heapq.heappop(heap)
    max_cnt = max(max_cnt, len(heap))

print(max_cnt)