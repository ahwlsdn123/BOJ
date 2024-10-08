import sys
from math import *

input = sys.stdin.readline
INF = sys.maxsize

def min(a:list, b:list) -> list:
    if a[0] > b[0]:
        return b
    else:
        return a

def init(node, start, end):
    if start == end:
        segtree[node] = values[start]
        return segtree[node]
    
    mid = (start+end)//2
    segtree[node] = min(init(node*2, start, mid), init(node*2+1, mid+1, end))
    return segtree[node]

def query(node, start, end, left, right):
    if start > right or end < left:
        return [INF, INF]
    
    if left <= start and end <= right:
        return segtree[node]
    
    mid = (start+end)//2
    return min(query(node*2, start, mid, left, right), query(node*2+1, mid+1, end, left, right))

def update(node, start, end, index, x):
    if index < start or index > end:
        return [INF, INF]
    
    if start == end:
        segtree[node] = x
        return
    
    mid = (start+end)//2
    update(node*2, start, mid, index, x)
    update(node*2+1, mid+1, end, index, x)

    segtree[node] = min(segtree[node*2], segtree[node*2+1])

n = int(input())
temp = list(map(int, input().split()))
values = [[0,0] for _ in range(n)]

for i in range(n):
    values[i][0] = temp[i]
    values[i][1] = i+1

ts = 1 << (int(ceil(log2(n)))+1)
segtree = [0] * ts

init(1, 0, n-1)

m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        values[b-1][0] = c
        update(1, 0, n-1, b-1, values[b-1])
    
    else:
        print(query(1, 0, n-1, b-1, c-1)[1])