import sys
input = sys.stdin.readline

def init(start,end,index):
    if start == end:
        seg_tree[index] = arr[start]
        return seg_tree[index]
    mid = start + end >> 1
    seg_tree[index] = init(start,mid,2*index) + init(mid+1,end,2*index+1)
    return seg_tree[index]

def update(s, e, x, l, r, dif):
    updateLazy(x, s, e)
    if e < l or r < s:
        return
    if l <= s and e <= r:
        seg_tree[x] += (e - s + 1) * dif
        if s != e:
            lazy[x * 2] += dif
            lazy[x * 2 + 1] += dif
        return
    m = s + e >> 1
    update(s, m, x * 2, l, r, dif)
    update(m + 1, e, x * 2 + 1, l, r, dif)
    seg_tree[x] = seg_tree[x * 2] + seg_tree[x * 2 + 1]
 
def updateLazy(x, s, e):
    if lazy[x]:
        seg_tree[x] += (e - s + 1) * lazy[x]
        if s != e:
            lazy[x * 2] += lazy[x]
            lazy[x * 2 + 1] += lazy[x]
        lazy[x] = 0
 
def getSum(s,e,x,l,r):
    updateLazy(x, s, e)
    if e < l or r < s:
        return 0
    if l <= s and e <= r:
        return seg_tree[x]
    m = s + e >> 1
    return getSum(s, m, x * 2, l, r) + getSum(m + 1, e, x * 2 + 1, l, r)
 
n,m,k = map(int, input().split())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
seg_tree = [0 for _ in range(4*n)]
lazy = [0 for _ in range(4*n)]
init(1,n,1)
for _ in range(m+k):
    cmd = input().rstrip()
    if cmd[0] == '1':
        _,b,c,d = map(int, cmd.split())
        update(1,n,1,b,c,d)
    else:
        _,b,c = map(int, cmd.split())
        print(getSum(1,n,1,b,c))