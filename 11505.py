import sys
import math
input = sys.stdin.readline
MOD = 1000000007

def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
    else:
        mid = (start+end)//2
        tree[index] = init(start, mid, index*2) * init(mid+1, end, index*2+1) % MOD
    return tree[index]

def find_product(start, end, index, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[index]
    
    mid = (start+end)//2
    return find_product(start, mid, index*2, left, right) * find_product(mid+1, end, index*2+1, left, right) % MOD

def update(start, end, index, where, diff):
    if where < start or end < where:
        return
    
    if start == end:
        tree[index] = diff
    else:
        mid = (start+end)//2
        update(start, mid, index*2, where, diff)
        update(mid+1, end, index*2+1, where, diff)
        tree[index] = tree[index*2] * tree[index*2+1] % MOD

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * (1 << (int(math.ceil(math.log2(n)))+1))
init(0, n-1, 1)

for _ in range(m+k):
    a, b, c = map(int, input().split())

    if a == 1:
        update(0, n-1, 1, b-1, c)

    else:
        print(find_product(0, n-1, 1, b-1, c-1))