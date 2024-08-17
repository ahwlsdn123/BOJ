import sys
input = sys.stdin.readline
MAX_VALUE = 1e10

n, m = map(int, input().split())

l = []
min_tree = [0]*(n*4)
max_tree = [0]*(n*4)

def min_init(start, end, index):
    if start == end:
        min_tree[index] = l[start-1]
        return min_tree[index]
    
    mid = (start+end) // 2
    min_tree[index] = min(min_init(start, mid, index*2), min_init(mid+1, end, index*2+1))
    return min_tree[index]

def max_init(start, end, index):
    if start == end:
        max_tree[index] = l[start-1]
        return max_tree[index]
    
    mid = (start+end) // 2
    max_tree[index] = max(max_init(start, mid, index*2), max_init(mid+1, end, index*2+1))
    return max_tree[index]

def min_find(start, end, index, left, right):
    if start > right or end < left:
        return MAX_VALUE
    
    if start >= left and end <= right:
        return min_tree[index]
    
    mid = (start + end) // 2
    sub_min = min(min_find(start, mid, index*2, left, right), min_find(mid+1, end, index*2+1, left, right))
    return sub_min

def max_find(start, end, index, left, right):
    if start > right or end < left:
        return 0
    
    if start >= left and end <= right:
        return max_tree[index]
    
    mid = (start + end) // 2
    sub_max = max(max_find(start, mid, index*2, left, right), max_find(mid+1, end, index*2+1, left, right))
    return sub_max

for _ in range(n):
    l.append(int(input()))

min_init(1, n, 1)
max_init(1, n, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(f"{min_find(1, n, 1, a, b)} {max_find(1, n, 1, a, b)}")