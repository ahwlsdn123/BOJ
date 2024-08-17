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
            leaf_q.append(x)
            index[x][1] = cnt
            continue
        for c in children[x]:
            q.append(c)
    while leaf_q:
        x = leaf_q.pop()
        p = parents[x][0]
        if p:
            if index[p][1] < index[x][1]:
                index[p][1] = index[x][1]
            parents[p][1] -= 1
            if not parents[p][1]:
                leaf_q.append(p)

def propagate(s,e,x):
    if s != e:
        lazy[2*x] += lazy[x]
        lazy[2*x+1] += lazy[x]
    else:
        seg_tree[x] += lazy[x]
    lazy[x] = 0

def update(l,r,v):
    q = [(1,n,1)]
    while q:
        s,e,x = q.pop()
        propagate(s,e,x)
        if r < s or e < l:
            continue
        if l <= s and e <= r:
            lazy[x] += v
            continue
        mid = (s+e) >> 1
        q.append((s,mid,2*x))
        q.append((mid+1,e,2*x+1))

def search(t):
    s,e,x = 1,n,1
    while s < e:
        propagate(s,e,x)
        mid = (s+e) >> 1
        if t <= mid:
            e = mid
            x = 2*x
        else:
            s = mid+1
            x = 2*x+1
    propagate(s,e,x)
    return seg_tree[x]

n,m = map(int,input().split())
children = [[] for _ in range(n+1)]
parents = [[0,0] for _ in range(n+1)]
index = [[0,0] for _ in range(n+1)]
arr = [-1] + list(map(int,input().split()))
for i in range(2,n+1):
    p = arr[i]
    parents[i][0] = p
    parents[p][1] += 1
    children[p].append(i)
dfs()
seg_tree = [0]*(4*n+4)
lazy = [0]*(4*n+4)
for _ in range(m):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        a,b = cmd[1:]
        l,r = index[a]
        update(l,r,b)
    else:
        a = cmd[1]
        print(search(index[a][0]))