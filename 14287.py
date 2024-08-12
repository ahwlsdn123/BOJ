import sys
sys.setrecursionlimit(100000)
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
        p = parents[x]
        if p != 0:
            if index[p][1] < index[x][1]:
                index[p][1] = index[x][1]
            num_children[p] -= 1
            if num_children[p] == 0:
                leaf_q.append(p)

def update(t,v):
    s,e,x = 1,n,1
    while s < e:
        seg_tree[x] += v
        mid = (s+e) >> 1
        if t <= mid:
            e = mid
            x = 2*x
        else:
            s = mid+1
            x = 2*x+1
    seg_tree[x] += v

def search(l,r):
    q = [(1,n,1)]
    _ret = 0
    while q:
        s,e,x = q.pop()
        if e < l or r < s:
            continue
        if l <= s and e <= r:
            _ret += seg_tree[x]
            continue
        mid = (s+e) >> 1
        q.append((s,mid,2*x))
        q.append((mid+1,e,2*x+1))
    return _ret

n,m = map(int,input().split())
arr = [-1]+list(map(int,input().split()))
parents = [0]*(n+1)
num_children = [0]*(n+1)
index = [[0,0] for _ in range(n+1)]
children = [[] for _ in range(n+1)]

for i in range(2,n+1):
    p = arr[i]
    parents[i] = p
    num_children[p] += 1
    children[p].append(i)

dfs()

seg_tree = [0]*(4*n)

for _ in range(m):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        x,v = cmd[1:]
        t,_ = index[x]
        update(t,v)
    else:
        x = cmd[1]
        l,r = index[x]
        print(search(l,r))