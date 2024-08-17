import sys
input = sys.stdin.readline

def dfs():
    q = [1]
    leaf_q = []
    cnt = 0
    while q:
        x = q.pop()
        cnt += 1
        index[x][0] = cnt
        if not children[x]:
            index[x][1] = cnt
            leaf_q.append(x)
            continue
        for c in children[x]:
            q.append(c)
    while leaf_q:
        x = leaf_q.pop()
        p = parent[x]
        if index[p][1] < index[x][1]:
            index[p][1] = index[x][1]
        num_children[p] -= 1
        if num_children[p] == 0:
            leaf_q.append(p)

def init(s,e,x):
    if s == e:
        seg_tree[x] = 1
        return
    mid = (s+e) >> 1
    init(s,mid,2*x)
    init(mid+1,e,2*x+1)
    seg_tree[x] = seg_tree[2*x] + seg_tree[2*x+1]

def propagate(s,e,x):
    if lazy[x] != 0:
        if lazy[x] == 1:
            seg_tree[x] = e-s+1
            if s != e:
                lazy[2*x] = lazy[x]
                lazy[2*x+1] = lazy[x]
        else:
            seg_tree[x] = 0
            if s != e:
                lazy[2*x] = lazy[x]
                lazy[2*x+1] = lazy[x]
        lazy[x] = 0

def update(s,e,x,l,r,v):
    propagate(s,e,x)
    if e < l or r < s:
        return
    if l <= s and e <= r:
        if v == 1:
            seg_tree[x] = e-s+1
            if s != e:
                lazy[2*x] = v
                lazy[2*x+1] = v
        else:
            seg_tree[x] = 0
            if s != e:
                lazy[2*x] = v
                lazy[2*x+1] = v
        return
    mid = (s+e) >> 1
    update(s,mid,2*x,l,r,v)
    update(mid+1,e,2*x+1,l,r,v)
    seg_tree[x] = seg_tree[2*x] + seg_tree[2*x+1]

def search(s,e,x,l,r):
    propagate(s,e,x)
    if e < l or r < s:
        return 0
    if l <= s and e <= r:
        return seg_tree[x]
    mid = (s+e) >> 1
    return search(s,mid,2*x,l,r) + search(mid+1,e,2*x+1,l,r)

n = int(input())
arr = [0] + list(map(int,input().split()))

parent = [0]*(n+1)
index = [[0,0] for _ in range(n+1)]
children = [[] for _ in range(n+1)]
num_children = [0]*(n+1)

for i in range(2,n+1):
    p = arr[i]
    parent[i] = p
    children[p].append(i)
    num_children[p] += 1

dfs()

seg_tree = [0]*(4*n)
lazy = [0]*(4*n)
init(1,n,1)

m = int(input())
for _ in range(m):
    q,i = map(int,input().split())
    if q == 1:
        l,r = index[i]
        if l < r:
            update(1,n,1,l+1,r,1) # 1: 켠다 / 2: 끈다
    elif q == 2:
        l,r = index[i]
        if l < r:
            update(1,n,1,l+1,r,2) # 1: 켠다 / 2: 끈다
    else:
        l,r = index[i]
        if l < r:
            print(search(1,n,1,l+1,r))
        else:
            print(0)